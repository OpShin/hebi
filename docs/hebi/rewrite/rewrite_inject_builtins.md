# RewriteInjectBuiltins

[hebi Index](../../README.md#hebi-index) /
[Hebi](../index.md#hebi) /
[Rewrite](./index.md#rewrite) /
RewriteInjectBuiltins

> Auto-generated documentation for [hebi.rewrite.rewrite_inject_builtins](https://github.com/ImperatorLang/hebi/blob/master/hebi/rewrite/rewrite_inject_builtins.py) module.

- [RewriteInjectBuiltins](#rewriteinjectbuiltins)
  - [RewriteInjectBuiltins](#rewriteinjectbuiltins-1)
    - [RewriteInjectBuiltins().visit_Module](#rewriteinjectbuiltins()visit_module)

## RewriteInjectBuiltins

[Show source in rewrite_inject_builtins.py:15](https://github.com/ImperatorLang/hebi/blob/master/hebi/rewrite/rewrite_inject_builtins.py#L15)

#### Signature

```python
class RewriteInjectBuiltins(CompilingNodeTransformer):
    ...
```

### RewriteInjectBuiltins().visit_Module

[Show source in rewrite_inject_builtins.py:18](https://github.com/ImperatorLang/hebi/blob/master/hebi/rewrite/rewrite_inject_builtins.py#L18)

#### Signature

```python
def visit_Module(self, node: TypedModule) -> TypedModule:
    ...
```