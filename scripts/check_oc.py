#!/usr/bin/env python3
"""Check mechanically-verifiable Object Calisthenics rules. Warn-only."""

from __future__ import annotations

import ast
import sys
from pathlib import Path


class _OCVisitor(ast.NodeVisitor):
    """AST visitor that collects OC violations per file."""

    def __init__(self) -> None:
        self.violations: list[str] = []

    def _line_ref(self, node: ast.stmt) -> str:
        """Return 'L{line}' for a node."""
        return f"L{node.lineno}"

    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        """Check class length (OC-7)."""
        code_lines = set()
        for child in ast.walk(node):
            if child is node:
                continue
            if isinstance(child, ast.stmt):
                code_lines.add(child.lineno)
        if len(code_lines) > 50:
            self.violations.append(
                f"{node.name} {self._line_ref(node)}: class >50 lines "
                f"({len(code_lines)} code lines)"
            )
        self.generic_visit(node)

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        """Check function-level OC rules."""
        self._check_func(node)
        self.generic_visit(node)

    def _check_func(self, node: ast.FunctionDef | ast.AsyncFunctionDef) -> None:
        """Shared OC checks for sync and async functions."""
        self._check_function_length(node)
        self._check_nesting(node)
        self._check_else_after_return(node)
        self._check_getter_setter(node)

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
        """Check async function-level OC rules (same as sync)."""
        self._check_func(node)
        self.generic_visit(node)

    def _check_function_length(
        self, node: ast.FunctionDef | ast.AsyncFunctionDef
    ) -> None:
        """OC-7: function body <=20 code lines (excluding docstring)."""
        doc_end = 0
        if (
            node.body
            and isinstance(node.body[0], ast.Expr)
            and isinstance(node.body[0].value, ast.Constant)
            and isinstance(node.body[0].value.value, str)
        ):
            doc_end = node.body[0].end_lineno or node.body[0].lineno

        code_lines = {
            child.lineno
            for child in ast.walk(node)
            if isinstance(child, ast.stmt)
            and child.lineno > doc_end
            and child is not node
        }
        if len(code_lines) > 20:
            self.violations.append(
                f"{node.name} {self._line_ref(node)}: function >20 lines "
                f"({len(code_lines)} code lines)"
            )

    def _check_nesting(self, node: ast.FunctionDef | ast.AsyncFunctionDef) -> None:
        """OC-1: nesting depth <=2."""
        max_depth = 0
        stack: list[tuple[ast.AST, int]] = [(node, 0)]
        while stack:
            current, depth = stack.pop()
            if isinstance(current, (ast.For, ast.While, ast.If, ast.With, ast.Try)):
                depth += 1
                max_depth = max(max_depth, depth)
            for child in ast.iter_child_nodes(current):
                stack.append((child, depth))
        if max_depth > 2:
            self.violations.append(
                f"{node.name} {self._line_ref(node)}: nesting depth {max_depth} >2"
            )

    def _check_else_after_return(
        self, node: ast.FunctionDef | ast.AsyncFunctionDef
    ) -> None:
        """OC-2: no else after return."""
        for child in ast.walk(node):
            if (
                isinstance(child, ast.If)
                and self._ends_with_return(child.body)
                and child.orelse
            ):
                self.violations.append(
                    f"{node.name} {self._line_ref(child)}: else after return"
                )

    def _ends_with_return(self, body: list[ast.stmt]) -> bool:
        """True if the last statement in body is a return or raise."""
        if not body:
            return False
        last = body[-1]
        return isinstance(last, (ast.Return, ast.Raise))

    def _check_getter_setter(
        self, node: ast.FunctionDef | ast.AsyncFunctionDef
    ) -> None:
        """OC-9: no get_ / set_ method names."""
        if node.name.startswith(("get_", "set_")):
            self.violations.append(
                f"{node.name} {self._line_ref(node)}: getter/setter name"
            )


def _is_dataclass_like(text: str, class_node: ast.ClassDef) -> bool:
    """Heuristic: class has @dataclass, @dataclass(), @pydantic decorator."""
    for dec in class_node.decorator_list:
        name = ""
        if isinstance(dec, ast.Name):
            name = dec.id
        elif isinstance(dec, ast.Call) and isinstance(dec.func, ast.Name):
            name = dec.func.id
        if name in {"dataclass", "pydantic"}:
            return True
    return "@dataclass" in text or "BaseModel" in text


def _scan_forbidden(text: str, rel_path: Path) -> list[str]:
    """Scan file text for noqa and type: ignore lines."""
    forbidden: list[str] = []
    for i, line in enumerate(text.splitlines(), 1):
        if "noqa" in line:
            forbidden.append(f"{rel_path} L{i}: noqa")
        if "type: ignore" in line:
            forbidden.append(f"{rel_path} L{i}: type: ignore")
    return forbidden


def _check_file(f: Path, project_root: Path) -> tuple[list[str], list[str]]:
    """Run OC checks on a single file; return (violations, forbidden)."""
    text = f.read_text()
    rel = f.relative_to(project_root)
    forbidden = _scan_forbidden(text, rel)

    try:
        tree = ast.parse(text, filename=str(f))
    except SyntaxError:
        return [], forbidden

    violations: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef) and _is_dataclass_like(text, node):
            continue
        if isinstance(node, ast.FunctionDef):
            visitor = _OCVisitor()
            visitor.visit(node)
            for v in visitor.violations:
                violations.append(f"{rel} {v}")

    return violations, forbidden


def check_oc(project_root: Path, package: str = "app") -> tuple[list[str], list[str]]:
    """Run OC checks on the package; return (violations, forbidden)."""
    pkg_dir = project_root / package
    all_violations: list[str] = []
    all_forbidden: list[str] = []

    if not pkg_dir.exists():
        return all_violations, all_forbidden

    for f in pkg_dir.rglob("*.py"):
        v, fb = _check_file(f, project_root)
        all_violations.extend(v)
        all_forbidden.extend(fb)

    return all_violations, all_forbidden


def main() -> int:
    """Run OC checks and print violations as warnings. Always exits 0."""
    project_root = Path(__file__).resolve().parent.parent
    violations, forbidden = check_oc(project_root)

    if forbidden:
        for f in forbidden:
            print(f"FORBIDDEN: {f}")
    if violations:
        for v in violations:
            print(f"OC: {v}")
    if not violations and not forbidden:
        print("OK: no OC violations or forbidden patterns")
    else:
        print(f"\nWarnings: {len(forbidden)} forbidden, {len(violations)} OC")

    return 0


if __name__ == "__main__":
    sys.exit(main())
