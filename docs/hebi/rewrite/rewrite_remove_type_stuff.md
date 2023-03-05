# RewriteRemoveTypeStuff

[hebi Index](../../README.md#hebi-index) /
[Hebi](../index.md#hebi) /
[Rewrite](./index.md#rewrite) /
RewriteRemoveTypeStuff

> Auto-generated documentation for [hebi.rewrite.rewrite_remove_type_stuff](https://github.com/ImperatorLang/hebi/blob/master/hebi/rewrite/rewrite_remove_type_stuff.py) module.

- [RewriteRemoveTypeStuff](#rewriteremovetypestuff)
  - [RewriteRemoveTypeStuff](#rewriteremovetypestuff-1)
    - [RewriteRemoveTypeStuff().visit_Assign](#rewriteremovetypestuff()visit_assign)

## RewriteRemoveTypeStuff

[Show source in rewrite_remove_type_stuff.py:11](https://github.com/ImperatorLang/hebi/blob/master/hebi/rewrite/rewrite_remove_type_stuff.py#L11)

#### Signature

```python
class RewriteRemoveTypeStuff(CompilingNodeTransformer):
    ...
```

### RewriteRemoveTypeStuff().visit_Assign

[Show source in rewrite_remove_type_stuff.py:14](https://github.com/ImperatorLang/hebi/blob/master/hebi/rewrite/rewrite_remove_type_stuff.py#L14)

#### Signature

```python
def visit_Assign(self, node: TypedAssign) -> Optional[TypedAssign]:
    ...
```