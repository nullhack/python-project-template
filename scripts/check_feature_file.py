#!/usr/bin/env python3
"""Validate the in-progress .feature file structure."""

from __future__ import annotations

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


def _flush_example(
    current_example: dict | None,
    current_rule: dict | None,
) -> dict | None:
    """Append current_example to current_rule and return None."""
    if current_example is not None and current_rule is not None:
        current_rule["examples"].append(current_example)
    return None


def _flush_rule(current_rule: dict | None, data: dict) -> dict | None:
    """Append current_rule to data["rules"] and return None."""
    if current_rule is not None:
        data["rules"].append(current_rule)
    return None


def _handle_rule_line(
    line: str, current_example: dict | None, current_rule: dict | None, data: dict
) -> tuple[dict | None, dict | None]:
    """Process a 'Rule:' line and return updated state."""
    current_example = _flush_example(current_example, current_rule)
    current_rule = _flush_rule(current_rule, data)
    return {"name": line, "examples": []}, current_example


def _handle_tag_line(
    line: str, current_example: dict | None, current_rule: dict | None
) -> tuple[dict | None, dict | None]:
    """Process an @id tag line and return updated state."""
    current_example = _flush_example(current_example, current_rule)
    return {"id": line[1:], "steps": []}, current_example


def _handle_keyword_line(
    line: str, current_example: dict | None, data: dict
) -> dict | None:
    """Process Example:/Scenario: or step lines."""
    if current_example is None:
        current_example = {"id": None, "steps": []}
    if line.startswith("Scenario:"):
        data["errors"].append("uses 'Scenario:' instead of 'Example:'")
    return current_example


def parse_feature(text: str) -> dict:
    """Parse a .feature file into structured data via regex."""
    data = {
        "has_baselined": False,
        "rules": [],
        "errors": [],
    }
    current_rule: dict | None = None
    current_example: dict | None = None

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if "Status: BASELINED" in line:
            data["has_baselined"] = True
        if line.startswith("Rule:"):
            current_rule, current_example = _handle_rule_line(
                line, current_example, current_rule, data
            )
        if re.match(r"^@\w+$", line):
            current_example, _ = _handle_tag_line(line, current_example, current_rule)
        if line.startswith(("Example:", "Scenario:")):
            current_example = _handle_keyword_line(line, current_example, data)
        step_keywords = ("Given ", "When ", "Then ", "And ", "But ")
        if line.startswith(step_keywords) and current_example is not None:
            current_example["steps"].append(line)

    current_example = _flush_example(current_example, current_rule)
    _flush_rule(current_rule, data)

    return data


def _validate_examples(rule: dict, errors: list[str]) -> int:
    """Validate all examples in a rule; return count."""
    count = 0
    if not rule["examples"]:
        errors.append(f"{rule['name']} has no Example: blocks")
    for ex in rule["examples"]:
        count += 1
        if not ex["id"]:
            errors.append(f"Example in {rule['name']} missing @id tag")
        steps = [s.split()[0] for s in ex["steps"]]
        for keyword in ("Given", "When", "Then"):
            if keyword not in steps:
                errors.append(f"@{ex['id'] or '?'} missing {keyword} step")
    return count


def validate_feature(project_root: Path) -> tuple[bool, list[str]]:
    """Validate the in-progress feature file; return (ok, errors)."""
    feature = _in_progress_feature(project_root)
    if feature is None:
        return False, ["no feature file in docs/features/in-progress/"]

    data = parse_feature(feature.read_text())
    errors = list(data["errors"])

    if not data["has_baselined"]:
        errors.append("missing 'Status: BASELINED'")
    if not data["rules"]:
        errors.append("no 'Rule:' blocks found")

    total_examples = sum(_validate_examples(rule, errors) for rule in data["rules"])

    if total_examples > 8:
        errors.append(f"decomposition check failed: {total_examples} examples (>8)")

    return not errors, errors


def main() -> int:
    """Run validation and print results."""
    project_root = Path(__file__).resolve().parent.parent
    ok, errors = validate_feature(project_root)
    if ok:
        print("OK: feature file is valid")
        return 0
    for err in errors:
        print(f"ERROR: {err}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
