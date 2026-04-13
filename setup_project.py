#!/usr/bin/env python3
"""Setup a new Python project from the template.

This script copies template files from .opencode/templates/ to the project root,
substituting templated fields with the provided parameters.

Usage:
    # Interactive mode (prompts for any missing values)
    python setup_project.py

    # With parameters
    python setup_project.py --github-username myuser --project-name my-project \
        --project-description "My project description" --author-name "My Name"

    # Accept defaults for missing values
    python setup_project.py --github-username myuser --yes
"""

import argparse
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

TEMPLATES_DIR = Path(__file__).parent / ".opencode" / "templates"
ROOT_DIR = Path(__file__).parent
DEFAULTS_FILE = ROOT_DIR / "project_defaults.json"


def load_defaults() -> dict:
    """Load defaults from JSON file."""
    if DEFAULTS_FILE.exists():
        return json.loads(DEFAULTS_FILE.read_text(encoding="utf-8"))
    return {}


def substitute_values(content: str, replacements: dict) -> str:
    """Replace all values in content based on replacements dict."""
    result = content
    for original, replacement in replacements.items():
        result = result.replace(original, replacement)
    return result


def prompt_for_value(key: str, default: str | None = None) -> str:
    """Prompt user for a value."""
    prompt = f"{key}"
    if default:
        prompt += f" [{default}]"
    prompt += ": "
    value = input(prompt)
    return value if value else (default or "")


def process_templates(replacements: dict) -> None:
    """Process template files and create them in the root directory."""
    for template_file in TEMPLATES_DIR.glob("*.template"):
        dst_name = template_file.stem

        if dst_name == "project_defaults":
            continue

        content = template_file.read_text(encoding="utf-8")
        content = substitute_values(content, replacements)

        dst_path = ROOT_DIR / dst_name
        dst_path.write_text(content, encoding="utf-8")
        print(f"Created: {dst_path.relative_to(ROOT_DIR)}")

    github_templates_dir = TEMPLATES_DIR / ".github"
    if github_templates_dir.exists():
        github_dst_dir = ROOT_DIR / ".github"
        if github_dst_dir.exists():
            shutil.rmtree(github_dst_dir)
        github_dst_dir.mkdir(parents=True, exist_ok=True)

        for item in github_templates_dir.rglob("*"):
            if item.is_file():
                rel_path = item.relative_to(github_templates_dir)
                dst_path = github_dst_dir / rel_path
                dst_path.parent.mkdir(parents=True, exist_ok=True)

                if item.suffix == ".template":
                    content = item.read_text(encoding="utf-8")
                    content = substitute_values(content, replacements)
                    dst_path = dst_path.with_suffix("")
                    dst_path.write_text(content, encoding="utf-8")
                    print(f"Created: {dst_path.relative_to(ROOT_DIR)}")
                else:
                    shutil.copy2(item, dst_path)
                    print(f"Copied: {dst_path.relative_to(ROOT_DIR)}")


def run(
    github_username: str | None = None,
    project_name: str | None = None,
    project_description: str | None = None,
    author_name: str | None = None,
    author_email: str | None = None,
    yes: bool = False,
    dry_run: bool = False,
) -> None:
    """Run the setup script with provided parameters."""
    defaults = load_defaults()

    if yes or dry_run:
        github_username = github_username or defaults.get("github_username")
        project_name = project_name or defaults.get("project_name")
        project_description = project_description or defaults.get("project_description")
        author_name = author_name or defaults.get("author_name")
        author_email = author_email or defaults.get("author_email")

    interactive = (
        not yes
        and not dry_run
        and any(
            (val is None)
            for key, val in {
                "github_username": github_username,
                "project_name": project_name,
                "project_description": project_description,
                "author_name": author_name,
                "author_email": author_email,
            }.items()
        )
    )

    if interactive:
        print("\n--- Interactive Mode ---")
        print("Press Enter to accept default value shown in brackets\n")

        if not github_username:
            github_username = prompt_for_value(
                "GitHub Username", defaults.get("github_username")
            )
        if not project_name:
            project_name = prompt_for_value(
                "Project Name", defaults.get("project_name")
            )
        if not project_description:
            project_description = prompt_for_value(
                "Project Description", defaults.get("project_description")
            )
        if not author_name:
            author_name = prompt_for_value("Author Name", defaults.get("author_name"))
        if not author_email:
            author_email = prompt_for_value(
                "Author Email", defaults.get("author_email")
            )

    if not all(
        [github_username, project_name, project_description, author_name, author_email]
    ):
        print("Error: Missing required values", file=sys.stderr)
        sys.exit(1)

    today = datetime.now(timezone.utc).strftime("%Y%m%d")

    original_project = defaults.get("project_name", "python-project-template")
    original_desc = defaults.get(
        "project_description",
        "Python template with some awesome tools to quickstart any Python project",
    )
    original_user = defaults.get("github_username", "nullhack")
    original_author = defaults.get("author_name", "eol")
    original_email = defaults.get("author_email", "nullhack@users.noreply.github.com")

    replacements = {
        original_user: github_username,
        original_author: author_name,
        original_email: author_email,
        original_project: project_name,
        "0.1.20260411": f"0.1.{today}",
        original_desc: project_description,
    }

    print(f"\nSetting up project: {project_name}")
    print(f"Description: {project_description}")
    print(f"GitHub: github.com/{github_username}/{project_name}")
    print(f"Author: {author_name} <{author_email}>")
    print("")

    if dry_run:
        print("--- Dry Run: No files created ---")
        return

    process_templates(replacements)

    print("\nProject setup complete!")
    print("\nNext steps:")
    print("  1. Review and update templated files (README.md, AGENTS.md, etc.)")
    print("  2. Run: uv venv && uv pip install -e '.[dev]'")


def detect_fields() -> None:
    """Show what fields would need changing."""
    defaults = load_defaults()
    today = datetime.now(timezone.utc).strftime("%Y%m%d")
    print("\nTemplated fields in templates:")
    print("-" * 50)
    print(f"  1. GitHub Username: {defaults.get('github_username', 'N/A')}")
    print(f"  2. Project Name: {defaults.get('project_name', 'N/A')}")
    print(f"  3. Project Description: '{defaults.get('project_description', 'N/A')}'")
    print(f"  4. Author Name: {defaults.get('author_name', 'N/A')}")
    print(f"  5. Author Email: {defaults.get('author_email', 'N/A')}")
    print(f"  6. Version: starts with 0.1.{today}")


def main() -> None:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Setup a new Python project from the template.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )

    parser.add_argument(
        "--github-username",
        help="GitHub username or organization",
    )
    parser.add_argument(
        "--project-name",
        help="Project name",
    )
    parser.add_argument(
        "--project-description",
        help="Project description",
    )
    parser.add_argument(
        "--author-name",
        help="Author name",
    )
    parser.add_argument(
        "--author-email",
        help="Author email",
    )
    parser.add_argument(
        "-y",
        "--yes",
        action="store_true",
        help="Accept defaults for missing values (non-interactive)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without creating files",
    )
    parser.add_argument(
        "command",
        nargs="?",
        choices=["run", "detect-fields"],
        help="Command to run",
    )

    args = parser.parse_args()

    if args.command == "detect-fields":
        detect_fields()
        return

    if args.command == "run" or not args.command:
        run(
            github_username=args.github_username,
            project_name=args.project_name,
            project_description=args.project_description,
            author_name=args.author_name,
            author_email=args.author_email,
            yes=args.yes,
            dry_run=args.dry_run,
        )
        return

    parser.print_help()


if __name__ == "__main__":
    main()
