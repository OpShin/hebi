# RewriteForbiddenOverwrites

[hebi Index](../../README.md#hebi-index) /
[Hebi](../index.md#hebi) /
[Rewrite](./index.md#rewrite) /
RewriteForbiddenOverwrites

> Auto-generated documentation for [hebi.rewrite.rewrite_forbidden_overwrites](https://github.com/ImperatorLang/hebi/blob/master/hebi/rewrite/rewrite_forbidden_overwrites.py) module.

- [RewriteForbiddenOverwrites](#rewriteforbiddenoverwrites)
  - [ForbiddenOverwriteError](#forbiddenoverwriteerror)
  - [RewriteForbiddenOverwrites](#rewriteforbiddenoverwrites-1)
    - [RewriteForbiddenOverwrites().visit_Name](#rewriteforbiddenoverwrites()visit_name)

## ForbiddenOverwriteError

[Show source in rewrite_forbidden_overwrites.py:20](https://github.com/ImperatorLang/hebi/blob/master/hebi/rewrite/rewrite_forbidden_overwrites.py#L20)

#### Signature

```python
class ForbiddenOverwriteError(ValueError):
    ...
```



## RewriteForbiddenOverwrites

[Show source in rewrite_forbidden_overwrites.py:24](https://github.com/ImperatorLang/hebi/blob/master/hebi/rewrite/rewrite_forbidden_overwrites.py#L24)

#### Signature

```python
class RewriteForbiddenOverwrites(CompilingNodeTransformer):
    ...
```

### RewriteForbiddenOverwrites().visit_Name

[Show source in rewrite_forbidden_overwrites.py:27](https://github.com/ImperatorLang/hebi/blob/master/hebi/rewrite/rewrite_forbidden_overwrites.py#L27)

#### Signature

```python
def visit_Name(self, node: Name) -> Name:
    ...
```