#!/usr/bin/env python3
"""Verify version consistency before release.

Checks:
1. Version in pyproject.toml is plain semver (no + suffix, no date component).
2. CHANGELOG.md has an entry for the current version (with optional +date suffix).
3. app/__init__.py __version__ matches pyproject.toml (if present).
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")
SEMVER_BUILD_RE = re.compile(r"^\d+\.\d+\.\d+\+\d{8}$")


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

    # 2. Validate pyproject.toml version is plain semver (no + suffix, no date)
    if not SEMVER_RE.match(version):
        print(
            f"ERROR: pyproject.toml version '{version}' is not plain semver. "
            "Expected format: X.Y.Z (no + suffix, no date). "
            "The date suffix is only for git tags and CHANGELOG entries."
        )
        return 1
    print(f"Checking release v{version}")

    # 3. Check CHANGELOG.md has entry for this version
    #    Accepts both plain semver (v0.1.0) and semver+date (v0.1.0+20260427)
    changelog_text = changelog.read_text()
    import datetime

    today = datetime.datetime.now(tz=datetime.timezone.utc)
    date_suffix = f"+{today.strftime('%Y%m%d')}"
    plain_tag = f"## [v{version}]"
    dated_tag = f"## [v{version}{date_suffix}]"
    if plain_tag not in changelog_text and dated_tag not in changelog_text:
        print(
            f"ERROR: CHANGELOG.md has no entry for "
            f"v{version} or v{version}{date_suffix}"
        )
        return 1
    print("  OK: CHANGELOG.md entry found")

    # 4. Check app/__init__.py __version__ matches (if present)
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
