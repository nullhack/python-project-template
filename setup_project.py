#!/usr/bin/env python3
"""Setup a new Python project from the template.

This script copies template files from .opencode/templates/ to the project root,
substituting templated fields with the provided parameters.

Usage:
    python setup_project.py run --github-username <username> --project-name <name>
                              --project-description <desc> [--author-name <name>]
                              [--author-email <email>] [--package-name <name>]
                              [--module-name <name>]

    python setup_project.py detect-fields
"""

import logging
import shutil
import sys
from datetime import datetime
from pathlib import Path

import fire

# Configure logging for user feedback
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)

TEMPLATES_DIR = Path(__file__).parent / ".opencode" / "templates"
ROOT_DIR = Path(__file__).parent

ORIGINAL_PROJECT_NAME = "python-project-template"
ORIGINAL_PACKAGE_NAME = "python_package_template"
ORIGINAL_MODULE_NAME = "python_module_template"
ORIGINAL_GITHUB_USERNAME = "nullhack"
ORIGINAL_AUTHOR_NAME = "eol"
ORIGINAL_AUTHOR_EMAIL = "nullhack@users.noreply.github.com"


def substitute_values(content: str, replacements: dict) -> str:
    """Replace all values in content based on replacements dict."""
    result = content
    for original, replacement in replacements.items():
        result = result.replace(original, replacement)
    return result


def copy_and_rename_package(src_name: str, dst_name: str) -> None:
    """Copy package directory and rename references inside."""
    src_dir = ROOT_DIR / src_name
    dst_dir = ROOT_DIR / dst_name

    if src_dir.exists():
        if dst_dir.exists():
            shutil.rmtree(dst_dir)
        shutil.copytree(src_dir, dst_dir, dirs_exist_ok=True)
        logger.info("Copied package: %s -> %s", src_name, dst_name)

        for py_file in dst_dir.rglob("*.py"):
            content = py_file.read_text(encoding="utf-8")
            content = content.replace(src_name, dst_name)
            py_file.write_text(content, encoding="utf-8")
            logger.info("  Renamed in: %s", py_file.relative_to(ROOT_DIR))


def detect_fields() -> None:
    """Show what fields would need changing."""
    today = datetime.now().strftime("%Y%m%d")
    logger.info("\nFields that would need to be changed in templates:")
    logger.info("-" * 50)
    logger.info("  1. GitHub Username: %s", ORIGINAL_GITHUB_USERNAME)
    logger.info("  2. Project Name: %s", ORIGINAL_PROJECT_NAME)
    logger.info("  3. Project Description: 'Python template...'")
    logger.info("  4. Author Name: %s", ORIGINAL_AUTHOR_NAME)
    logger.info("  5. Author Email: %s", ORIGINAL_AUTHOR_EMAIL)
    logger.info("  6. Package Name: %s", ORIGINAL_PACKAGE_NAME)
    logger.info("  7. Module Name: %s", ORIGINAL_MODULE_NAME)
    logger.info("  8. Version: starts with 0.1.%s", today)


def copy_directory_structure(src_dir: Path, dst_dir: Path, replacements: dict) -> None:
    """Copy directory structure recursively, processing template files."""
    if dst_dir.exists():
        shutil.rmtree(dst_dir)
    dst_dir.mkdir(parents=True, exist_ok=True)

    for item in src_dir.rglob("*"):
        if item.is_file():
            # Calculate relative path and destination
            rel_path = item.relative_to(src_dir)
            dst_path = dst_dir / rel_path
            dst_path.parent.mkdir(parents=True, exist_ok=True)

            # Process template files
            if item.suffix == ".template":
                content = item.read_text(encoding="utf-8")
                content = substitute_values(content, replacements)
                # Remove .template extension
                dst_path = dst_path.with_suffix("")
                dst_path.write_text(content, encoding="utf-8")
                logger.info("Created: %s", dst_path.relative_to(ROOT_DIR))
            else:
                # Copy non-template files as-is
                shutil.copy2(item, dst_path)
                logger.info("Copied: %s", dst_path.relative_to(ROOT_DIR))


def run(
    github_username: str,
    project_name: str,
    project_description: str,
    author_name: str = "Your Name",
    author_email: str = "[EMAIL]",
    package_name: str = None,
    module_name: str = None,
) -> None:
    """Run the setup script with provided parameters."""
    if package_name is None:
        package_name = project_name.replace("-", "_")
    if module_name is None:
        module_name = package_name

    replacements = {
        ORIGINAL_GITHUB_USERNAME: github_username,
        ORIGINAL_AUTHOR_NAME: author_name,
        ORIGINAL_AUTHOR_EMAIL: author_email,
        ORIGINAL_PROJECT_NAME: project_name,
        ORIGINAL_PACKAGE_NAME: package_name,
        ORIGINAL_MODULE_NAME: module_name,
    }

    today = datetime.now().strftime("%Y%m%d")
    replacements["0.1.20260411"] = f"0.1.{today}"
    replacements[
        "Python template with some awesome tools to quickstart any Python project"
    ] = project_description

    logger.info("\nSetting up project: %s", project_name)
    logger.info("Description: %s", project_description)
    logger.info("GitHub: github.com/%s/%s", github_username, project_name)
    logger.info("Package: %s", package_name)
    logger.info("Module: %s", module_name)
    logger.info("")

    # Process root-level template files
    for template_file in TEMPLATES_DIR.glob("*.template"):
        content = template_file.read_text(encoding="utf-8")
        content = substitute_values(content, replacements)

        dst_name = template_file.stem
        dst_path = ROOT_DIR / dst_name
        dst_path.write_text(content, encoding="utf-8")
        logger.info("Created: %s", dst_path.relative_to(ROOT_DIR))

    # Process .github directory structure
    github_templates_dir = TEMPLATES_DIR / ".github"
    if github_templates_dir.exists():
        github_dst_dir = ROOT_DIR / ".github"
        copy_directory_structure(github_templates_dir, github_dst_dir, replacements)

    # Copy and rename package directory
    if package_name != ORIGINAL_PACKAGE_NAME:
        copy_and_rename_package(ORIGINAL_PACKAGE_NAME, package_name)

    logger.info("\nProject setup complete!")
    logger.info("\nNext steps:")
    logger.info("  1. Review and update README.md with project-specific content")
    logger.info("  2. Run: uv venv && uv pip install -e '.[dev]'")
    logger.info("  3. Run: task test && task lint && task static-check")
    logger.info(
        "  4. Initialize secrets baseline: uv run detect-secrets scan --baseline .secrets.baseline"
    )


if __name__ == "__main__":
    fire.Fire({"run": run, "detect-fields": detect_fields})
