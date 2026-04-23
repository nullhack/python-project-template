#!/usr/bin/env python3
"""Assign @id tags to untagged Examples and verify global uniqueness.

Calls pytest-beehave's assign_ids() to write missing @id tags into .feature
files, then checks that all @id values are globally unique across every stage
(backlog, in-progress, completed).

Exit 0 if all Examples are tagged and IDs are unique.
Exit 1 on missing tags, duplicate IDs, or write failures.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

from pytest_beehave.id_generator import assign_ids

_ID_RE: re.Pattern[str] = re.compile(r"@id:([a-f0-9]{8})")

FEATURE_STAGES: tuple[str, ...] = ("backlog", "in-progress", "completed")


def _collect_all_ids(features_dir: Path) -> dict[str, list[str]]:
    """Collect all @id values across all stages, mapping id -> [locations].

    Args:
        features_dir: Root features directory.

    Returns:
        Dict mapping each id to a list of "file:line" location strings.
    """
    locations: dict[str, list[str]] = {}
    for stage in FEATURE_STAGES:
        stage_dir = features_dir / stage
        if not stage_dir.exists():
            continue
        for feature_path in sorted(stage_dir.rglob("*.feature")):
            for line_no, line in enumerate(
                feature_path.read_text(encoding="utf-8").splitlines(), start=1
            ):
                for match in _ID_RE.finditer(line):
                    tag_id = match.group(1)
                    locations.setdefault(tag_id, []).append(
                        f"{feature_path.relative_to(features_dir.parent.parent)}:{line_no}"
                    )
    return locations


def _check_uniqueness(locations: dict[str, list[str]]) -> list[str]:
    """Return error strings for any @id that appears more than once.

    Args:
        locations: Dict mapping each id to its location strings.

    Returns:
        List of error strings for duplicate IDs.
    """
    errors: list[str] = []
    for tag_id, locs in sorted(locations.items()):
        if len(locs) > 1:
            joined = ", ".join(locs)
            errors.append(f"duplicate @id:{tag_id} found in {joined}")
    return errors


def main() -> int:
    """Run @id assignment and uniqueness check."""
    project_root = Path(__file__).resolve().parent.parent
    features_dir = project_root / "docs" / "features"

    if not features_dir.exists():
        print("ERROR: docs/features/ not found")
        return 1

    write_errors = assign_ids(features_dir)
    for err in write_errors:
        print(f"ERROR: {err}")

    locations = _collect_all_ids(features_dir)
    uniqueness_errors = _check_uniqueness(locations)
    for err in uniqueness_errors:
        print(f"ERROR: {err}")

    total_ids = len(locations)
    total_examples = sum(len(v) for v in locations.values())

    if write_errors or uniqueness_errors:
        print(f"ids: {total_ids}, examples: {total_examples} — FAILED")
        return 1

    print(f"ids: {total_ids}, examples: {total_examples}")
    print("OK: all Examples have @id tags and all IDs are unique")
    return 0


if __name__ == "__main__":
    sys.exit(main())
