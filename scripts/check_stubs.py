#!/usr/bin/env python3
"""Check test stubs against @id tags in the in-progress .feature file."""

from __future__ import annotations

import ast
import re
import sys
from pathlib import Path


def _in_progress_feature(project_root: Path) -> Path | None:
    """Return the single .feature file in in-progress/, or None."""
    ip = project_root / "docs" / "features" / "in-progress"
    if not ip.exists():
        return None
    files = [f for f in ip.iterdir() if f.suffix == ".feature"]
    return files[0] if len(files) == 1 else None


def _extract_ids(text: str) -> set[str]:
    """Extract all @id tags that precede Example: blocks."""
    return set(re.findall(r"@(\w+)\n\s*Example:", text))


def _scan_test_dir(stub_dir: Path) -> dict[str, dict]:
    """Parse all *_test.py files and map test functions to metadata."""
    mapping: dict[str, dict] = {}
    for f in stub_dir.glob("*_test.py"):
        tree = ast.parse(f.read_text(), filename=str(f))
        for node in ast.walk(tree):
            if not isinstance(node, ast.FunctionDef):
                continue
            mapping[node.name] = {
                "file": f.name,
                "skipped": any(
                    isinstance(dec, ast.Attribute) and dec.attr == "skip"
                    for dec in node.decorator_list
                ),
            }
    return mapping


def check_stubs(project_root: Path) -> tuple[bool, list[str], dict]:
    """Check stubs; return (ok, errors, stats)."""
    feature = _in_progress_feature(project_root)
    if feature is None:
        return False, ["no feature file in in-progress/"], {}

    stem = feature.stem
    ids = _extract_ids(feature.read_text())
    stub_dir = project_root / "tests" / "features" / stem
    stats = {"total_ids": len(ids), "stubs_found": 0, "skipped": 0}

    if not stub_dir.exists():
        return (
            False,
            [f"tests/features/{stem}/ does not exist"],
            stats,
        )

    mapping = _scan_test_dir(stub_dir)
    errors = []
    found_ids: set[str] = set()

    for id_tag in ids:
        func_name = f"test_{stem}_{id_tag}"
        if func_name not in mapping:
            errors.append(f"missing stub for @id {id_tag} ({func_name})")
        else:
            found_ids.add(id_tag)
            stats["stubs_found"] += 1
            if mapping[func_name]["skipped"]:
                stats["skipped"] += 1

    for func_name, meta in mapping.items():
        if func_name.startswith(f"test_{stem}_"):
            derived_id = func_name[len(f"test_{stem}_") :]
            if derived_id not in ids:
                errors.append(f"orphan stub {func_name} in {meta['file']}")

    if not ids:
        errors.append("no @id tags found in .feature file")

    return not errors, errors, stats


def main() -> int:
    """Run stub check and print results."""
    project_root = Path(__file__).resolve().parent.parent
    ok, errors, stats = check_stubs(project_root)
    if not stats:
        for err in errors:
            print(f"ERROR: {err}")
        return 1
    print(
        f"ids: {stats['total_ids']}, "
        f"stubs: {stats['stubs_found']}, "
        f"skipped: {stats['skipped']}"
    )
    if ok:
        print("OK: all @id tags have matching stubs")
        return 0
    for err in errors:
        print(f"ERROR: {err}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
