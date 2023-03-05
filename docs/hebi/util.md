# Util

[hebi Index](../README.md#hebi-index) /
[Hebi](./index.md#hebi) /
Util

> Auto-generated documentation for [hebi.util](https://github.com/ImperatorLang/hebi/blob/master/hebi/util.py) module.

- [Util](#util)
  - [CompilerError](#compilererror)
  - [CompilingNodeTransformer](#compilingnodetransformer)
    - [CompilingNodeTransformer().visit](#compilingnodetransformer()visit)
  - [CompilingNodeVisitor](#compilingnodevisitor)
    - [CompilingNodeVisitor().visit](#compilingnodevisitor()visit)
  - [LenImpl](#lenimpl)
    - [LenImpl().impl_from_args](#lenimpl()impl_from_args)
    - [LenImpl().type_from_args](#lenimpl()type_from_args)
  - [PythonBuiltIn](#pythonbuiltin)
  - [ReversedImpl](#reversedimpl)
    - [ReversedImpl().impl_from_args](#reversedimpl()impl_from_args)
    - [ReversedImpl().type_from_args](#reversedimpl()type_from_args)
  - [data_from_json](#data_from_json)

## CompilerError

[Show source in util.py:507](https://github.com/ImperatorLang/hebi/blob/master/hebi/util.py#L507)

#### Signature

```python
class CompilerError(Exception):
    def __init__(self, orig_err: Exception, node: ast.AST, compilation_step: str):
        ...
```



## CompilingNodeTransformer

[Show source in util.py:514](https://github.com/ImperatorLang/hebi/blob/master/hebi/util.py#L514)

#### Signature

```python
class CompilingNodeTransformer(TypedNodeTransformer):
    ...
```

### CompilingNodeTransformer().visit

[Show source in util.py:517](https://github.com/ImperatorLang/hebi/blob/master/hebi/util.py#L517)

#### Signature

```python
def visit(self, node):
    ...
```



## CompilingNodeVisitor

[Show source in util.py:526](https://github.com/ImperatorLang/hebi/blob/master/hebi/util.py#L526)

#### Signature

```python
class CompilingNodeVisitor(TypedNodeVisitor):
    ...
```

### CompilingNodeVisitor().visit

[Show source in util.py:529](https://github.com/ImperatorLang/hebi/blob/master/hebi/util.py#L529)

#### Signature

```python
def visit(self, node):
    ...
```



## LenImpl

[Show source in util.py:374](https://github.com/ImperatorLang/hebi/blob/master/hebi/util.py#L374)

#### Signature

```python
class LenImpl(PolymorphicFunction):
    ...
```

### LenImpl().impl_from_args

[Show source in util.py:384](https://github.com/ImperatorLang/hebi/blob/master/hebi/util.py#L384)

#### Signature

```python
def impl_from_args(self, args: typing.List[Type]) -> plt.AST:
    ...
```

### LenImpl().type_from_args

[Show source in util.py:375](https://github.com/ImperatorLang/hebi/blob/master/hebi/util.py#L375)

#### Signature

```python
def type_from_args(self, args: typing.List[Type]) -> FunctionType:
    ...
```



## PythonBuiltIn

[Show source in util.py:28](https://github.com/ImperatorLang/hebi/blob/master/hebi/util.py#L28)

#### Attributes

- `chr` - maps an integer to a unicode code point and decodes it
  reference: https://en.wikipedia.org/wiki/UTF-8#Encoding: `plt.Lambda(['_', 'x'], plt.DecodeUtf8(plt.Ite(plt.LessThanInteger(plt.Var('x'), plt.Integer(0)), plt.TraceError('ValueError: chr() arg not in range(0x110000)'), plt.Ite(plt.LessThanInteger(plt.Var('x'), plt.Integer(128)), plt.ConsByteString(plt.Var('x'), plt.ByteString(b'')), plt.Ite(plt.LessThanInteger(plt.Var('x'), plt.Integer(2048)), plt.ConsByteString(plt.AddInteger(plt.Integer(6 << 5), plt.DivideInteger(plt.Var('x'), plt.Integer(1 << 6))), plt.ConsByteString(plt.AddInteger(plt.Integer(2 << 6), plt.ModInteger(plt.Var('x'), plt.Integer(1 << 6))), plt.ByteString(b''))), plt.Ite(plt.LessThanInteger(plt.Var('x'), plt.Integer(65536)), plt.ConsByteString(plt.AddInteger(plt.Integer(14 << 4), plt.DivideInteger(plt.Var('x'), plt.Integer(1 << 12))), plt.ConsByteString(plt.AddInteger(plt.Integer(2 << 6), plt.DivideInteger(plt.ModInteger(plt.Var('x'), plt.Integer(1 << 12)), plt.Integer(1 << 6))), plt.ConsByteString(plt.AddInteger(plt.Integer(2 << 6), plt.ModInteger(plt.Var('x'), plt.Integer(1 << 6))), plt.ByteString(b'')))), plt.Ite(plt.LessThanInteger(plt.Var('x'), plt.Integer(1114112)), plt.ConsByteString(plt.AddInteger(plt.Integer(30 << 3), plt.DivideInteger(plt.Var('x'), plt.Integer(1 << 18))), plt.ConsByteString(plt.AddInteger(plt.Integer(2 << 6), plt.DivideInteger(plt.ModInteger(plt.Var('x'), plt.Integer(1 << 18)), plt.Integer(1 << 12))), plt.ConsByteString(plt.AddInteger(plt.Integer(2 << 6), plt.DivideInteger(plt.ModInteger(plt.Var('x'), plt.Integer(1 << 12)), plt.Integer(1 << 6))), plt.ConsByteString(plt.AddInteger(plt.Integer(2 << 6), plt.ModInteger(plt.Var('x'), plt.Integer(1 << 6))), plt.ByteString(b''))))), plt.TraceError('ValueError: chr() arg not in range(0x110000)'))))))))`

- `pow` - NOTE: only correctly defined for positive y: `PowImpl`


#### Signature

```python
class PythonBuiltIn(Enum):
    ...
```



## ReversedImpl

[Show source in util.py:404](https://github.com/ImperatorLang/hebi/blob/master/hebi/util.py#L404)

#### Signature

```python
class ReversedImpl(PolymorphicFunction):
    ...
```

### ReversedImpl().impl_from_args

[Show source in util.py:415](https://github.com/ImperatorLang/hebi/blob/master/hebi/util.py#L415)

#### Signature

```python
def impl_from_args(self, args: typing.List[Type]) -> plt.AST:
    ...
```

### ReversedImpl().type_from_args

[Show source in util.py:405](https://github.com/ImperatorLang/hebi/blob/master/hebi/util.py#L405)

#### Signature

```python
def type_from_args(self, args: typing.List[Type]) -> FunctionType:
    ...
```



## data_from_json

[Show source in util.py:538](https://github.com/ImperatorLang/hebi/blob/master/hebi/util.py#L538)

#### Signature

```python
def data_from_json(j: typing.Dict[str, typing.Any]) -> uplc.PlutusData:
    ...
```