"""Pytest configuration for BDD docstring display in HTML reports."""

import json
import os

import pytest


def _build_docstring_map() -> dict[str, str]:
    """Walk test files and map nodeid → docstring."""
    import ast
    from pathlib import Path

    mapping: dict[str, str] = {}
    tests_dir = Path(__file__).resolve().parent
    project_root = tests_dir.parent

    for py_file in tests_dir.rglob("*_test.py"):
        rel = str(py_file.relative_to(project_root))
        try:
            tree = ast.parse(py_file.read_text())
        except (SyntaxError, OSError):
            continue

        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                for item in node.body:
                    if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        if item.name.startswith("test_"):
                            doc = ast.get_docstring(item)
                            if doc:
                                mapping[f"{rel}::{node.name}::{item.name}"] = doc
            elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                if node.name.startswith("test_"):
                    doc = ast.get_docstring(node)
                    if doc:
                        mapping[f"{rel}::{node.name}"] = doc

    return mapping


@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus) -> None:
    """Add docstrings to JSON and regenerate HTML."""
    html_output = session.config.getoption("--html-output") or "docs/tests"
    json_report = session.config.getoption("--json-report") or "final_report.json"
    json_path = os.path.join(html_output, json_report)

    try:
        with open(json_path) as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return

    doc_map = _build_docstring_map()
    for result in data.get("results", []):
        nodeid = result.get("nodeid", "")

        # Strip parametrize suffix like [a-b] for lookup
        if "[" in nodeid and nodeid.endswith("]"):
            bracket_idx = nodeid.rindex("[")
            base_nodeid = nodeid[:bracket_idx]
            params = nodeid[bracket_idx + 1 : -1]
        else:
            base_nodeid = nodeid
            params = None

        doc = doc_map.get(base_nodeid)
        if doc:
            doc_html = doc.replace("\n", "<br>")
            if params:
                param_doc = f"Params: ({params.replace('-', ', ')})\n{doc}"
                param_html = param_doc.replace("\n", "<br>")
                result["docstring"] = param_doc
                result["test"] = param_html
            else:
                result["docstring"] = doc
                result["test"] = doc_html

    with open(json_path, "w") as f:
        json.dump(data, f, indent=2)

    from pytest_html_plus.generate_html_report import JSONReporter

    reporter = JSONReporter(json_path, "", html_output)
    reporter.load_report()
    reporter.generate_html_report()
