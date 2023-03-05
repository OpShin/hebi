# Rewrite Inject Builtin Constr

[hebi Index](../../README.md#hebi-index) /
[Hebi](../index.md#hebi) /
[Rewrite](./index.md#rewrite) /
Rewrite Inject Builtin Constr

> Auto-generated documentation for [hebi.rewrite.rewrite_inject_builtin_constr](https://github.com/ImperatorLang/hebi/blob/master/hebi/rewrite/rewrite_inject_builtin_constr.py) module.

- [Rewrite Inject Builtin Constr](#rewrite-inject-builtin-constr)
  - [RewriteInjectBuiltinsConstr](#rewriteinjectbuiltinsconstr)
    - [RewriteInjectBuiltinsConstr().visit_Module](#rewriteinjectbuiltinsconstr()visit_module)

## RewriteInjectBuiltinsConstr

[Show source in rewrite_inject_builtin_constr.py:13](https://github.com/ImperatorLang/hebi/blob/master/hebi/rewrite/rewrite_inject_builtin_constr.py#L13)

#### Signature

```python
class RewriteInjectBuiltinsConstr(CompilingNodeTransformer):
    ...
```

### RewriteInjectBuiltinsConstr().visit_Module

[Show source in rewrite_inject_builtin_constr.py:16](https://github.com/ImperatorLang/hebi/blob/master/hebi/rewrite/rewrite_inject_builtin_constr.py#L16)

#### Signature

```python
def visit_Module(self, node: TypedModule) -> TypedModule:
    ...
```