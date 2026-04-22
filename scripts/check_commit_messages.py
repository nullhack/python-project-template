#!/usr/bin/env python3
"""Validate commit messages on the current branch against conventional commits."""

from __future__ import annotations

import re
import sys
from pathlib import Path

CONVENTIONAL_RE = re.compile(
    r"^(feat|fix|test|refactor|chore|docs|perf|ci)"
    r"(\([^)]+\))?: .+"
)

FORBIDDEN = re.compile(
    r"^(wip|temp|fix tests|oops|asdf|xxx|qwerty|test)",
    re.IGNORECASE,
)


def _current_branch(project_root: Path) -> str:
    """Return the current git branch name by reading .git/HEAD."""
    git_head = project_root / ".git" / "HEAD"
    if not git_head.exists():
        return ""
    content = git_head.read_text().strip()
    if content.startswith("ref: refs/heads/"):
        return content[len("ref: refs/heads/") :]
    return ""


def _main_sha(project_root: Path) -> str:
    """Return the current SHA of main by reading .git/refs/heads/main or packed-refs."""
    ref_file = project_root / ".git" / "refs" / "heads" / "main"
    if ref_file.exists():
        return ref_file.read_text().strip()
    # Fall back to packed-refs
    packed = project_root / ".git" / "packed-refs"
    if packed.exists():
        for line in packed.read_text().splitlines():
            if line.endswith(" refs/heads/main"):
                return line.split()[0]
    return ""


def _branch_sha(project_root: Path, branch: str) -> str:
    """Return the current SHA of a branch."""
    ref_file = project_root / ".git" / "refs" / "heads" / branch
    if ref_file.exists():
        return ref_file.read_text().strip()
    packed = project_root / ".git" / "packed-refs"
    if packed.exists():
        for line in packed.read_text().splitlines():
            if line.endswith(f" refs/heads/{branch}"):
                return line.split()[0]
    return ""


def _reflog_commits(project_root: Path, branch: str) -> list[tuple[str, str]]:
    """Return (sha, subject) pairs from .git/logs/refs/heads/<branch>."""
    log_file = project_root / ".git" / "logs" / "refs" / "heads" / branch
    if not log_file.exists():
        return []
    commits = []
    for line in log_file.read_text().splitlines():
        # Format: <old-sha> <new-sha> <identity> <timestamp>\t<action>: <message>
        parts = line.split("\t", 1)
        if len(parts) < 2:
            continue
        new_sha = parts[0].split()[1]
        action_msg = parts[1]
        # Only commit entries (not checkout/merge/etc)
        if action_msg.startswith("commit: "):
            subject = action_msg[len("commit: ") :]
            commits.append((new_sha, subject))
    return commits


def _git_commits(project_root: Path) -> list[str]:
    """Return commit subjects for all commits on the current branch ahead of main."""
    branch = _current_branch(project_root)
    if not branch or branch == "main":
        return []

    main_sha = _main_sha(project_root)
    commits = _reflog_commits(project_root, branch)

    # Walk from tip back until we hit a SHA that main also has
    subjects = []
    for sha, subject in reversed(commits):
        if sha == main_sha:
            break
        subjects.append(subject)

    return list(reversed(subjects))


def validate_commits(project_root: Path) -> tuple[bool, list[str]]:
    """Check all branch commits; return (ok, errors)."""
    subjects = _git_commits(project_root)
    if not subjects:
        return True, []

    errors = []
    for subject in subjects:
        if FORBIDDEN.search(subject):
            errors.append(f"forbidden pattern: '{subject}'")
        elif not CONVENTIONAL_RE.match(subject):
            errors.append(f"non-conventional: '{subject}'")

    return not errors, errors


def main() -> int:
    """Run commit message validation."""
    project_root = Path(__file__).resolve().parent.parent
    ok, errors = validate_commits(project_root)
    if ok:
        print("OK: all commits follow conventional format")
        return 0
    for err in errors:
        print(f"ERROR: {err}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
