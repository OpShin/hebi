# RewriteImportPlutusData

[hebi Index](../../README.md#hebi-index) /
[Hebi](../index.md#hebi) /
[Rewrite](./index.md#rewrite) /
RewriteImportPlutusData

> Auto-generated documentation for [hebi.rewrite.rewrite_import_plutusdata](https://github.com/ImperatorLang/hebi/blob/master/hebi/rewrite/rewrite_import_plutusdata.py) module.

- [RewriteImportPlutusData](#rewriteimportplutusdata)
  - [RewriteImportPlutusData](#rewriteimportplutusdata-1)
    - [RewriteImportPlutusData().visit_ClassDef](#rewriteimportplutusdata()visit_classdef)
    - [RewriteImportPlutusData().visit_ImportFrom](#rewriteimportplutusdata()visit_importfrom)

## RewriteImportPlutusData

[Show source in rewrite_import_plutusdata.py:11](https://github.com/ImperatorLang/hebi/blob/master/hebi/rewrite/rewrite_import_plutusdata.py#L11)

#### Signature

```python
class RewriteImportPlutusData(CompilingNodeTransformer):
    ...
```

### RewriteImportPlutusData().visit_ClassDef

[Show source in rewrite_import_plutusdata.py:37](https://github.com/ImperatorLang/hebi/blob/master/hebi/rewrite/rewrite_import_plutusdata.py#L37)

#### Signature

```python
def visit_ClassDef(self, node: ClassDef) -> ClassDef:
    ...
```

### RewriteImportPlutusData().visit_ImportFrom

[Show source in rewrite_import_plutusdata.py:16](https://github.com/ImperatorLang/hebi/blob/master/hebi/rewrite/rewrite_import_plutusdata.py#L16)

#### Signature

```python
def visit_ImportFrom(self, node: ImportFrom) -> Optional[ImportFrom]:
    ...
```