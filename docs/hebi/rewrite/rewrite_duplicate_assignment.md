# RewriteDuplicateAssignment

[hebi Index](../../README.md#hebi-index) /
[Hebi](../index.md#hebi) /
[Rewrite](./index.md#rewrite) /
RewriteDuplicateAssignment

> Auto-generated documentation for [hebi.rewrite.rewrite_duplicate_assignment](https://github.com/ImperatorLang/hebi/blob/master/hebi/rewrite/rewrite_duplicate_assignment.py) module.

- [RewriteDuplicateAssignment](#rewriteduplicateassignment)
  - [RewriteDuplicateAssignment](#rewriteduplicateassignment-1)
    - [RewriteDuplicateAssignment().avail](#rewriteduplicateassignment()avail)
    - [RewriteDuplicateAssignment().enter_scope](#rewriteduplicateassignment()enter_scope)
    - [RewriteDuplicateAssignment().exit_scope](#rewriteduplicateassignment()exit_scope)
    - [RewriteDuplicateAssignment().in_current_scope](#rewriteduplicateassignment()in_current_scope)
    - [RewriteDuplicateAssignment().set_avail](#rewriteduplicateassignment()set_avail)
    - [RewriteDuplicateAssignment().visit_AnnAssign](#rewriteduplicateassignment()visit_annassign)
    - [RewriteDuplicateAssignment().visit_Assign](#rewriteduplicateassignment()visit_assign)
    - [RewriteDuplicateAssignment().visit_ClassDef](#rewriteduplicateassignment()visit_classdef)
    - [RewriteDuplicateAssignment().visit_FunctionDef](#rewriteduplicateassignment()visit_functiondef)
    - [RewriteDuplicateAssignment().visit_If](#rewriteduplicateassignment()visit_if)
    - [RewriteDuplicateAssignment().visit_Module](#rewriteduplicateassignment()visit_module)

## RewriteDuplicateAssignment

[Show source in rewrite_duplicate_assignment.py:13](https://github.com/ImperatorLang/hebi/blob/master/hebi/rewrite/rewrite_duplicate_assignment.py#L13)

#### Attributes

- `step` - we are a transformer but actually don't change anything: `'Checking that variables do not override other variables in the current scope'`

- `avail_names` - names that are possibly available to the current node: `[list(INITIAL_SCOPE.keys())]`


#### Signature

```python
class RewriteDuplicateAssignment(CompilingNodeTransformer):
    ...
```

### RewriteDuplicateAssignment().avail

[Show source in rewrite_duplicate_assignment.py:22](https://github.com/ImperatorLang/hebi/blob/master/hebi/rewrite/rewrite_duplicate_assignment.py#L22)

#### Signature

```python
def avail(self, name: str) -> bool:
    ...
```

### RewriteDuplicateAssignment().enter_scope

[Show source in rewrite_duplicate_assignment.py:32](https://github.com/ImperatorLang/hebi/blob/master/hebi/rewrite/rewrite_duplicate_assignment.py#L32)

#### Signature

```python
def enter_scope(self):
    ...
```

### RewriteDuplicateAssignment().exit_scope

[Show source in rewrite_duplicate_assignment.py:35](https://github.com/ImperatorLang/hebi/blob/master/hebi/rewrite/rewrite_duplicate_assignment.py#L35)

#### Signature

```python
def exit_scope(self):
    ...
```

### RewriteDuplicateAssignment().in_current_scope

[Show source in rewrite_duplicate_assignment.py:29](https://github.com/ImperatorLang/hebi/blob/master/hebi/rewrite/rewrite_duplicate_assignment.py#L29)

#### Signature

```python
def in_current_scope(self, name: str) -> bool:
    ...
```

### RewriteDuplicateAssignment().set_avail

[Show source in rewrite_duplicate_assignment.py:38](https://github.com/ImperatorLang/hebi/blob/master/hebi/rewrite/rewrite_duplicate_assignment.py#L38)

#### Signature

```python
def set_avail(self, name: str):
    ...
```

### RewriteDuplicateAssignment().visit_AnnAssign

[Show source in rewrite_duplicate_assignment.py:76](https://github.com/ImperatorLang/hebi/blob/master/hebi/rewrite/rewrite_duplicate_assignment.py#L76)

#### Signature

```python
def visit_AnnAssign(self, node: AnnAssign):
    ...
```

### RewriteDuplicateAssignment().visit_Assign

[Show source in rewrite_duplicate_assignment.py:67](https://github.com/ImperatorLang/hebi/blob/master/hebi/rewrite/rewrite_duplicate_assignment.py#L67)

#### Signature

```python
def visit_Assign(self, node: Assign):
    ...
```

### RewriteDuplicateAssignment().visit_ClassDef

[Show source in rewrite_duplicate_assignment.py:84](https://github.com/ImperatorLang/hebi/blob/master/hebi/rewrite/rewrite_duplicate_assignment.py#L84)

#### Signature

```python
def visit_ClassDef(self, node: ClassDef):
    ...
```

### RewriteDuplicateAssignment().visit_FunctionDef

[Show source in rewrite_duplicate_assignment.py:91](https://github.com/ImperatorLang/hebi/blob/master/hebi/rewrite/rewrite_duplicate_assignment.py#L91)

#### Signature

```python
def visit_FunctionDef(self, node: FunctionDef):
    ...
```

### RewriteDuplicateAssignment().visit_If

[Show source in rewrite_duplicate_assignment.py:48](https://github.com/ImperatorLang/hebi/blob/master/hebi/rewrite/rewrite_duplicate_assignment.py#L48)

#### Signature

```python
def visit_If(self, node: If):
    ...
```

### RewriteDuplicateAssignment().visit_Module

[Show source in rewrite_duplicate_assignment.py:41](https://github.com/ImperatorLang/hebi/blob/master/hebi/rewrite/rewrite_duplicate_assignment.py#L41)

#### Signature

```python
def visit_Module(self, node: Module) -> Module:
    ...
```