#!/usr/bin/env python3
"""Verify version consistency before release.

Checks:
1. Version is present in pyproject.toml.
2. CHANGELOG.md has an entry for the current version.
3. app/__init__.py __version__ matches pyproject.toml (if present).
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


def main() -> int:
    """Run version consistency checks."""
    project_root = Path(__file__).resolve().parent.parent
    pyproject = project_root / "pyproject.toml"
    changelog = project_root / "CHANGELOG.md"
    init_py = project_root / "app" / "__init__.py"

    # 1. Extract version from pyproject.toml
    version = None
    for line in pyproject.read_text().splitlines():
        if line.startswith("version"):
            version = line.split("=")[-1].strip().strip('"')
            break
    if not version:
        print("ERROR: Could not extract version from pyproject.toml")
        return 1
    print(f"Checking release v{version}")

    # 2. Check CHANGELOG.md has entry for this version
    if f"## [v{version}]" not in changelog.read_text():
        print(f"ERROR: CHANGELOG.md has no entry for v{version}")
        return 1
    print("  OK: CHANGELOG.md entry found")

    # 3. Check app/__init__.py __version__ matches (if present)
    init_text = init_py.read_text() if init_py.exists() else ""
    if "__version__" in init_text:
        match = re.search(
            r'^__version__\s*=\s*["\']([^"\']+)["\']',
            init_text,
            re.MULTILINE,
        )
        pkg_version = match.group(1) if match else None
        if pkg_version != version:
            print(
                f"ERROR: app/__init__.py __version__ ({pkg_version!r}) "
                f"does not match pyproject.toml ({version!r})"
            )
            return 1
        print("  OK: app/__init__.py __version__ matches")
    else:
        print("  NOTE: app/__init__.py has no __version__ (skipping)")

    print("Version checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
