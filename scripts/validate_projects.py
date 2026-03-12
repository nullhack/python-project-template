#!/usr/bin/env python3
"""Validate pyproject.toml in generated projects."""

import sys
import tomllib
from pathlib import Path


def validate_project(project_dir: str) -> bool:
    toml_path = Path(project_dir) / "pyproject.toml"

    if not toml_path.exists():
        print(f"FAIL: {toml_path} does not exist")
        return False

    try:
        with open(toml_path, "rb") as f:
            data = tomllib.load(f)

        # Check required sections
        if "project" not in data:
            print(f"FAIL: {project_dir}/pyproject.toml missing [project] section")
            return False

        required_project_keys = ["name", "version", "requires-python"]
        missing = [k for k in required_project_keys if k not in data["project"]]

        if missing:
            print(f"FAIL: {project_dir}/pyproject.toml missing: {missing}")
            return False

        print(f"PASS: {project_dir}/pyproject.toml is valid")
        return True
    except Exception as e:
        print(f"FAIL: {project_dir}/pyproject.toml error: {e}")
        return False


def main():
    projects = ["python-project-example", "custom-test-project"]
    all_valid = True

    for project in projects:
        if not validate_project(project):
            all_valid = False

    if all_valid:
        print("\nAll pyproject.toml files are valid")
        return 0
    else:
        sys.exit(1)


if __name__ == "__main__":
    sys.exit(main())
