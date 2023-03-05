from ast import *
from copy import copy
from collections import defaultdict

from ..util import CompilingNodeVisitor, CompilingNodeTransformer
from ..type_inference import INITIAL_SCOPE

"""
Check no double assignments occur in the current scope
"""


class RewriteDuplicateAssignment(CompilingNodeTransformer):
    # we are a transformer but actually don't change anything
    step = (
        "Checking that variables do not override other variables in the current scope"
    )

    # names that are possibly available to the current node
    avail_names = [list(INITIAL_SCOPE.keys())]

    def avail(self, name: str) -> bool:
        name = name
        for scope in reversed(self.avail_names):
            if name in scope:
                return True
        return False

    def in_current_scope(self, name: str) -> bool:
        return name in self.avail_names[-1]

    def enter_scope(self):
        self.avail_names.append([])

    def exit_scope(self):
        self.avail_names.pop()

    def set_avail(self, name: str):
        self.avail_names[-1].append(name)

    def visit_Module(self, node: Module) -> Module:
        self.enter_scope()
        # collect all variable names
        node.body = [self.visit(s) for s in node.body]
        self.exit_scope()
        return node

    def visit_If(self, node: If):
        node_cp = copy(node)
        node_cp.test = self.visit(node.test)
        self.enter_scope()
        # all the names from the previous scope STILL cause a conflict
        self.avail_names[-1].extend(self.avail_names[-2])
        node_cp.body = [self.visit(s) for s in node.body]
        body_scope_cp = self.avail_names[-1].copy()
        self.exit_scope()
        self.enter_scope()
        # all the names from the previous scope STILL cause a conflict, but not from the body
        self.avail_names[-1].extend(self.avail_names[-2])
        node_cp.orelse = [self.visit(s) for s in node.orelse]
        else_scope_cp = self.avail_names[-1].copy()
        self.exit_scope()
        # after the if/else, all potentially assigned variables in each branch are potentially available
        self.avail_names[-1].extend(set(body_scope_cp).union(else_scope_cp))
        return node_cp

    def visit_Assign(self, node: Assign):
        for t in node.targets:
            assert isinstance(t, Name), "Can not assign to non-names"
            assert not self.in_current_scope(
                t.id
            ), f"Can not assign a value to variable {t.id}, already assigned in this scope"
            self.set_avail(t.id)
        return self.generic_visit(node)

    def visit_AnnAssign(self, node: AnnAssign):
        assert isinstance(node.target, Name), "Can not assign to non-names"
        assert not self.in_current_scope(
            node.target.id
        ), f"Can not assign a value to variable {node.target.id}, already assigned in this scope"
        self.set_avail(node.target.id)
        return self.generic_visit(node)

    def visit_ClassDef(self, node: ClassDef):
        assert not self.in_current_scope(
            node.name
        ), f"Can not define class {node.name} which was already defined in the current scope"
        self.set_avail(node.name)
        return node

    def visit_FunctionDef(self, node: FunctionDef):
        assert not self.in_current_scope(
            node.name
        ), f"Can not define function {node.name} which was already defined in the current scope"
        self.set_avail(node.name)
        self.enter_scope()
        # variable names are available here
        for a in node.args.args:
            self.set_avail(a.arg)
        node.body = [self.visit(s) for s in node.body]
        self.exit_scope()
        return node
