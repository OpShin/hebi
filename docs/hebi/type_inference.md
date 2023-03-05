# Type Inference

[hebi Index](../README.md#hebi-index) /
[Hebi](./index.md#hebi) /
Type Inference

> Auto-generated documentation for [hebi.type_inference](https://github.com/ImperatorLang/hebi/blob/master/hebi/type_inference.py) module.

- [Type Inference](#type-inference)
  - [AggressiveTypeInferencer](#aggressivetypeinferencer)
    - [AggressiveTypeInferencer().enter_scope](#aggressivetypeinferencer()enter_scope)
    - [AggressiveTypeInferencer().exit_scope](#aggressivetypeinferencer()exit_scope)
    - [AggressiveTypeInferencer().generic_visit](#aggressivetypeinferencer()generic_visit)
    - [AggressiveTypeInferencer().set_variable_type](#aggressivetypeinferencer()set_variable_type)
    - [AggressiveTypeInferencer().type_from_annotation](#aggressivetypeinferencer()type_from_annotation)
    - [AggressiveTypeInferencer().variable_type](#aggressivetypeinferencer()variable_type)
    - [AggressiveTypeInferencer().visit_AnnAssign](#aggressivetypeinferencer()visit_annassign)
    - [AggressiveTypeInferencer().visit_Assert](#aggressivetypeinferencer()visit_assert)
    - [AggressiveTypeInferencer().visit_Assign](#aggressivetypeinferencer()visit_assign)
    - [AggressiveTypeInferencer().visit_Attribute](#aggressivetypeinferencer()visit_attribute)
    - [AggressiveTypeInferencer().visit_BinOp](#aggressivetypeinferencer()visit_binop)
    - [AggressiveTypeInferencer().visit_BoolOp](#aggressivetypeinferencer()visit_boolop)
    - [AggressiveTypeInferencer().visit_Call](#aggressivetypeinferencer()visit_call)
    - [AggressiveTypeInferencer().visit_ClassDef](#aggressivetypeinferencer()visit_classdef)
    - [AggressiveTypeInferencer().visit_Compare](#aggressivetypeinferencer()visit_compare)
    - [AggressiveTypeInferencer().visit_Constant](#aggressivetypeinferencer()visit_constant)
    - [AggressiveTypeInferencer().visit_Dict](#aggressivetypeinferencer()visit_dict)
    - [AggressiveTypeInferencer().visit_Expr](#aggressivetypeinferencer()visit_expr)
    - [AggressiveTypeInferencer().visit_For](#aggressivetypeinferencer()visit_for)
    - [AggressiveTypeInferencer().visit_FunctionDef](#aggressivetypeinferencer()visit_functiondef)
    - [AggressiveTypeInferencer().visit_If](#aggressivetypeinferencer()visit_if)
    - [AggressiveTypeInferencer().visit_IfExp](#aggressivetypeinferencer()visit_ifexp)
    - [AggressiveTypeInferencer().visit_List](#aggressivetypeinferencer()visit_list)
    - [AggressiveTypeInferencer().visit_ListComp](#aggressivetypeinferencer()visit_listcomp)
    - [AggressiveTypeInferencer().visit_Module](#aggressivetypeinferencer()visit_module)
    - [AggressiveTypeInferencer().visit_Name](#aggressivetypeinferencer()visit_name)
    - [AggressiveTypeInferencer().visit_Pass](#aggressivetypeinferencer()visit_pass)
    - [AggressiveTypeInferencer().visit_RawPlutoExpr](#aggressivetypeinferencer()visit_rawplutoexpr)
    - [AggressiveTypeInferencer().visit_Return](#aggressivetypeinferencer()visit_return)
    - [AggressiveTypeInferencer().visit_Subscript](#aggressivetypeinferencer()visit_subscript)
    - [AggressiveTypeInferencer().visit_Tuple](#aggressivetypeinferencer()visit_tuple)
    - [AggressiveTypeInferencer().visit_UnaryOp](#aggressivetypeinferencer()visit_unaryop)
    - [AggressiveTypeInferencer().visit_While](#aggressivetypeinferencer()visit_while)
    - [AggressiveTypeInferencer().visit_arg](#aggressivetypeinferencer()visit_arg)
    - [AggressiveTypeInferencer().visit_arguments](#aggressivetypeinferencer()visit_arguments)
    - [AggressiveTypeInferencer().visit_comprehension](#aggressivetypeinferencer()visit_comprehension)
  - [RecordReader](#recordreader)
    - [RecordReader.extract](#recordreaderextract)
    - [RecordReader().generic_visit](#recordreader()generic_visit)
    - [RecordReader().visit_AnnAssign](#recordreader()visit_annassign)
    - [RecordReader().visit_Assign](#recordreader()visit_assign)
    - [RecordReader().visit_ClassDef](#recordreader()visit_classdef)
    - [RecordReader().visit_Expr](#recordreader()visit_expr)
    - [RecordReader().visit_Pass](#recordreader()visit_pass)
  - [ReturnExtractor](#returnextractor)
    - [ReturnExtractor().visit_Return](#returnextractor()visit_return)
  - [typed_ast](#typed_ast)

## AggressiveTypeInferencer

[Show source in type_inference.py:55](https://github.com/ImperatorLang/hebi/blob/master/hebi/type_inference.py#L55)

#### Attributes

- `scopes` - A stack of dictionaries for storing scoped knowledge of variable types: `[INITIAL_SCOPE]`


#### Signature

```python
class AggressiveTypeInferencer(CompilingNodeTransformer):
    ...
```

### AggressiveTypeInferencer().enter_scope

[Show source in type_inference.py:69](https://github.com/ImperatorLang/hebi/blob/master/hebi/type_inference.py#L69)

#### Signature

```python
def enter_scope(self):
    ...
```

### AggressiveTypeInferencer().exit_scope

[Show source in type_inference.py:72](https://github.com/ImperatorLang/hebi/blob/master/hebi/type_inference.py#L72)

#### Signature

```python
def exit_scope(self):
    ...
```

### AggressiveTypeInferencer().generic_visit

[Show source in type_inference.py:624](https://github.com/ImperatorLang/hebi/blob/master/hebi/type_inference.py#L624)

#### Signature

```python
def generic_visit(self, node: AST) -> TypedAST:
    ...
```

### AggressiveTypeInferencer().set_variable_type

[Show source in type_inference.py:75](https://github.com/ImperatorLang/hebi/blob/master/hebi/type_inference.py#L75)

#### Signature

```python
def set_variable_type(self, name: str, typ: Type, force=False):
    ...
```

### AggressiveTypeInferencer().type_from_annotation

[Show source in type_inference.py:82](https://github.com/ImperatorLang/hebi/blob/master/hebi/type_inference.py#L82)

#### Signature

```python
def type_from_annotation(self, ann: expr):
    ...
```

### AggressiveTypeInferencer().variable_type

[Show source in type_inference.py:62](https://github.com/ImperatorLang/hebi/blob/master/hebi/type_inference.py#L62)

#### Signature

```python
def variable_type(self, name: str) -> Type:
    ...
```

### AggressiveTypeInferencer().visit_AnnAssign

[Show source in type_inference.py:216](https://github.com/ImperatorLang/hebi/blob/master/hebi/type_inference.py#L216)

#### Signature

```python
def visit_AnnAssign(self, node: AnnAssign) -> TypedAnnAssign:
    ...
```

### AggressiveTypeInferencer().visit_Assert

[Show source in type_inference.py:551](https://github.com/ImperatorLang/hebi/blob/master/hebi/type_inference.py#L551)

#### Signature

```python
def visit_Assert(self, node: Assert) -> TypedAssert:
    ...
```

### AggressiveTypeInferencer().visit_Assign

[Show source in type_inference.py:204](https://github.com/ImperatorLang/hebi/blob/master/hebi/type_inference.py#L204)

#### Signature

```python
def visit_Assign(self, node: Assign) -> TypedAssign:
    ...
```

### AggressiveTypeInferencer().visit_Attribute

[Show source in type_inference.py:543](https://github.com/ImperatorLang/hebi/blob/master/hebi/type_inference.py#L543)

#### Signature

```python
def visit_Attribute(self, node: Attribute) -> TypedAttribute:
    ...
```

### AggressiveTypeInferencer().visit_BinOp

[Show source in type_inference.py:394](https://github.com/ImperatorLang/hebi/blob/master/hebi/type_inference.py#L394)

#### Signature

```python
def visit_BinOp(self, node: BinOp) -> TypedBinOp:
    ...
```

### AggressiveTypeInferencer().visit_BoolOp

[Show source in type_inference.py:405](https://github.com/ImperatorLang/hebi/blob/master/hebi/type_inference.py#L405)

#### Signature

```python
def visit_BoolOp(self, node: BoolOp) -> TypedBoolOp:
    ...
```

### AggressiveTypeInferencer().visit_Call

[Show source in type_inference.py:500](https://github.com/ImperatorLang/hebi/blob/master/hebi/type_inference.py#L500)

#### Signature

```python
def visit_Call(self, node: Call) -> TypedCall:
    ...
```

### AggressiveTypeInferencer().visit_ClassDef

[Show source in type_inference.py:154](https://github.com/ImperatorLang/hebi/blob/master/hebi/type_inference.py#L154)

#### Signature

```python
def visit_ClassDef(self, node: ClassDef) -> TypedClassDef:
    ...
```

### AggressiveTypeInferencer().visit_Compare

[Show source in type_inference.py:328](https://github.com/ImperatorLang/hebi/blob/master/hebi/type_inference.py#L328)

#### Signature

```python
def visit_Compare(self, node: Compare) -> TypedCompare:
    ...
```

### AggressiveTypeInferencer().visit_Constant

[Show source in type_inference.py:162](https://github.com/ImperatorLang/hebi/blob/master/hebi/type_inference.py#L162)

#### Signature

```python
def visit_Constant(self, node: Constant) -> TypedConstant:
    ...
```

### AggressiveTypeInferencer().visit_Dict

[Show source in type_inference.py:191](https://github.com/ImperatorLang/hebi/blob/master/hebi/type_inference.py#L191)

#### Signature

```python
def visit_Dict(self, node: Dict) -> TypedDict:
    ...
```

### AggressiveTypeInferencer().visit_Expr

[Show source in type_inference.py:389](https://github.com/ImperatorLang/hebi/blob/master/hebi/type_inference.py#L389)

#### Signature

```python
def visit_Expr(self, node: Expr) -> TypedExpr:
    ...
```

### AggressiveTypeInferencer().visit_For

[Show source in type_inference.py:292](https://github.com/ImperatorLang/hebi/blob/master/hebi/type_inference.py#L292)

#### Signature

```python
def visit_For(self, node: For) -> TypedFor:
    ...
```

### AggressiveTypeInferencer().visit_FunctionDef

[Show source in type_inference.py:351](https://github.com/ImperatorLang/hebi/blob/master/hebi/type_inference.py#L351)

#### Signature

```python
def visit_FunctionDef(self, node: FunctionDef) -> TypedFunctionDef:
    ...
```

### AggressiveTypeInferencer().visit_If

[Show source in type_inference.py:232](https://github.com/ImperatorLang/hebi/blob/master/hebi/type_inference.py#L232)

#### Signature

```python
def visit_If(self, node: If) -> TypedIf:
    ...
```

### AggressiveTypeInferencer().visit_IfExp

[Show source in type_inference.py:568](https://github.com/ImperatorLang/hebi/blob/master/hebi/type_inference.py#L568)

#### Signature

```python
def visit_IfExp(self, node: IfExp) -> TypedIfExp:
    ...
```

### AggressiveTypeInferencer().visit_List

[Show source in type_inference.py:181](https://github.com/ImperatorLang/hebi/blob/master/hebi/type_inference.py#L181)

#### Signature

```python
def visit_List(self, node: List) -> TypedList:
    ...
```

### AggressiveTypeInferencer().visit_ListComp

[Show source in type_inference.py:612](https://github.com/ImperatorLang/hebi/blob/master/hebi/type_inference.py#L612)

#### Signature

```python
def visit_ListComp(self, node: ListComp) -> TypedListComp:
    ...
```

### AggressiveTypeInferencer().visit_Module

[Show source in type_inference.py:382](https://github.com/ImperatorLang/hebi/blob/master/hebi/type_inference.py#L382)

#### Signature

```python
def visit_Module(self, node: Module) -> TypedModule:
    ...
```

### AggressiveTypeInferencer().visit_Name

[Show source in type_inference.py:322](https://github.com/ImperatorLang/hebi/blob/master/hebi/type_inference.py#L322)

#### Signature

```python
def visit_Name(self, node: Name) -> TypedName:
    ...
```

### AggressiveTypeInferencer().visit_Pass

[Show source in type_inference.py:533](https://github.com/ImperatorLang/hebi/blob/master/hebi/type_inference.py#L533)

#### Signature

```python
def visit_Pass(self, node: Pass) -> TypedPass:
    ...
```

### AggressiveTypeInferencer().visit_RawPlutoExpr

[Show source in type_inference.py:564](https://github.com/ImperatorLang/hebi/blob/master/hebi/type_inference.py#L564)

#### Signature

```python
def visit_RawPlutoExpr(self, node: RawPlutoExpr) -> RawPlutoExpr:
    ...
```

### AggressiveTypeInferencer().visit_Return

[Show source in type_inference.py:537](https://github.com/ImperatorLang/hebi/blob/master/hebi/type_inference.py#L537)

#### Signature

```python
def visit_Return(self, node: Return) -> TypedReturn:
    ...
```

### AggressiveTypeInferencer().visit_Subscript

[Show source in type_inference.py:420](https://github.com/ImperatorLang/hebi/blob/master/hebi/type_inference.py#L420)

#### Signature

```python
def visit_Subscript(self, node: Subscript) -> TypedSubscript:
    ...
```

### AggressiveTypeInferencer().visit_Tuple

[Show source in type_inference.py:175](https://github.com/ImperatorLang/hebi/blob/master/hebi/type_inference.py#L175)

#### Signature

```python
def visit_Tuple(self, node: Tuple) -> TypedTuple:
    ...
```

### AggressiveTypeInferencer().visit_UnaryOp

[Show source in type_inference.py:414](https://github.com/ImperatorLang/hebi/blob/master/hebi/type_inference.py#L414)

#### Signature

```python
def visit_UnaryOp(self, node: UnaryOp) -> TypedUnaryOp:
    ...
```

### AggressiveTypeInferencer().visit_While

[Show source in type_inference.py:282](https://github.com/ImperatorLang/hebi/blob/master/hebi/type_inference.py#L282)

#### Signature

```python
def visit_While(self, node: While) -> TypedWhile:
    ...
```

### AggressiveTypeInferencer().visit_arg

[Show source in type_inference.py:336](https://github.com/ImperatorLang/hebi/blob/master/hebi/type_inference.py#L336)

#### Signature

```python
def visit_arg(self, node: arg) -> typedarg:
    ...
```

### AggressiveTypeInferencer().visit_arguments

[Show source in type_inference.py:342](https://github.com/ImperatorLang/hebi/blob/master/hebi/type_inference.py#L342)

#### Signature

```python
def visit_arguments(self, node: arguments) -> typedarguments:
    ...
```

### AggressiveTypeInferencer().visit_comprehension

[Show source in type_inference.py:584](https://github.com/ImperatorLang/hebi/blob/master/hebi/type_inference.py#L584)

#### Signature

```python
def visit_comprehension(self, g: comprehension) -> typedcomprehension:
    ...
```



## RecordReader

[Show source in type_inference.py:630](https://github.com/ImperatorLang/hebi/blob/master/hebi/type_inference.py#L630)

#### Signature

```python
class RecordReader(NodeVisitor):
    def __init__(self, type_inferencer: AggressiveTypeInferencer):
        ...
```

#### See also

- [AggressiveTypeInferencer](#aggressivetypeinferencer)

### RecordReader.extract

[Show source in type_inference.py:641](https://github.com/ImperatorLang/hebi/blob/master/hebi/type_inference.py#L641)

#### Signature

```python
@classmethod
def extract(cls, c: ClassDef, type_inferencer: AggressiveTypeInferencer) -> Record:
    ...
```

#### See also

- [AggressiveTypeInferencer](#aggressivetypeinferencer)

### RecordReader().generic_visit

[Show source in type_inference.py:704](https://github.com/ImperatorLang/hebi/blob/master/hebi/type_inference.py#L704)

#### Signature

```python
def generic_visit(self, node: AST) -> None:
    ...
```

### RecordReader().visit_AnnAssign

[Show source in type_inference.py:647](https://github.com/ImperatorLang/hebi/blob/master/hebi/type_inference.py#L647)

#### Signature

```python
def visit_AnnAssign(self, node: AnnAssign) -> None:
    ...
```

### RecordReader().visit_Assign

[Show source in type_inference.py:683](https://github.com/ImperatorLang/hebi/blob/master/hebi/type_inference.py#L683)

#### Signature

```python
def visit_Assign(self, node: Assign) -> None:
    ...
```

### RecordReader().visit_ClassDef

[Show source in type_inference.py:675](https://github.com/ImperatorLang/hebi/blob/master/hebi/type_inference.py#L675)

#### Signature

```python
def visit_ClassDef(self, node: ClassDef) -> None:
    ...
```

### RecordReader().visit_Expr

[Show source in type_inference.py:698](https://github.com/ImperatorLang/hebi/blob/master/hebi/type_inference.py#L698)

#### Signature

```python
def visit_Expr(self, node: Expr) -> None:
    ...
```

### RecordReader().visit_Pass

[Show source in type_inference.py:680](https://github.com/ImperatorLang/hebi/blob/master/hebi/type_inference.py#L680)

#### Signature

```python
def visit_Pass(self, node: Pass) -> None:
    ...
```



## ReturnExtractor

[Show source in type_inference.py:45](https://github.com/ImperatorLang/hebi/blob/master/hebi/type_inference.py#L45)

Utility to find all Return statements in an AST subtree

#### Signature

```python
class ReturnExtractor(NodeVisitor):
    def __init__(self):
        ...
```

### ReturnExtractor().visit_Return

[Show source in type_inference.py:51](https://github.com/ImperatorLang/hebi/blob/master/hebi/type_inference.py#L51)

#### Signature

```python
def visit_Return(self, node: Return) -> None:
    ...
```



## typed_ast

[Show source in type_inference.py:708](https://github.com/ImperatorLang/hebi/blob/master/hebi/type_inference.py#L708)

#### Signature

```python
def typed_ast(ast: AST):
    ...
```