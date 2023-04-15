from ast import *
from copy import copy
from collections import defaultdict

from ..util import CompilingNodeVisitor, CompilingNodeTransformer
from ..type_inference import INITIAL_SCOPE

"""
Checks that used variables are bound in every branch of preceding control flow
"""


class RewriteGuaranteedVariables(CompilingNodeTransformer):
    step = "Ensure variables are bound"

    loaded_vars = None
    # names that are guaranteed to be available to the current node
    # this acts differently to the type inferencer! in particular, ite/while/for all produce their own scope
    guaranteed_avail_names = [
        list(INITIAL_SCOPE.keys()) + ["List", "Dict", "Union", "isinstance"]
    ]

    def guaranteed(self, name: str) -> bool:
        name = name
        for scope in reversed(self.guaranteed_avail_names):
            if name in scope:
                return True
        return False

    def enter_scope(self):
        self.guaranteed_avail_names.append([])

    def exit_scope(self):
        self.guaranteed_avail_names.pop()

    def set_guaranteed(self, name: str):
        self.guaranteed_avail_names[-1].append(name)

    def visit_Module(self, node: Module) -> Module:
        # repeat until no more change due to removal
        # i.e. b = a; c = b needs 2 passes to remove c and b
        node_cp = copy(node)
        self.enter_scope()
        node_cp.body = [self.visit(s) for s in node_cp.body]
        self.exit_scope()
        return node_cp

    def visit_If(self, node: If):
        node_cp = copy(node)
        node_cp.test = self.visit(node.test)
        self.enter_scope()
        node_cp.body = [self.visit(s) for s in node.body]
        scope_body_cp = self.guaranteed_avail_names[-1].copy()
        self.exit_scope()
        self.enter_scope()
        node_cp.orelse = [self.visit(s) for s in node.orelse]
        scope_orelse_cp = self.guaranteed_avail_names[-1].copy()
        self.exit_scope()
        # what remains after this in the scope is the intersection of both
        for var in set(scope_body_cp).intersection(scope_orelse_cp):
            self.set_guaranteed(var)
        return node_cp

    def visit_While(self, node: While):
        node_cp = copy(node)
        node_cp.test = self.visit(node.test)
        self.enter_scope()
        node_cp.body = [self.visit(s) for s in node.body]
        node_cp.orelse = [self.visit(s) for s in node.orelse]
        self.exit_scope()
        return node_cp

    def visit_For(self, node: For):
        node_cp = copy(node)
        assert isinstance(node.target, Name), "Can only assign to singleton name"
        self.enter_scope()
        self.guaranteed(node.target.id)
        node_cp.body = [self.visit(s) for s in node.body]
        node_cp.orelse = [self.visit(s) for s in node.orelse]
        self.exit_scope()
        return node_cp

    def visit_ListComp(self, node: ListComp):
        assert len(node.generators) == 1, "Currently only one generator supported"
        gen = node.generators[0]
        assert isinstance(
            gen.target, Name
        ), "Can only assign value to singleton element"
        assert isinstance(gen.target, Name), "Can only assign to singleton name"
        node_cp = copy(node)
        node_cp.generators = [copy(gen)]
        self.enter_scope()
        self.set_guaranteed(gen.target.id)
        node_cp.generators[0].ifs = [self.visit(if_expr) for if_expr in gen.ifs]
        node_cp.elt = self.visit(node.elt)
        self.exit_scope()
        return node_cp

    def visit_Assign(self, node: Assign):
        for t in node.targets:
            assert isinstance(t, Name), f"Need to have name, not {t.__class__}"
            self.set_guaranteed(t.id)
        return self.generic_visit(node)

    def visit_AnnAssign(self, node: AnnAssign):
        assert isinstance(
            node.target, Name
        ), f"Need to have name, not {node.target.__class__}"
        self.set_guaranteed(node.target.id)
        return self.generic_visit(node)

    def visit_ClassDef(self, node: ClassDef):
        self.set_guaranteed(node.name)
        return node

    def visit_FunctionDef(self, node: FunctionDef):
        node_cp = copy(node)
        self.set_guaranteed(node.name)
        self.enter_scope()
        # variable names are available here
        for a in node.args.args:
            self.set_guaranteed(a.arg)
        node_cp.body = [self.visit(s) for s in node.body]
        self.exit_scope()
        return node_cp

    def visit_Name(self, node: Name):
        if isinstance(node.ctx, Load):
            assert self.guaranteed(
                node.id
            ), f"Variable {node.id} is not initialized in (every branch of) preceding control flow"
        return self.generic_visit(node)
