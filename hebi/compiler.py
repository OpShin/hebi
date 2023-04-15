import logging
from logging import getLogger
from ast import fix_missing_locations

from .optimize.optimize_remove_comments import OptimizeRemoveDeadconstants
from .rewrite.rewrite_forbidden_overwrites import RewriteForbiddenOverwrites
from .rewrite.rewrite_guaranteed_variables import RewriteGuaranteedVariables
from .rewrite.rewrite_import import RewriteImport
from .rewrite.rewrite_import_dataclasses import RewriteImportDataclasses
from .rewrite.rewrite_import_hashlib import RewriteImportHashlib
from .rewrite.rewrite_import_plutusdata import RewriteImportPlutusData
from .rewrite.rewrite_import_typing import RewriteImportTyping
from .rewrite.rewrite_inject_builtins import RewriteInjectBuiltins
from .rewrite.rewrite_inject_builtin_constr import RewriteInjectBuiltinsConstr
from .rewrite.rewrite_remove_type_stuff import RewriteRemoveTypeStuff
from .rewrite.rewrite_subscript38 import RewriteSubscript38
from .rewrite.rewrite_tuple_assign import RewriteTupleAssign
from .rewrite.rewrite_duplicate_assignment import RewriteDuplicateAssignment
from .rewrite.rewrite_zero_ary import RewriteZeroAry
from .optimize.optimize_remove_pass import OptimizeRemovePass
from .optimize.optimize_remove_deadvars import OptimizeRemoveDeadvars
from .type_inference import *
from .util import CompilingNodeTransformer, PowImpl
from .typed_ast import transform_ext_params_map, transform_output_map, RawPlutoExpr


_LOGGER = logging.getLogger(__name__)

BinOpMap = {
    Add: {
        IntegerInstanceType: {
            IntegerInstanceType: plt.AddInteger,
        },
        ByteStringInstanceType: {
            ByteStringInstanceType: plt.AppendByteString,
        },
        StringInstanceType: {
            StringInstanceType: plt.AppendString,
        },
    },
    Sub: {
        IntegerInstanceType: {
            IntegerInstanceType: plt.SubtractInteger,
        }
    },
    Mult: {
        IntegerInstanceType: {
            IntegerInstanceType: plt.MultiplyInteger,
        }
    },
    FloorDiv: {
        IntegerInstanceType: {
            IntegerInstanceType: plt.DivideInteger,
        }
    },
    Mod: {
        IntegerInstanceType: {
            IntegerInstanceType: plt.ModInteger,
        }
    },
    Pow: {
        IntegerInstanceType: {
            IntegerInstanceType: lambda x, y: plt.Apply(plt.RecFun(PowImpl), x, y),
        }
    },
}

BoolOpMap = {
    And: plt.And,
    Or: plt.Or,
}

UnaryOpMap = {
    Not: {BoolInstanceType: plt.Not},
    USub: {IntegerInstanceType: lambda x: plt.SubtractInteger(plt.Integer(0), x)},
}

ConstantMap = {
    str: plt.Text,
    bytes: lambda x: plt.ByteString(x),
    int: lambda x: plt.Integer(x),
    bool: plt.Bool,
    type(None): lambda _: plt.Unit(),
}


def wrap_validator_double_function(x: plt.AST, pass_through: int = 0):
    """
    Wraps the validator function to enable a double function as minting script

    pass_through defines how many parameters x would normally take and should be passed through to x
    """
    return plt.Lambda(
        [f"v{i}" for i in range(pass_through)] + ["a0", "a1"],
        plt.Let(
            [("p", plt.Apply(x, *(plt.Var(f"v{i}") for i in range(pass_through))))],
            plt.Ite(
                # if the second argument has constructor 0 = script context
                plt.DelayedChooseData(
                    plt.Var("a1"),
                    plt.EqualsInteger(plt.Constructor(plt.Var("a1")), plt.Integer(0)),
                    plt.Bool(False),
                    plt.Bool(False),
                    plt.Bool(False),
                    plt.Bool(False),
                ),
                # call the validator with a0, a1, and plug in Unit for data
                plt.Apply(plt.Var("p"), plt.Unit(), plt.Var("a0"), plt.Var("a1")),
                # else call the validator with a0, a1 and return (now partially bound)
                plt.Apply(plt.Var("p"), plt.Var("a0"), plt.Var("a1")),
            ),
        ),
    )


