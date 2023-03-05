# RewriteTupleAssign

[hebi Index](../../README.md#hebi-index) /
[Hebi](../index.md#hebi) /
[Rewrite](./index.md#rewrite) /
RewriteTupleAssign

> Auto-generated documentation for [hebi.rewrite.rewrite_tuple_assign](https://github.com/ImperatorLang/hebi/blob/master/hebi/rewrite/rewrite_tuple_assign.py) module.

- [RewriteTupleAssign](#rewritetupleassign)
  - [RewriteTupleAssign](#rewritetupleassign-1)
    - [RewriteTupleAssign().visit_Assign](#rewritetupleassign()visit_assign)

## RewriteTupleAssign

[Show source in rewrite_tuple_assign.py:11](https://github.com/ImperatorLang/hebi/blob/master/hebi/rewrite/rewrite_tuple_assign.py#L11)

#### Signature

```python
class RewriteTupleAssign(CompilingNodeTransformer):
    ...
```

### RewriteTupleAssign().visit_Assign

[Show source in rewrite_tuple_assign.py:16](https://github.com/ImperatorLang/hebi/blob/master/hebi/rewrite/rewrite_tuple_assign.py#L16)

#### Signature

```python
def visit_Assign(self, node: Assign) -> typing.List[stmt]:
    ...
```