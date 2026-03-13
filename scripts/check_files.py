#!/usr/bin/env python3
"""Check that all required files exist in generated projects."""

import sys
from pathlib import Path

REQUIRED_FILES = [
    "pyproject.toml",
    "README.md",
    "AGENTS.md",
    ".opencode/agents/developer.md",
    ".opencode/agents/architect.md",
    ".opencode/agents/repo-manager.md",
    "Dockerfile",
]


def check_project(project_dir: str) -> tuple[bool, list[str]]:
    """Check a project for required files."""
    project_path = Path(project_dir)
    missing = []

    for file_path in REQUIRED_FILES:
        full_path = project_path / file_path
        if not full_path.exists():
            missing.append(file_path)

    return len(missing) == 0, missing


def main():
    projects = ["python-project-example", "custom-test-project"]
    all_present = True

    for project in projects:
        present, missing = check_project(project)

        if present:
            print(f"PASS: All required files present in {project}")
        else:
            print(f"FAIL: Missing files in {project}:")
            for f in missing:
                print(f"  - {f}")
            all_present = False

    if all_present:
        print("\nAll required files are present")
        return 0
    else:
        sys.exit(1)


if __name__ == "__main__":
    sys.exit(main())
