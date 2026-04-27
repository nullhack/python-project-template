#!/usr/bin/env python3
"""Detect the current workflow state from filesystem signals."""

from __future__ import annotations

import io
import re
import sys
from pathlib import Path


def _current_branch(project_root: Path) -> str:
    """Return the current git branch name by reading .git/HEAD."""
    git_head = project_root / ".git" / "HEAD"
    if not git_head.exists():
        return ""
    content = git_head.read_text().strip()
    if content.startswith("ref: refs/heads/"):
        return content[len("ref: refs/heads/") :]
    return ""


def _in_progress_feature(project_root: Path) -> Path | None:
    """Return the single .feature file in in-progress/, or None."""
    ip = project_root / "docs" / "features" / "in-progress"
    if not ip.exists():
        return None
    files = [f for f in ip.iterdir() if f.suffix == ".feature"]
    return files[0] if len(files) == 1 else None


def _has_status_baselined(text: str) -> bool:
    """True if the feature text contains 'Status: BASELINED'."""
    return "Status: BASELINED" in text


def _has_rule_blocks(text: str) -> bool:
    """True if any 'Rule:' block exists."""
    return "Rule:" in text


def _has_example_with_id(text: str) -> bool:
    """True if any 'Example:' block carries an @id tag."""
    return bool(re.search(r"@\w+\n\s*Example:", text))


def _backlog_features_with_baselined_no_id(
    project_root: Path,
) -> bool:
    """Check if any backlog feature is BASELINED but lacks @id Examples."""
    backlog = project_root / "docs" / "features" / "backlog"
    if not backlog.exists():
        return False
    for f in backlog.iterdir():
        if f.suffix != ".feature":
            continue
        text = f.read_text()
        if _has_status_baselined(text) and not _has_example_with_id(text):
            return True
    return False


def _branch_exists(project_root: Path, branch_name: str) -> bool:
    """Check if a local branch exists by reading .git/refs or packed-refs."""
    ref_file = project_root / ".git" / "refs" / "heads" / branch_name
    if ref_file.exists():
        return True
    packed = project_root / ".git" / "packed-refs"
    if packed.exists():
        marker = f" refs/heads/{branch_name}"
        return any(line.endswith(marker) for line in packed.read_text().splitlines())
    return False


def _feature_branch_exists(project_root: Path, feature_stem: str) -> bool:
    """Check if a feat/ or fix/ branch exists for this feature."""
    return _branch_exists(project_root, f"feat/{feature_stem}") or _branch_exists(
        project_root, f"fix/{feature_stem}"
    )


def _stubs_exist(project_root: Path, feature_stem: str) -> bool:
    """True if tests/features/<stem>/ exists and has .py files."""
    stub_dir = project_root / "tests" / "features" / feature_stem
    return stub_dir.exists() and any(stub_dir.glob("*_test.py"))


def _count_skipped_stubs(project_root: Path, feature_stem: str) -> int:
    """Count @pytest.mark.skip decorators in test stubs."""
    stub_dir = project_root / "tests" / "features" / feature_stem
    if not stub_dir.exists():
        return 0
    return sum(
        f.read_text().count("@pytest.mark.skip") for f in stub_dir.glob("*_test.py")
    )


def _pytest_result(project_root: Path, feature_stem: str) -> int:
    """Run pytest on feature tests and return exit code."""
    try:
        import pytest
    except ImportError:
        return 0
    stub_dir = project_root / "tests" / "features" / feature_stem
    if not stub_dir.exists():
        return 0
    buf = io.StringIO()
    old_stdout, old_stderr = sys.stdout, sys.stderr
    sys.stdout = sys.stderr = buf
    try:
        code = pytest.main([str(stub_dir), "-q", "--tb=no"])
    finally:
        sys.stdout, sys.stderr = old_stdout, old_stderr
    return int(code)


def _session_state(project_root: Path) -> str | None:
    """Read current @state from .flowr/sessions/session.yaml."""
    session = project_root / ".flowr" / "sessions" / "session.yaml"
    if not session.exists():
        return None
    for line in session.read_text().splitlines():
        m = re.match(r"^\s*@?state:\s*(\S+)", line)
        if m:
            return m.group(1)
    return None


def _work_md_state(project_root: Path) -> str | None:
    """Parse WORK.md for the first @state value in ## Active Items."""
    work_md = project_root / "WORK.md"
    if not work_md.exists():
        return None
    text = work_md.read_text()
    in_active = False
    for line in text.splitlines():
        if line.strip().startswith("## Active Items"):
            in_active = True
            continue
        if in_active and line.strip().startswith("##"):
            break
        if in_active and "@state:" in line:
            return line.split("@state:")[1].strip().split()[0]
    return None


