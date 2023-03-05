# Compiler

[hebi Index](../README.md#hebi-index) /
[Hebi](./index.md#hebi) /
Compiler

> Auto-generated documentation for [hebi.compiler](https://github.com/ImperatorLang/hebi/blob/master/hebi/compiler.py) module.

- [Compiler](#compiler)
  - [UPLCCompiler](#uplccompiler)
    - [UPLCCompiler().generic_visit](#uplccompiler()generic_visit)
    - [UPLCCompiler().visit_AnnAssign](#uplccompiler()visit_annassign)
    - [UPLCCompiler().visit_Assert](#uplccompiler()visit_assert)
    - [UPLCCompiler().visit_Assign](#uplccompiler()visit_assign)
    - [UPLCCompiler().visit_Attribute](#uplccompiler()visit_attribute)
    - [UPLCCompiler().visit_BinOp](#uplccompiler()visit_binop)
    - [UPLCCompiler().visit_BoolOp](#uplccompiler()visit_boolop)
    - [UPLCCompiler().visit_Call](#uplccompiler()visit_call)
    - [UPLCCompiler().visit_ClassDef](#uplccompiler()visit_classdef)
    - [UPLCCompiler().visit_Compare](#uplccompiler()visit_compare)
    - [UPLCCompiler().visit_Constant](#uplccompiler()visit_constant)
    - [UPLCCompiler().visit_Dict](#uplccompiler()visit_dict)
    - [UPLCCompiler().visit_Expr](#uplccompiler()visit_expr)
    - [UPLCCompiler().visit_FunctionDef](#uplccompiler()visit_functiondef)
    - [UPLCCompiler().visit_If](#uplccompiler()visit_if)
    - [UPLCCompiler().visit_IfExp](#uplccompiler()visit_ifexp)
    - [UPLCCompiler().visit_List](#uplccompiler()visit_list)
    - [UPLCCompiler().visit_ListComp](#uplccompiler()visit_listcomp)
    - [UPLCCompiler().visit_Module](#uplccompiler()visit_module)
    - [UPLCCompiler().visit_Name](#uplccompiler()visit_name)
    - [UPLCCompiler().visit_NoneType](#uplccompiler()visit_nonetype)
    - [UPLCCompiler().visit_Pass](#uplccompiler()visit_pass)
    - [UPLCCompiler().visit_RawPlutoExpr](#uplccompiler()visit_rawplutoexpr)
    - [UPLCCompiler().visit_Return](#uplccompiler()visit_return)
    - [UPLCCompiler().visit_Subscript](#uplccompiler()visit_subscript)
    - [UPLCCompiler().visit_Tuple](#uplccompiler()visit_tuple)
    - [UPLCCompiler().visit_UnaryOp](#uplccompiler()visit_unaryop)
    - [UPLCCompiler().visit_sequence](#uplccompiler()visit_sequence)
  - [compile](#compile)
  - [wrap_validator_double_function](#wrap_validator_double_function)

## UPLCCompiler

[Show source in compiler.py:116](https://github.com/ImperatorLang/hebi/blob/master/hebi/compiler.py#L116)

Expects a TypedAST and returns UPLC/Pluto like code

#### Signature

```python
class UPLCCompiler(CompilingNodeTransformer):
    def __init__(self, force_three_params=False):
        ...
```

### UPLCCompiler().generic_visit

[Show source in compiler.py:613](https://github.com/ImperatorLang/hebi/blob/master/hebi/compiler.py#L613)

#### Signature

```python
def generic_visit(self, node: AST) -> plt.AST:
    ...
```

### UPLCCompiler().visit_AnnAssign

[Show source in compiler.py:287](https://github.com/ImperatorLang/hebi/blob/master/hebi/compiler.py#L287)

#### Signature

```python
def visit_AnnAssign(self, node: AnnAssign) -> typing.Callable[[plt.AST], plt.AST]:
    ...
```

### UPLCCompiler().visit_Assert

[Show source in compiler.py:529](https://github.com/ImperatorLang/hebi/blob/master/hebi/compiler.py#L529)

#### Signature

```python
def visit_Assert(self, node: TypedAssert) -> typing.Callable[[plt.AST], plt.AST]:
    ...
```

### UPLCCompiler().visit_Assign

[Show source in compiler.py:276](https://github.com/ImperatorLang/hebi/blob/master/hebi/compiler.py#L276)

#### Signature

```python
def visit_Assign(self, node: TypedAssign) -> typing.Callable[[plt.AST], plt.AST]:
    ...
```

### UPLCCompiler().visit_Attribute

[Show source in compiler.py:521](https://github.com/ImperatorLang/hebi/blob/master/hebi/compiler.py#L521)

#### Signature

```python
def visit_Attribute(self, node: TypedAttribute) -> plt.AST:
    ...
```

### UPLCCompiler().visit_BinOp

[Show source in compiler.py:137](https://github.com/ImperatorLang/hebi/blob/master/hebi/compiler.py#L137)

#### Signature

```python
def visit_BinOp(self, node: TypedBinOp) -> plt.AST:
    ...
```

### UPLCCompiler().visit_BoolOp

[Show source in compiler.py:153](https://github.com/ImperatorLang/hebi/blob/master/hebi/compiler.py#L153)

#### Signature

```python
def visit_BoolOp(self, node: TypedBoolOp) -> plt.AST:
    ...
```

### UPLCCompiler().visit_Call

[Show source in compiler.py:317](https://github.com/ImperatorLang/hebi/blob/master/hebi/compiler.py#L317)

#### Signature

```python
def visit_Call(self, node: TypedCall) -> plt.AST:
    ...
```

### UPLCCompiler().visit_ClassDef

[Show source in compiler.py:516](https://github.com/ImperatorLang/hebi/blob/master/hebi/compiler.py#L516)

#### Signature

```python
def visit_ClassDef(self, node: TypedClassDef) -> typing.Callable[[plt.AST], plt.AST]:
    ...
```

### UPLCCompiler().visit_Compare

[Show source in compiler.py:173](https://github.com/ImperatorLang/hebi/blob/master/hebi/compiler.py#L173)

#### Signature

```python
def visit_Compare(self, node: TypedCompare) -> plt.AST:
    ...
```

### UPLCCompiler().visit_Constant

[Show source in compiler.py:265](https://github.com/ImperatorLang/hebi/blob/master/hebi/compiler.py#L265)

#### Signature

```python
def visit_Constant(self, node: TypedConstant) -> plt.AST:
    ...
```

### UPLCCompiler().visit_Dict

[Show source in compiler.py:552](https://github.com/ImperatorLang/hebi/blob/master/hebi/compiler.py#L552)

#### Signature

```python
def visit_Dict(self, node: TypedDict) -> plt.AST:
    ...
```

### UPLCCompiler().visit_Expr

[Show source in compiler.py:310](https://github.com/ImperatorLang/hebi/blob/master/hebi/compiler.py#L310)

#### Signature

```python
def visit_Expr(self, node: TypedExpr) -> typing.Callable[[plt.AST], plt.AST]:
    ...
```

### UPLCCompiler().visit_FunctionDef

[Show source in compiler.py:342](https://github.com/ImperatorLang/hebi/blob/master/hebi/compiler.py#L342)

#### Signature

```python
def visit_FunctionDef(
    self, node: TypedFunctionDef
) -> typing.Callable[[plt.AST], plt.AST]:
    ...
```

### UPLCCompiler().visit_If

[Show source in compiler.py:361](https://github.com/ImperatorLang/hebi/blob/master/hebi/compiler.py#L361)

#### Signature

```python
def visit_If(self, node: TypedIf) -> typing.Callable[[plt.AST], plt.AST]:
    ...
```

### UPLCCompiler().visit_IfExp

[Show source in compiler.py:568](https://github.com/ImperatorLang/hebi/blob/master/hebi/compiler.py#L568)

#### Signature

```python
def visit_IfExp(self, node: TypedIfExp) -> plt.AST:
    ...
```

### UPLCCompiler().visit_List

[Show source in compiler.py:544](https://github.com/ImperatorLang/hebi/blob/master/hebi/compiler.py#L544)

#### Signature

```python
def visit_List(self, node: TypedList) -> plt.AST:
    ...
```

### UPLCCompiler().visit_ListComp

[Show source in compiler.py:575](https://github.com/ImperatorLang/hebi/blob/master/hebi/compiler.py#L575)

#### Signature

```python
def visit_ListComp(self, node: TypedListComp) -> plt.AST:
    ...
```

### UPLCCompiler().visit_Module

[Show source in compiler.py:185](https://github.com/ImperatorLang/hebi/blob/master/hebi/compiler.py#L185)

#### Signature

```python
def visit_Module(self, node: TypedModule) -> plt.AST:
    ...
```

### UPLCCompiler().visit_Name

[Show source in compiler.py:301](https://github.com/ImperatorLang/hebi/blob/master/hebi/compiler.py#L301)

#### Signature

```python
def visit_Name(self, node: TypedName) -> plt.AST:
    ...
```

### UPLCCompiler().visit_NoneType

[Show source in compiler.py:273](https://github.com/ImperatorLang/hebi/blob/master/hebi/compiler.py#L273)

#### Signature

```python
def visit_NoneType(self, _: typing.Optional[typing.Any]) -> plt.AST:
    ...
```

### UPLCCompiler().visit_Pass

[Show source in compiler.py:372](https://github.com/ImperatorLang/hebi/blob/master/hebi/compiler.py#L372)

#### Signature

```python
def visit_Pass(self, node: TypedPass) -> typing.Callable[[plt.AST], plt.AST]:
    ...
```

### UPLCCompiler().visit_RawPlutoExpr

[Show source in compiler.py:541](https://github.com/ImperatorLang/hebi/blob/master/hebi/compiler.py#L541)

#### Signature

```python
def visit_RawPlutoExpr(self, node: RawPlutoExpr) -> plt.AST:
    ...
```

### UPLCCompiler().visit_Return

[Show source in compiler.py:368](https://github.com/ImperatorLang/hebi/blob/master/hebi/compiler.py#L368)

#### Signature

```python
def visit_Return(self, node: TypedReturn) -> typing.Callable[[plt.AST], plt.AST]:
    ...
```

### UPLCCompiler().visit_Subscript

[Show source in compiler.py:375](https://github.com/ImperatorLang/hebi/blob/master/hebi/compiler.py#L375)

#### Signature

```python
def visit_Subscript(self, node: TypedSubscript) -> plt.AST:
    ...
```

### UPLCCompiler().visit_Tuple

[Show source in compiler.py:513](https://github.com/ImperatorLang/hebi/blob/master/hebi/compiler.py#L513)

#### Signature

```python
def visit_Tuple(self, node: TypedTuple) -> plt.AST:
    ...
```

### UPLCCompiler().visit_UnaryOp

[Show source in compiler.py:164](https://github.com/ImperatorLang/hebi/blob/master/hebi/compiler.py#L164)

#### Signature

```python
def visit_UnaryOp(self, node: TypedUnaryOp) -> plt.AST:
    ...
```

### UPLCCompiler().visit_sequence

[Show source in compiler.py:126](https://github.com/ImperatorLang/hebi/blob/master/hebi/compiler.py#L126)

#### Signature

```python
def visit_sequence(
    self, node_seq: typing.List[typedstmt]
) -> typing.Callable[[plt.AST], plt.AST]:
    ...
```



## compile

[Show source in compiler.py:617](https://github.com/ImperatorLang/hebi/blob/master/hebi/compiler.py#L617)

#### Signature

```python
def compile(prog: AST, force_three_params=False):
    ...
```



## wrap_validator_double_function

[Show source in compiler.py:87](https://github.com/ImperatorLang/hebi/blob/master/hebi/compiler.py#L87)

Wraps the validator function to enable a double function as minting script

pass_through defines how many parameters x would normally take and should be passed through to x

#### Signature

```python
def wrap_validator_double_function(x: plt.AST, pass_through: int = 0):
    ...
```