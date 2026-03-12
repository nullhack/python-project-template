#!/usr/bin/env python3
"""Validate YAML frontmatter in agents and skills."""

import sys
import yaml
from pathlib import Path


def validate_yaml_file(filepath: Path) -> tuple[bool, str]:
    """Validate YAML frontmatter in a file."""
    if not filepath.exists():
        return False, f"File does not exist: {filepath}"

    try:
        with open(filepath, "r") as f:
            content = f.read()

        if "---" not in content:
            return True, f"No YAML frontmatter in {filepath}"

        parts = content.split("---")
        if len(parts) < 3:
            return True, f"No complete YAML frontmatter in {filepath}"

        yaml_part = parts[1]
        if yaml_part.strip():
            data = yaml.safe_load(yaml_part)
            if data is None:
                return False, f"Empty YAML frontmatter in {filepath}"

        return True, f"Valid YAML in {filepath}"
    except yaml.YAMLError as e:
        return False, f"YAML error in {filepath}: {e}"
    except Exception as e:
        return False, f"Error in {filepath}: {e}"


def main():
    projects = ["python-project-example", "custom-test-project"]
    errors = []

    for project in projects:
        project_path = Path(project)

        # Validate agents
        agents_dir = project_path / ".opencode" / "agents"
        if agents_dir.exists():
            for agent_file in agents_dir.glob("*.md"):
                valid, msg = validate_yaml_file(agent_file)
                print(msg)
                if not valid:
                    errors.append(msg)

        # Validate skills
        skills_dir = project_path / ".opencode" / "skills"
        if skills_dir.exists():
            for skill_dir in skills_dir.iterdir():
                skill_file = skill_dir / "SKILL.md"
                if skill_file.exists():
                    valid, msg = validate_yaml_file(skill_file)
                    print(msg)
                    if not valid:
                        errors.append(msg)

    if errors:
        print(f"\nFAIL: Found {len(errors)} YAML errors")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)

    print("\nAll YAML frontmatter is valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
