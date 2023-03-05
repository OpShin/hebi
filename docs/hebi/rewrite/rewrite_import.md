# RewriteImport

[hebi Index](../../README.md#hebi-index) /
[Hebi](../index.md#hebi) /
[Rewrite](./index.md#rewrite) /
RewriteImport

> Auto-generated documentation for [hebi.rewrite.rewrite_import](https://github.com/ImperatorLang/hebi/blob/master/hebi/rewrite/rewrite_import.py) module.

- [RewriteImport](#rewriteimport)
  - [RewriteImport](#rewriteimport-1)
    - [RewriteImport().visit_ImportFrom](#rewriteimport()visit_importfrom)

## RewriteImport

[Show source in rewrite_import.py:13](https://github.com/ImperatorLang/hebi/blob/master/hebi/rewrite/rewrite_import.py#L13)

#### Signature

```python
class RewriteImport(CompilingNodeTransformer):
    ...
```

### RewriteImport().visit_ImportFrom

[Show source in rewrite_import.py:16](https://github.com/ImperatorLang/hebi/blob/master/hebi/rewrite/rewrite_import.py#L16)

#### Signature

```python
def visit_ImportFrom(
    self, node: ImportFrom
) -> typing.Union[ImportFrom, typing.List[AST]]:
    ...
```