class UPLCCompiler(CompilingNodeTransformer):
    """
    Expects a TypedAST and returns UPLC/Pluto like code
    """

    step = "Compiling python statements to UPLC"

    def __init__(self, force_three_params=False, validator_function_name="validator"):
        self.force_three_params = force_three_params
        self.validator_function_name = validator_function_name

    def visit_sequence(
        self, node_seq: typing.List[typedstmt]
    ) -> typing.Callable[[plt.AST], plt.AST]:
        def g(s: plt.AST):
            for n in reversed(node_seq):
                compiled_stmt = self.visit(n)
                s = compiled_stmt(s)
            return s

        return g

    def visit_BinOp(self, node: TypedBinOp) -> plt.AST:
        opmap = BinOpMap.get(type(node.op))
        if opmap is None:
            raise NotImplementedError(f"Operation {node.op} is not implemented")
        opmap2 = opmap.get(node.left.typ)
        if opmap2 is None:
            raise NotImplementedError(
                f"Operation {node.op} is not implemented for left type {node.left.typ}"
            )
        op = opmap2.get(node.right.typ)
        if opmap2 is None:
            raise NotImplementedError(
                f"Operation {node.op} is not implemented for left type {node.left.typ} and right type {node.right.typ}"
            )
        return op(self.visit(node.left), self.visit(node.right))

    def visit_BoolOp(self, node: TypedBoolOp) -> plt.AST:
        op = BoolOpMap.get(type(node.op))
        assert len(node.values) >= 2, "Need to compare at least to values"
        ops = op(
            self.visit(node.values[0]),
            self.visit(node.values[1]),
        )
        for v in node.values[2:]:
            ops = op(ops, self.visit(v))
        return ops

    def visit_UnaryOp(self, node: TypedUnaryOp) -> plt.AST:
        opmap = UnaryOpMap.get(type(node.op))
        assert opmap is not None, f"Operator {type(node.op)} is not supported"
        op = opmap.get(node.operand.typ)
        assert (
            op is not None
        ), f"Operator {type(node.op)} is not supported for type {node.operand.typ}"
        return op(self.visit(node.operand))

    def visit_Compare(self, node: TypedCompare) -> plt.AST:
        assert len(node.ops) == 1, "Only single comparisons are supported"
        assert len(node.comparators) == 1, "Only single comparisons are supported"
        cmpop = node.ops[0]
        comparator = node.comparators[0].typ
        op = node.left.typ.cmp(cmpop, comparator)
        return plt.Apply(
            op,
            self.visit(node.left),
            self.visit(node.comparators[0]),
        )

    def visit_Module(self, node: TypedModule) -> plt.AST:
        # find main function
        # TODO can use more sophisiticated procedure here i.e. functions marked by comment
        main_fun: typing.Optional[InstanceType] = None
        for s in node.body:
            if isinstance(s, FunctionDef) and s.name == self.validator_function_name:
                main_fun = s
        assert (
            main_fun is not None
        ), f"Could not find function named {self.validator_function_name}"
        main_fun_typ: FunctionType = main_fun.typ.typ
        assert isinstance(
            main_fun_typ, FunctionType
        ), f"Variable named {self.validator_function_name} is not of type function"

        # check if this is a contract written to double function
        enable_double_func_mint_spend = False
        if len(main_fun_typ.argtyps) >= 3 and self.force_three_params:
            # check if is possible
            second_last_arg = main_fun_typ.argtyps[-2]
            assert isinstance(
                second_last_arg, InstanceType
            ), "Can not pass Class into validator"
            if isinstance(second_last_arg.typ, UnionType):
                possible_types = second_last_arg.typ.typs
            else:
                possible_types = [second_last_arg.typ]
            if any(isinstance(t, UnitType) for t in possible_types):
                _LOGGER.warning(
                    "The redeemer is annotated to be 'None'. This value is usually encoded in PlutusData with constructor id 0 and no fields. If you want the script to double function as minting and spending script, annotate the second argument with 'NoRedeemer'."
                )
            enable_double_func_mint_spend = not any(
                (isinstance(t, RecordType) and t.record.constructor == 0)
                or isinstance(t, UnitType)
                for t in possible_types
            )
            if not enable_double_func_mint_spend:
                _LOGGER.warning(
                    "The second argument to the validator function potentially has constructor id 0. The validator will not be able to double function as minting script and spending script."
                )

        body = node.body + [
            TypedReturn(
                value=Name(
                    id=self.validator_function_name,
                    typ=InstanceType(main_fun_typ),
                    ctx=Load(),
                ),
                typ=InstanceType(main_fun_typ),
            )
        ]

        validator = plt.Lambda(
            [f"p{i}" for i, _ in enumerate(main_fun_typ.argtyps)],
            transform_output_map(main_fun_typ.rettyp)(
                plt.Let(
                    [
                        (
                            "val",
                            self.visit_sequence(body)(
                                plt.ConstrData(plt.Integer(0), plt.EmptyDataList())
                            ),
                        ),
                    ],
                    plt.Apply(
                        plt.Var("val"),
                        plt.Var("val"),
                        *[
                            transform_ext_params_map(a)(plt.Var(f"p{i}"))
                            for i, a in enumerate(main_fun_typ.argtyps)
                        ],
                    ),
                ),
            ),
        )
        if enable_double_func_mint_spend:
            validator = wrap_validator_double_function(
                validator, pass_through=len(main_fun_typ.argtyps) - 3
            )
        elif self.force_three_params:
            # Error if the double function is enforced but not possible
            raise RuntimeError(
                "The contract can not always detect if it was passed three or two parameters on-chain."
            )
        cp = plt.Program((1, 0, 0), validator)
        return cp

    def visit_Constant(self, node: TypedConstant) -> plt.AST:
        plt_type = ConstantMap.get(type(node.value))
        if plt_type is None:
            raise NotImplementedError(
                f"Constants of type {type(node.value)} are not supported"
            )
        return plt_type(node.value)

    def visit_NoneType(self, _: typing.Optional[typing.Any]) -> plt.AST:
        return plt.Unit()

    def visit_Assign(self, node: TypedAssign) -> typing.Callable[[plt.AST], plt.AST]:
        assert (
            len(node.targets) == 1
        ), "Assignments to more than one variable not supported yet"
        assert isinstance(
            node.targets[0], Name
        ), "Assignments to other things then names are not supported"
        compiled_e = self.visit(node.value)
        varname = node.targets[0].id
        return lambda x: plt.Let([(varname, compiled_e)], x)

    def visit_AnnAssign(self, node: AnnAssign) -> typing.Callable[[plt.AST], plt.AST]:
        assert isinstance(
            node.target, Name
        ), "Assignments to other things than names are not supported"
        assert isinstance(
            node.target.typ, InstanceType
        ), "Can only assign instances to instances"
        compiled_e = self.visit(node.value)
        # (\{STATEMONAD} -> (\x -> if (x ==b {self.visit(node.targets[0])}) then ({compiled_e} {STATEMONAD}) else ({STATEMONAD} x)))
        val = compiled_e
        if isinstance(node.value.typ, InstanceType) and isinstance(
            node.value.typ.typ, AnyType
        ):
            # we need to map this as it will originate from PlutusData
            # AnyType is the only type other than the builtin itself that can be cast to builtin values
            val = transform_ext_params_map(node.target.typ)(val)
        if isinstance(node.target.typ, InstanceType) and isinstance(
            node.target.typ.typ, AnyType
        ):
            # we need to map this back as it will be treated as PlutusData
            # AnyType is the only type other than the builtin itself that can be cast to from builtin values
            val = transform_output_map(node.value.typ)(val)
        return lambda x: plt.Let([(node.target.id, val)], x)

    def visit_Name(self, node: TypedName) -> plt.AST:
        # depending on load or store context, return the value of the variable or its name
        if not isinstance(node.ctx, Load):
            raise NotImplementedError(f"Context {node.ctx} not supported")
        if isinstance(node.typ, ClassType):
            # if this is not an instance but a class, call the constructor
            return node.typ.constr()
        return plt.Var(node.id)

    def visit_Expr(self, node: TypedExpr) -> typing.Callable[[plt.AST], plt.AST]:
        # we exploit UPLCs eager evaluation here
        # the expression is computed even though its value is eventually discarded
        # Note this really only makes sense for Trace
        # we use an invalid name here to avoid conflicts
        return lambda x: plt.Apply(plt.Lambda(["0"], x), self.visit(node.value))

    def visit_Call(self, node: TypedCall) -> plt.AST:
        # compiled_args = " ".join(f"({self.visit(a)} {STATEMONAD})" for a in node.args)
        # return rf"(\{STATEMONAD} -> ({self.visit(node.func)} {compiled_args})"
        # TODO function is actually not of type polymorphic function type here anymore
        if isinstance(node.func.typ, PolymorphicFunctionInstanceType):
            # edge case for weird builtins that are polymorphic
            func_plt = node.func.typ.polymorphic_function.impl_from_args(
                node.func.typ.typ.argtyps
            )
        else:
            func_plt = self.visit(node.func)
        args = []
        for a, t in zip(node.args, node.func.typ.typ.argtyps):
            assert isinstance(t, InstanceType)
            # pass in all arguments evaluated with the statemonad
            a_int = self.visit(a)
            if isinstance(t.typ, AnyType):
                # if the function expects input of generic type data, wrap data before passing it inside
                a_int = transform_output_map(a.typ)(a_int)
            args.append(a_int)
        return plt.Apply(
            plt.RecFun(func_plt),
            *args,
        )

    def visit_FunctionDef(
        self, node: TypedFunctionDef
    ) -> typing.Callable[[plt.AST], plt.AST]:
        body = node.body.copy()
        # defaults to returning None if there is no return statement
        if node.typ.typ.rettyp.typ == AnyType():
            ret_val = plt.ConstrData(plt.Integer(0), plt.EmptyDataList())
        else:
            ret_val = plt.Unit()
        compiled_body = self.visit_sequence(body)(ret_val)
        return lambda x: plt.Let(
            [
                (
                    node.name,
                    plt.Lambda(
                        [node.name] + [a.arg for a in node.args.args],
                        compiled_body,
                    ),
                )
            ],
            x,
        )

    def visit_If(self, node: TypedIf) -> typing.Callable[[plt.AST], plt.AST]:
        return lambda x: plt.Ite(
            self.visit(node.test),
            self.visit_sequence(node.body)(x),
            self.visit_sequence(node.orelse)(x),
        )

    def visit_Return(self, node: TypedReturn) -> typing.Callable[[plt.AST], plt.AST]:
        # Throw away the term we were passed, this is going to be the last!
        compiled_return = self.visit(node.value)
        if isinstance(node.typ.typ, AnyType):
            # if the function returns generic data, wrap the function return value
            compiled_return = transform_output_map(node.value.typ)(compiled_return)
        return lambda _: compiled_return

    def visit_Pass(self, node: TypedPass) -> typing.Callable[[plt.AST], plt.AST]:
        return lambda x: x

    def visit_Subscript(self, node: TypedSubscript) -> plt.AST:
        assert isinstance(
            node.value.typ, InstanceType
        ), "Can only access elements of instances, not classes"
        if isinstance(node.value.typ.typ, TupleType):
            assert isinstance(
                node.slice, Constant
            ), "Only constant index access for tuples is supported"
            assert isinstance(
                node.slice.value, int
            ), "Only constant index integer access for tuples is supported"
            index = node.slice.value
            if index < 0:
                index += len(node.value.typ.typ.typs)
            assert isinstance(node.ctx, Load), "Tuples are read-only"
            return plt.FunctionalTupleAccess(
                self.visit(node.value),
                index,
                len(node.value.typ.typ.typs),
            )
        if isinstance(node.value.typ.typ, PairType):
            assert isinstance(
                node.slice, Constant
            ), "Only constant index access for pairs is supported"
            assert isinstance(
                node.slice.value, int
            ), "Only constant index integer access for pairs is supported"
            index = node.slice.value
            if index < 0:
                index += 2
            assert isinstance(node.ctx, Load), "Pairs are read-only"
            assert (
                0 <= index < 2
            ), f"Pairs only have 2 elements, index should be 0 or 1, is {node.slice.value}"
            member_func = plt.FstPair if index == 0 else plt.SndPair
            # the content of pairs is always Data, so we need to unwrap
            member_typ = node.typ
            return transform_ext_params_map(member_typ)(
                member_func(
                    self.visit(node.value),
                ),
            )
        if isinstance(node.value.typ.typ, ListType):
            assert (
                node.slice.typ == IntegerInstanceType
            ), "Only single element list index access supported"
            return plt.Let(
                [
                    ("l", self.visit(node.value)),
                    (
                        "raw_i",
                        self.visit(node.slice),
                    ),
                    (
                        "i",
                        plt.Ite(
                            plt.LessThanInteger(plt.Var("raw_i"), plt.Integer(0)),
                            plt.AddInteger(
                                plt.Var("raw_i"), plt.LengthList(plt.Var("l"))
                            ),
                            plt.Var("raw_i"),
                        ),
                    ),
                ],
                plt.IndexAccessList(plt.Var("l"), plt.Var("i")),
            )
        elif isinstance(node.value.typ.typ, DictType):
            dict_typ = node.value.typ.typ
            if not isinstance(node.slice, Slice):
                return plt.Let(
                    [
                        (
                            "key",
                            self.visit(node.slice),
                        )
                    ],
                    transform_ext_params_map(dict_typ.value_typ)(
                        plt.SndPair(
                            plt.FindList(
                                self.visit(node.value),
                                plt.Lambda(
                                    ["x"],
                                    plt.EqualsData(
                                        transform_output_map(dict_typ.key_typ)(
                                            plt.Var("key")
                                        ),
                                        plt.FstPair(plt.Var("x")),
                                    ),
                                ),
                                plt.TraceError("KeyError"),
                            ),
                        ),
                    ),
                )
        elif isinstance(node.value.typ.typ, ByteStringType):
            if not isinstance(node.slice, Slice):
                return plt.Let(
                    [
                        (
                            "bs",
                            self.visit(node.value),
                        ),
                        (
                            "raw_ix",
                            self.visit(node.slice),
                        ),
                        (
                            "ix",
                            plt.Ite(
                                plt.LessThanInteger(plt.Var("raw_ix"), plt.Integer(0)),
                                plt.AddInteger(
                                    plt.Var("raw_ix"),
                                    plt.LengthOfByteString(plt.Var("bs")),
                                ),
                                plt.Var("raw_ix"),
                            ),
                        ),
                    ],
                    plt.IndexByteString(plt.Var("bs"), plt.Var("ix")),
                )
            elif isinstance(node.slice, Slice):
                return plt.Let(
                    [
                        (
                            "bs",
                            self.visit(node.value),
                        ),
                        (
                            "raw_i",
                            self.visit(node.slice.lower),
                        ),
                        (
                            "i",
                            plt.Ite(
                                plt.LessThanInteger(plt.Var("raw_i"), plt.Integer(0)),
                                plt.AddInteger(
                                    plt.Var("raw_i"),
                                    plt.LengthOfByteString(plt.Var("bs")),
                                ),
                                plt.Var("raw_i"),
                            ),
                        ),
                        (
                            "raw_j",
                            self.visit(node.slice.upper),
                        ),
                        (
                            "j",
                            plt.Ite(
                                plt.LessThanInteger(plt.Var("raw_j"), plt.Integer(0)),
                                plt.AddInteger(
                                    plt.Var("raw_j"),
                                    plt.LengthOfByteString(plt.Var("bs")),
                                ),
                                plt.Var("raw_j"),
                            ),
                        ),
                        (
                            "drop",
                            plt.Ite(
                                plt.LessThanEqualsInteger(plt.Var("i"), plt.Integer(0)),
                                plt.Integer(0),
                                plt.Var("i"),
                            ),
                        ),
                        (
                            "take",
                            plt.SubtractInteger(plt.Var("j"), plt.Var("drop")),
                        ),
                    ],
                    plt.Ite(
                        plt.LessThanEqualsInteger(plt.Var("j"), plt.Var("i")),
                        plt.ByteString(b""),
                        plt.SliceByteString(
                            plt.Var("drop"),
                            plt.Var("take"),
                            plt.Var("bs"),
                        ),
                    ),
                )
        raise NotImplementedError(
            f'Could not implement subscript "{node.slice}" of "{node.value}"'
        )

    def visit_Tuple(self, node: TypedTuple) -> plt.AST:
        return plt.FunctionalTuple(*(self.visit(e) for e in node.elts))

    def visit_ClassDef(
        self, node: TypedClassDef
    ) -> typing.Callable[[plt.AST], plt.AST]:
        return lambda x: plt.Let([(node.name, node.class_typ.constr())], x)

    def visit_Attribute(self, node: TypedAttribute) -> plt.AST:
        assert isinstance(
            node.typ, InstanceType
        ), "Can only access attributes of instances"
        obj = self.visit(node.value)
        attr = node.value.typ.attribute(node.attr)
        return plt.Apply(attr, obj)

    def visit_Assert(self, node: TypedAssert) -> typing.Callable[[plt.AST], plt.AST]:
        return lambda x: plt.Ite(
            self.visit(node.test),
            x,
            plt.Apply(
                plt.Error(),
                plt.Trace(self.visit(node.msg), plt.Unit())
                if node.msg is not None
                else plt.Unit(),
            ),
        )

    def visit_RawPlutoExpr(self, node: RawPlutoExpr) -> plt.AST:
        return node.expr

    def visit_List(self, node: TypedList) -> plt.AST:
        assert isinstance(node.typ, InstanceType)
        assert isinstance(node.typ.typ, ListType)
        l = empty_list(node.typ.typ.typ)
        for e in reversed(node.elts):
            l = plt.MkCons(self.visit(e), l)
        return l

    def visit_Dict(self, node: TypedDict) -> plt.AST:
        assert isinstance(node.typ, InstanceType)
        assert isinstance(node.typ.typ, DictType)
        key_type = node.typ.typ.key_typ
        value_type = node.typ.typ.value_typ
        l = plt.EmptyDataPairList()
        for k, v in zip(node.keys, node.values):
            l = plt.MkCons(
                plt.MkPairData(
                    transform_output_map(key_type)(self.visit(k)),
                    transform_output_map(value_type)(self.visit(v)),
                ),
                l,
            )
        return l

    def visit_IfExp(self, node: TypedIfExp) -> plt.AST:
        return plt.Ite(
            self.visit(node.test),
            self.visit(node.body),
            self.visit(node.orelse),
        )

    def visit_ListComp(self, node: TypedListComp) -> plt.AST:
        assert len(node.generators) == 1, "Currently only one generator supported"
        gen = node.generators[0]
        assert isinstance(gen.iter.typ, InstanceType), "Only lists are valid generators"
        assert isinstance(gen.iter.typ.typ, ListType), "Only lists are valid generators"
        assert isinstance(
            gen.target, Name
        ), "Can only assign value to singleton element"
        lst = self.visit(gen.iter)
        ifs = None
        for ifexpr in gen.ifs:
            if ifs is None:
                ifs = self.visit(ifexpr)
            else:
                ifs = plt.And(ifs, self.visit(ifexpr))
        map_fun = plt.Lambda(
            [gen.target.id],
            self.visit(node.elt),
        )
        empty_list_con = empty_list(node.elt.typ)
        if ifs is not None:
            filter_fun = plt.Lambda(
                [gen.target.id],
                ifs,
            )
            return plt.MapFilterList(
                lst,
                filter_fun,
                map_fun,
                empty_list_con,
            )
        else:
            return plt.MapList(
                lst,
                map_fun,
                empty_list_con,
            )

    def generic_visit(self, node: AST) -> plt.AST:
        raise NotImplementedError(f"Can not compile {node}")