def _postmortem_exists(project_root: Path, feature_stem: str) -> bool:
    """Check if any post-mortem file references this feature stem."""
    pm_dir = project_root / "docs" / "post-mortem"
    if not pm_dir.exists():
        return False
    return any(feature_stem in f.name for f in pm_dir.iterdir() if f.is_file())


def _load_states_from_flows(project_root: Path) -> set[str]:
    """Load all valid state IDs from .flowr/flows/*.yaml files."""
    flows_dir = project_root / ".flowr" / "flows"
    states: set[str] = set()
    if not flows_dir.exists():
        return states
    for f in flows_dir.glob("*.yaml"):
        text = f.read_text()
        states.update(
            m.group(1) for m in re.finditer(r"^\s+-\s+id:\s+(\S+)", text, re.MULTILINE)
        )
    return states


def _detect_idle(project_root: Path) -> tuple[str, str]:
    """No feature in progress."""
    if _backlog_features_with_baselined_no_id(project_root):
        return "backlog-criteria", "backlog BASELINED but no @id"
    return "idle", "no feature in in-progress/"


def _detect_from_content(
    project_root: Path, text: str, stem: str
) -> tuple[str, str] | None:
    """Content-based detection."""
    if not _has_status_baselined(text):
        return "discovery", "feature in-progress but not BASELINED"
    if not _has_rule_blocks(text):
        return "stories", "BASELINED but no Rule: blocks"
    if not _has_example_with_id(text):
        return "criteria", "Rule: blocks present but no @id Examples"
    if not _feature_branch_exists(project_root, stem):
        return "ready", f"@id present but no feat/{stem} or fix/{stem} branch"
    return None


def _detect_from_tests(
    project_root: Path, stem: str, branch: str
) -> tuple[str, str] | None:
    """Branch and test state detection."""
    stubs = _stubs_exist(project_root, stem)
    if branch.startswith((f"feat/{stem}", f"fix/{stem}")) and not stubs:
        return "stubs", f"on {branch} but no test stubs in tests/features/{stem}/"

    skipped = _count_skipped_stubs(project_root, stem)
    if stubs and skipped == 0:
        if _pytest_result(project_root, stem) != 0:
            return "red", "unskipped test exists that fails"
        return "step-4-ready", "all tests pass, no skipped tests"

    session = _session_state(project_root)
    if session == "step-5-ready":
        return "step-5-ready", "session @state = step-5-ready"

    if stubs and skipped > 0:
        return "step-3a-working", "test stubs exist with @pytest.mark.skip remaining"

    return None


def _detect_final(project_root: Path, stem: str, branch: str) -> tuple[str, str] | None:
    """Final state detection."""
    session = _session_state(project_root)
    work = _work_md_state(project_root)
    stored = session or work
    if branch == "main" and stored == "step-5-complete":
        return "step-5-complete", "on main, session @state = step-5-complete"
    if branch.startswith((f"feat/{stem}", f"fix/{stem}")):
        return "step-5-merge", f"on {branch}, feature still in in-progress/"
    if _postmortem_exists(project_root, stem):
        return "post-mortem", f"post-mortem exists for {stem}"
    return None


def detect_state(project_root: Path) -> tuple[str, str]:
    """Evaluate detection rules and return (detected_state, reason)."""
    feature = _in_progress_feature(project_root)
    branch = _current_branch(project_root)

    if feature is None:
        return _detect_idle(project_root)

    text = feature.read_text()
    stem = feature.stem

    result = _detect_from_content(project_root, text, stem)
    if result is not None:
        return result

    result = _detect_from_tests(project_root, stem, branch)
    if result is not None:
        return result

    result = _detect_final(project_root, stem, branch)
    if result is not None:
        return result

    return "unknown", "no detection rule matched"


def main() -> int:
    """Run detection and report state, exiting non-zero on mismatch."""
    project_root = Path(__file__).resolve().parent.parent
    state, reason = detect_state(project_root)
    valid_states = _load_states_from_flows(project_root)
    session = _session_state(project_root)
    work = _work_md_state(project_root)
    stored = session or work

    print(f"Detected state: {state}")
    print(f"Reason: {reason}")
    if stored:
        print(f"Stored @state: {stored}")
        if stored != state and state in valid_states:
            print("WARNING: detected state differs from stored @state")
            return 1
    else:
        print("Stored @state: (none)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
