"""Generate and sync the TODO.md session bookmark from .feature files.

Reads the in-progress feature folder (or backlog if no in-progress feature),
merges missing @id rows into the existing TODO.md, and writes the result.

Modes:
    uv run task gen-todo              Merge-write TODO.md (default)
    uv run task gen-todo -- --check   Dry run — show what would change

Merge rules:
    - Adds @id rows that are in .feature files but missing from TODO.md
    - Never removes or downgrades existing [x], [~], [-] rows
    - Updates the Feature/Step/Source header from the in-progress folder
    - If no feature is in-progress, writes the "No feature in progress" format
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[4]
FEATURES_DIR = PROJECT_ROOT / "docs" / "features"
TODO_PATH = PROJECT_ROOT / "TODO.md"

PROGRESS_ROW_RE = re.compile(r"^- \[(?P<status>[x~\- ])\] `@id:(?P<id>[a-f0-9]{8})`")
ID_TAG_RE = re.compile(r"@id:([a-f0-9]{8})")
EXAMPLE_RE = re.compile(r"^\s*Example:\s*(.+)$")
DEPRECATED_TAG_RE = re.compile(r"@deprecated")


@dataclass(frozen=True, slots=True)
class Criterion:
    """One acceptance criterion extracted from a .feature file."""

    id_hex: str
    title: str
    deprecated: bool


def find_in_progress_feature() -> tuple[str, Path] | None:
    """Find the single feature currently in docs/features/in-progress/.

    Returns:
        Tuple of (feature_name, feature_path) or None if nothing is in progress.
    """
    in_progress = FEATURES_DIR / "in-progress"
    if not in_progress.exists():
        return None
    folders = [
        f
        for f in in_progress.iterdir()
        if f.is_dir() and f.name != ".gitkeep" and not f.name.startswith(".")
    ]
    if not folders:
        return None
    return folders[0].name, folders[0]


def find_backlog_features() -> list[str]:
    """List feature names in docs/features/backlog/.

    Returns:
        Sorted list of feature folder names.
    """
    backlog = FEATURES_DIR / "backlog"
    if not backlog.exists():
        return []
    return sorted(
        f.name
        for f in backlog.iterdir()
        if f.is_dir() and f.name != ".gitkeep" and not f.name.startswith(".")
    )


def extract_criteria(feature_path: Path) -> list[Criterion]:
    """Extract all @id-tagged Examples from .feature files in a feature folder.

    Args:
        feature_path: Path to the feature folder.

    Returns:
        Ordered list of Criterion objects (deprecated ones included).
    """
    criteria: list[Criterion] = []
    for feature_file in sorted(feature_path.glob("*.feature")):
        criteria.extend(_parse_feature_file(feature_file))
    return criteria


def _parse_feature_file(path: Path) -> list[Criterion]:
    """Parse a single .feature file for @id-tagged Examples.

    Args:
        path: Path to the .feature file.

    Returns:
        List of Criterion objects found in this file.
    """
    lines = path.read_text(encoding="utf-8").splitlines()
    criteria: list[Criterion] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        id_match = ID_TAG_RE.search(line)
        if id_match:
            id_hex = id_match.group(1)
            deprecated = bool(DEPRECATED_TAG_RE.search(line))
            title = _find_example_title(lines, i + 1)
            criteria.append(
                Criterion(id_hex=id_hex, title=title, deprecated=deprecated)
            )
        i += 1
    return criteria


def _find_example_title(lines: list[str], start: int) -> str:
    """Scan forward from start to find the Example: title line.

    Args:
        lines: All lines from the .feature file.
        start: Index to start scanning from.

    Returns:
        The Example title string, or empty string if not found.
    """
    for i in range(start, min(start + 5, len(lines))):
        m = EXAMPLE_RE.match(lines[i])
        if m:
            return m.group(1).strip()
    return ""


def read_existing_progress(todo_text: str) -> dict[str, str]:
    """Extract existing @id rows and their status from TODO.md content.

    Args:
        todo_text: Full content of current TODO.md.

    Returns:
        Dict mapping id_hex -> status character ('x', '~', '-', ' ').
    """
    existing: dict[str, str] = {}
    for line in todo_text.splitlines():
        m = PROGRESS_ROW_RE.match(line)
        if m:
            existing[m.group("id")] = m.group("status")
    return existing


def build_progress_lines(
    criteria: list[Criterion],
    existing: dict[str, str],
) -> list[str]:
    """Build the ## Progress section lines, merging new with existing.

    Args:
        criteria: All criteria from .feature files (in order).
        existing: Existing @id -> status mapping from current TODO.md.

    Returns:
        List of progress row strings (without trailing newline).
    """
    lines = []
    for c in criteria:
        status = existing.get(c.id_hex, " ")
        label = c.title if c.title else "(no title)"
        suffix = " — DEPRECATED" if c.deprecated else ""
        lines.append(f"- [{status}] `@id:{c.id_hex}`: {label}{suffix}")
    return lines


def build_todo_content(
    feature_name: str,
    step: str,
    source: str,
    progress_lines: list[str],
    next_action: str,
) -> str:
    """Assemble the full TODO.md content.

    Args:
        feature_name: Display name of the current feature.
        step: Current step number and name, e.g. '4 (implement)'.
        source: Path to discovery.md.
        progress_lines: The ## Progress rows.
        next_action: The ## Next one-liner.

    Returns:
        Full TODO.md content string.
    """
    lines = [
        "# Current Work",
        "",
        f"Feature: {feature_name}",
        f"Step: {step}",
        f"Source: {source}",
        "",
        "## Progress",
        *progress_lines,
        "",
        "## Next",
        next_action,
        "",
    ]
    return "\n".join(lines)


def build_empty_todo() -> str:
    """Build the 'No feature in progress' TODO.md content.

    Returns:
        Minimal TODO.md content string.
    """
    return "\n".join(
        [
            "# Current Work",
            "",
            "No feature in progress.",
            "Next: PO picks feature from docs/features/backlog/ and moves it to docs/features/in-progress/.",
            "",
        ]
    )


def _extract_header_field(todo_text: str, field: str) -> str:
    """Extract a header field value from existing TODO.md.

    Args:
        todo_text: Full TODO.md content.
        field: Field name to look for (e.g. 'Step', 'Feature').

    Returns:
        The value string, or empty string if not found.
    """
    pattern = re.compile(rf"^{field}:\s*(.+)$", re.MULTILINE)
    m = pattern.search(todo_text)
    return m.group(1).strip() if m else ""


def _extract_next_action(todo_text: str) -> str:
    """Extract the ## Next line from existing TODO.md.

    Args:
        todo_text: Full TODO.md content.

    Returns:
        The Next action string, or a placeholder.
    """
    lines = todo_text.splitlines()
    for i, line in enumerate(lines):
        if line.strip() == "## Next":
            if i + 1 < len(lines) and lines[i + 1].strip():
                return lines[i + 1].strip()
    return "<fill in next action>"


def sync_todo(*, check_only: bool = False) -> int:
    """Main sync logic: read feature state, merge TODO.md, write if changed.

    Args:
        check_only: If True, report changes without writing.

    Returns:
        Exit code: 0 = in sync or wrote successfully, 1 = changes needed (check mode).
    """
    result = find_in_progress_feature()

    if result is None:
        new_content = build_empty_todo()
        existing = TODO_PATH.read_text(encoding="utf-8") if TODO_PATH.exists() else ""
        if existing.strip() == new_content.strip():
            print("TODO.md is in sync.")
            return 0
        if check_only:
            print("TODO.md would be updated: no feature in progress format.")
            return 1
        TODO_PATH.write_text(new_content, encoding="utf-8")
        print("TODO.md updated: no feature in progress.")
        return 0

    feature_name, feature_path = result
    criteria = extract_criteria(feature_path)

    existing_text = TODO_PATH.read_text(encoding="utf-8") if TODO_PATH.exists() else ""
    existing_progress = read_existing_progress(existing_text)

    # Preserve existing header fields if present; otherwise use defaults
    step = (
        _extract_header_field(existing_text, "Step") or "? (unknown — update manually)"
    )
    source = f"docs/features/in-progress/{feature_name}/discovery.md"
    next_action = _extract_next_action(existing_text)

    progress_lines = build_progress_lines(criteria, existing_progress)
    new_content = build_todo_content(
        feature_name=feature_name,
        step=step,
        source=source,
        progress_lines=progress_lines,
        next_action=next_action,
    )

    existing_ids = set(existing_progress.keys())
    feature_ids = {c.id_hex for c in criteria}
    new_ids = feature_ids - existing_ids

    if existing_text.strip() == new_content.strip():
        print("TODO.md is in sync.")
        return 0

    if check_only:
        if new_ids:
            print(f"TODO.md would add {len(new_ids)} new @id row(s):")
            for c in criteria:
                if c.id_hex in new_ids:
                    print(f"  [ ] @id:{c.id_hex}: {c.title}")
        else:
            print("TODO.md header or structure would be updated.")
        return 1

    TODO_PATH.write_text(new_content, encoding="utf-8")
    if new_ids:
        print(f"TODO.md updated: added {len(new_ids)} new @id row(s).")
        for c in criteria:
            if c.id_hex in new_ids:
                print(f"  [ ] @id:{c.id_hex}: {c.title}")
    else:
        print("TODO.md updated.")
    return 0


def main() -> int:
    """Entry point for the gen-todo command.

    Returns:
        Exit code (0 = success, 1 = changes needed in check mode).
    """
    check_only = "--check" in sys.argv
    return sync_todo(check_only=check_only)


if __name__ == "__main__":
    raise SystemExit(main())
