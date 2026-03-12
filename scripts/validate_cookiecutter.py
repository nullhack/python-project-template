#!/usr/bin/env python3
"""Validate cookiecutter.json has required fields."""

import json
import sys
from pathlib import Path


def main():
    required = ["project_name", "package_name", "full_name", "email", "github_username"]

    with open("cookiecutter.json") as f:
        data = json.load(f)

    missing = [key for key in required if key not in data]

    if missing:
        print(f"FAIL: Missing required keys: {missing}")
        sys.exit(1)

    print("PASS: cookiecutter.json is valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
