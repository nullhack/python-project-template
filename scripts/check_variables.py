#!/usr/bin/env python3
"""Check for unsubstituted cookiecutter variables in generated projects."""

import sys
import re
from pathlib import Path


def check_project(project_dir: str) -> tuple[bool, list[str]]:
    """Check a project for unsubstituted variables."""
    project_path = Path(project_dir)
    errors = []

    # Pattern to match unsubstituted cookiecutter variables
    pattern = re.compile(r"\{\{cookiecutter\.[^}]+\}\}")

    for filepath in project_path.rglob("*"):
        # Skip certain directories
        if any(
            skip in filepath.parts
            for skip in ["venv", ".git", "__pycache__", ".pytest_cache"]
        ):
            continue

        # Only check files
        if not filepath.is_file():
            continue

        # Skip binary files and certain extensions
        if filepath.suffix in [".pyc", ".egg-info", ".so", ".whl"]:
            continue

        try:
            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()

            matches = pattern.findall(content)
            if matches:
                errors.append(f"{filepath.relative_to(project_path)}: {matches}")
        except Exception:
            pass

    return len(errors) == 0, errors


def main():
    projects = ["python-project-example", "custom-test-project"]
    all_clean = True

    for project in projects:
        clean, errors = check_project(project)

        if clean:
            print(f"PASS: No unsubstituted variables in {project}")
        else:
            print(f"FAIL: Found unsubstituted variables in {project}:")
            for err in errors:
                print(f"  {err}")
            all_clean = False

    if all_clean:
        print("\nNo unsubstituted cookiecutter variables found")
        return 0
    else:
        sys.exit(1)


if __name__ == "__main__":
    sys.exit(main())
