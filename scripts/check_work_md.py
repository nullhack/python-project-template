#!/usr/bin/env python3
"""Validate WORK.md structure and consistency."""

from __future__ import annotations

import re
import sys
from pathlib import Path

VALID_STATES = {
    "IDLE",
    "STEP-1-BACKLOG-CRITERIA",
    "STEP-1-DISCOVERY",
    "STEP-1-STORIES",
    "STEP-1-CRITERIA",
    "STEP-2-READY",
    "STEP-2-ARCH",
    "STEP-3-WORKING",
    "STEP-3-RED",
    "STEP-4-READY",
    "STEP-5-READY",
    "STEP-5-MERGE",
    "STEP-5-COMPLETE",
    "POST-MORTEM",
}


def _current_branch() -> str:
    """Return the current git branch name by reading .git/HEAD."""
    git_head = Path(__file__).resolve().parent.parent / ".git" / "HEAD"
    if not git_head.exists():
        return ""
    content = git_head.read_text().strip()
    # Format: "ref: refs/heads/<branch>" when on a branch
    if content.startswith("ref: refs/heads/"):
        return content[len("ref: refs/heads/") :]
    return ""


def parse_work_md(project_root: Path) -> tuple[list[dict], list[str]]:
    """Parse WORK.md active items; return (items, errors)."""
    work_md = project_root / "WORK.md"
    if not work_md.exists():
        return [], ["WORK.md does not exist"]

    text = work_md.read_text()
    in_active = False
    items: list[dict] = []
    errors: list[str] = []

    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("## Active Items"):
            in_active = True
            continue
        if in_active and stripped.startswith("##"):
            break
        if not in_active:
            continue
        if stripped.startswith("-") and "@id:" in stripped:
            item: dict = {"raw": stripped, "id": None, "state": None, "branch": None}
            id_match = re.search(r"@id:\s*(\S+)", stripped)
            state_match = re.search(r"@state:\s*(\S+)", stripped)
            branch_match = re.search(r"@branch:\s*(\S+)", stripped)
            if id_match:
                item["id"] = id_match.group(1)
            if state_match:
                item["state"] = state_match.group(1)
            if branch_match:
                item["branch"] = branch_match.group(1)
            items.append(item)

    return items, errors


def validate_work_md(project_root: Path) -> tuple[bool, list[str]]:
    """Validate WORK.md; return (ok, errors)."""
    items, errors = parse_work_md(project_root)
    branch = _current_branch()

    if not items:
        return True, errors

    for item in items:
        if item["id"] is None:
            errors.append(f"missing @id in: {item['raw']}")
        if item["state"] is None:
            errors.append(f"missing @state in: {item['raw']}")
        elif item["state"] not in VALID_STATES:
            errors.append(f"invalid @state '{item['state']}' in: {item['raw']}")
        if item["branch"] is None:
            errors.append(f"missing @branch in: {item['raw']}")
        elif item["branch"] != branch:
            errors.append(f"@branch '{item['branch']}' != current branch '{branch}'")

    return not errors, errors


def main() -> int:
    """Run WORK.md validation."""
    project_root = Path(__file__).resolve().parent.parent
    ok, errors = validate_work_md(project_root)
    if ok:
        print("OK: WORK.md is valid and consistent")
        return 0
    for err in errors:
        print(f"ERROR: {err}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
