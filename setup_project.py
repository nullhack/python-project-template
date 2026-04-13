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
import os
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import TextIO

TEMPLATES_DIR = Path(__file__).parent / ".opencode" / "templates"
ROOT_DIR = Path(__file__).parent
DEFAULTS_FILE = ROOT_DIR / "project_defaults.json"


def log_message(message: str, file: TextIO | None = None) -> None:
    """Log message to stdout or stderr."""
    if file:
        file.write(f"{message}\n")
        file.flush()
    else:
        sys.stdout.write(f"{message}\n")
        sys.stdout.flush()


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
    return value or (default or "")


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
        log_message(f"Created: {dst_path.relative_to(ROOT_DIR)}")

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
                    log_message(f"Created: {dst_path.relative_to(ROOT_DIR)}")
                else:
                    shutil.copy2(item, dst_path)
                    log_message(f"Copied: {dst_path.relative_to(ROOT_DIR)}")


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
        log_message("\n--- Interactive Mode ---")
        log_message("Press Enter to accept default value shown in brackets\n")

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
        log_message("Error: Missing required values", file=sys.stderr)
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

    log_message(f"\nSetting up project: {project_name}")
    log_message(f"Description: {project_description}")
    log_message(f"GitHub: github.com/{github_username}/{project_name}")
    log_message(f"Author: {author_name} <{author_email}>")
    log_message("")

    if dry_run:
        log_message("--- Dry Run: No files created ---")
        return

    process_templates(replacements)

    # Rename parent folder based on project name
    rename_parent_folder(project_name)

    # Show Git configuration instructions
    show_git_setup_instructions(
        github_username, project_name, author_name, author_email
    )

    log_message("\nProject setup complete!")
    log_message("\nNext steps:")
    log_message("  1. Run the Git configuration commands shown above")
    log_message("  2. Review and update templated files (README.md, AGENTS.md, etc.)")
    log_message("  3. Run: uv venv && uv pip install -e '.[dev]'")


def show_git_setup_instructions(
    github_username: str, project_name: str, author_name: str, author_email: str
) -> None:
    """Show Git configuration instructions for manual setup."""
    new_remote_url = f"https://github.com/{github_username}/{project_name}.git"

    log_message("\n" + "=" * 60)
    log_message("Git Configuration Required")
    log_message("=" * 60)
    log_message("Please run the following Git commands to complete setup:")
    log_message("")
    log_message("# Configure Git user (repository-specific)")
    log_message(f'git config user.name "{author_name}"')
    log_message(f'git config user.email "{author_email}"')
    log_message("")
    log_message("# Update remote origin URL")
    log_message(f"git remote set-url origin {new_remote_url}")
    log_message("")
    log_message("# Or add origin if it doesn't exist")
    log_message(f"git remote add origin {new_remote_url}")
    log_message("")
    log_message("=" * 60)


def rename_parent_folder(project_name: str) -> None:
    """Rename the parent folder to match the project name."""
    current_dir = Path.cwd()
    parent_dir = current_dir.parent
    current_name = current_dir.name

    # Convert project name to a valid directory name
    safe_project_name = project_name.replace(" ", "-").lower()

    if current_name != safe_project_name:
        new_path = parent_dir / safe_project_name

        # Check if target directory already exists
        if new_path.exists():
            log_message(
                f"Warning: Directory '{safe_project_name}' already exists in parent."
            )
            log_message("Skipping parent folder rename.")
            return

        try:
            # Rename the current directory
            current_dir.rename(new_path)
            log_message(
                f"Renamed parent folder from '{current_name}' to '{safe_project_name}'"
            )

            # Change working directory to the new location
            os.chdir(new_path)
            log_message(f"Changed working directory to: {new_path}")

        except OSError as e:
            log_message(f"Warning: Could not rename parent folder: {e}")
            log_message("Continuing with setup in current directory.")
    else:
        log_message(
            f"Parent folder name '{current_name}' already matches project name."
        )


def detect_fields() -> None:
    """Show what fields would need changing."""
    defaults = load_defaults()
    today = datetime.now(timezone.utc).strftime("%Y%m%d")
    log_message("\nTemplated fields in templates:")
    log_message("-" * 50)
    log_message(f"  1. GitHub Username: {defaults.get('github_username', 'N/A')}")
    log_message(f"  2. Project Name: {defaults.get('project_name', 'N/A')}")
    log_message(
        f"  3. Project Description: '{defaults.get('project_description', 'N/A')}'"
    )
    log_message(f"  4. Author Name: {defaults.get('author_name', 'N/A')}")
    log_message(f"  5. Author Email: {defaults.get('author_email', 'N/A')}")
    log_message(f"  6. Version: starts with 0.1.{today}")


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
