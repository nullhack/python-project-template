#!/usr/bin/env python3
"""Validate ADR files: naming convention and required sections."""

from __future__ import annotations

import re
import sys
from pathlib import Path

REQUIRED_SECTIONS = {
    "## Context",
    "## Decision",
    "## Reason",
    "## Alternatives Considered",
    "## Consequences",
}


def _adr_files(project_root: Path) -> list[Path]:
    """List all .md files in docs/adr/."""
    adr_dir = project_root / "docs" / "adr"
    if not adr_dir.exists():
        return []
    return sorted(f for f in adr_dir.iterdir() if f.suffix == ".md")


def validate_adrs(project_root: Path) -> tuple[bool, list[str]]:
    """Validate all ADR files; return (ok, errors)."""
    files = _adr_files(project_root)
    if not files:
        return True, ["no ADR files found (skipping)"]

    errors = []
    for f in files:
        if not re.match(r"ADR-\d{4}-\d{2}-\d{2}-[a-z0-9-]+\.md$", f.name):
            errors.append(
                f"{f.name}: invalid naming (expected ADR-YYYY-MM-DD-<slug>.md)"
            )

        text = f.read_text()
        for section in REQUIRED_SECTIONS:
            if section not in text:
                errors.append(f"{f.name}: missing {section}")

    return not errors, errors


def main() -> int:
    """Run ADR validation."""
    project_root = Path(__file__).resolve().parent.parent
    ok, errors = validate_adrs(project_root)
    for err in errors:
        print(f"ERROR: {err}")
    if ok and not any("no ADR files" in e for e in errors):
        print("OK: all ADR files are valid")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