def compile(
    prog: AST,
    filename=None,
    force_three_params=False,
    validator_function_name="validator",
):
    rewrite_steps = [
        # Important to call this one first - it imports all further files
        RewriteImport(filename=filename),
        # Rewrites that simplify the python code
        RewriteSubscript38(),
        RewriteTupleAssign(),
        RewriteImportPlutusData(),
        RewriteImportHashlib(),
        RewriteImportTyping(),
        RewriteForbiddenOverwrites(),
        RewriteImportDataclasses(),
        RewriteInjectBuiltins(),
        RewriteDuplicateAssignment(),
        RewriteGuaranteedVariables(),
        # The type inference needs to be run after complex python operations were rewritten
        AggressiveTypeInferencer(),
        # Rewrites that circumvent the type inference or use its results
        RewriteZeroAry(),
        RewriteInjectBuiltinsConstr(),
        RewriteRemoveTypeStuff(),
    ]
    for s in rewrite_steps:
        prog = s.visit(prog)
        prog = fix_missing_locations(prog)

    # from here on raw uplc may occur, so we dont attempt to fix locations
    compile_pipeline = [
        # Apply optimizations
        OptimizeRemoveDeadvars(),
        OptimizeRemoveDeadconstants(),
        OptimizeRemovePass(),
        # the compiler runs last
        UPLCCompiler(
            force_three_params=force_three_params,
            validator_function_name=validator_function_name,
        ),
    ]
    for s in compile_pipeline:
        prog = s.visit(prog)

    return prog
