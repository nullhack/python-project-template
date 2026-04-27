#!/usr/bin/env python3
"""Assign @id tags to untagged Examples and verify global uniqueness.

Scans all .feature files for Example: blocks without @id: tags, generates a
random 8-char hex ID for each, inserts it on the line before the Example:
line, then checks that all @id values are globally unique across every stage
(backlog, in-progress, completed).

Exit 0 if all Examples are tagged and IDs are unique.
Exit 1 on missing tags, duplicate IDs, or write failures.
"""

from __future__ import annotations

import re
import secrets
import sys
from pathlib import Path

_ID_RE: re.Pattern[str] = re.compile(r"@id:([a-f0-9]{8})")
_EXAMPLE_RE: re.Pattern[str] = re.compile(r"^\s+Example:")
_TAG_LINE_RE: re.Pattern[str] = re.compile(r"^\s+@\w+")

FEATURE_STAGES: tuple[str, ...] = ("backlog", "in-progress", "completed")


def _generate_id(existing_ids: set[str]) -> str:
    """Generate a unique 8-char hex ID not in existing_ids."""
    while True:
        new_id = f"{secrets.randbelow(0x100000000):08x}"
        if new_id not in existing_ids:
            return new_id


def _assign_ids_in_file(feature_path: Path, existing_ids: set[str]) -> list[str]:
    """Assign @id tags to untagged Examples in a single .feature file.

    Args:
        feature_path: Path to the .feature file.
        existing_ids: Set of already-used IDs to avoid collisions.

    Returns:
        List of error strings for write failures.
    """
    text = feature_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    modified = False
    errors: list[str] = []
    result_lines: list[str] = []

    i = 0
    while i < len(lines):
        line = lines[i]

        if _EXAMPLE_RE.match(line):
            has_id = False

            prev_has_tag = i > 0 and _TAG_LINE_RE.match(lines[i - 1])
            if prev_has_tag and _ID_RE.search(lines[i - 1]):
                has_id = True

            if not has_id:
                new_id = _generate_id(existing_ids)
                existing_ids.add(new_id)
                indent = "    "
                for ch in line:
                    if ch == " ":
                        indent += " "
                    else:
                        break
                indent = indent[:4]
                result_lines.append(f"{indent}@id:{new_id}")
                modified = True

        result_lines.append(line)
        i += 1

    if modified:
        try:
            feature_path.write_text("\n".join(result_lines) + "\n", encoding="utf-8")
        except OSError as e:
            errors.append(f"failed to write {feature_path}: {e}")

    return errors


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

    existing_ids: set[str] = set()
    locations = _collect_all_ids(features_dir)
    existing_ids.update(locations.keys())

    write_errors: list[str] = []
    for stage in FEATURE_STAGES:
        stage_dir = features_dir / stage
        if not stage_dir.exists():
            continue
        for feature_path in sorted(stage_dir.rglob("*.feature")):
            errors = _assign_ids_in_file(feature_path, existing_ids)
            write_errors.extend(errors)

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
