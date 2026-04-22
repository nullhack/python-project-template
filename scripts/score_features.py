#!/usr/bin/env python3
"""Score backlog features for WSJF selection."""

from __future__ import annotations

import re
import sys
from pathlib import Path


def _backlog_features(project_root: Path) -> list[Path]:
    """List all .feature files in docs/features/backlog/."""
    backlog = project_root / "docs" / "features" / "backlog"
    if not backlog.exists():
        return []
    return sorted(f for f in backlog.iterdir() if f.suffix == ".feature")


def _count_ids(text: str) -> int:
    """Count @id tags that precede Example: blocks."""
    return len(re.findall(r"@(\w+)\n\s*Example:", text))


def _count_must(text: str) -> int:
    """Count 'Must' markers (case-insensitive, whole word)."""
    return len(re.findall(r"\bMust\b", text))


def _effort_from_ids(count: int) -> str:
    """Map @id count to effort tier."""
    if count <= 2:
        return "trivial"
    if count <= 5:
        return "small"
    if count <= 8:
        return "medium"
    return "large"


def score_features(project_root: Path) -> list[dict]:
    """Score each backlog feature; return list of result dicts."""
    results = []
    for f in _backlog_features(project_root):
        text = f.read_text()
        ids = _count_ids(text)
        must = _count_must(text)
        results.append(
            {
                "stem": f.stem,
                "ids": ids,
                "must": must,
                "effort": _effort_from_ids(ids),
            }
        )
    return results


def main() -> int:
    """Print a WSJF scoring table for backlog features."""
    project_root = Path(__file__).resolve().parent.parent
    results = score_features(project_root)

    if not results:
        print("No backlog features found.")
        return 0

    print("| Feature | @ids | Effort | Must count |")
    print("|---------|------|--------|------------|")
    for r in results:
        print(f"| {r['stem']} | {r['ids']} | {r['effort']} | {r['must']} |")

    return 0


if __name__ == "__main__":
    sys.exit(main())
