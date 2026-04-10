#!/usr/bin/env python3
"""
Setup Project Agent Implementation

This script provides the core template processing functionality for the @setup-project agent.
It processes template files with user-provided metadata to create a customized Python project.
"""

import os
import re
import shutil
import subprocess
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
import datetime


@dataclass
class ProjectMetadata:
    """Project configuration metadata collected from user."""

    project_name: str  # "My Awesome Project"
    project_slug: str  # "my-awesome-project"
    package_name: str  # "my_awesome_project"
    module_name: str  # "my_awesome_module"
    author_name: str  # "John Doe"
    author_email: str  # "john@example.com"
    github_username: str  # "johndoe"
    description: str  # "Brief project description"
    license: str = "MIT"
    version: Optional[str] = None  # Will be auto-generated if None


class ValidationError(Exception):
    """Raised when user input validation fails."""

    pass


class TemplateProcessor:
    """Handles template file processing and project initialization."""

    # Template placeholders to replace
    PLACEHOLDERS = {
        "PythonProjectTemplate": "project_name",
        "python-project-template": "project_slug",
        "python_project_template": "package_name",
        "python_module_template": "module_name",
        "USER_NAME": "author_name",
        "USER@EMAIL": "author_email",
        "GitHubUsername": "github_username",
        "ProjectDescription": "description",
        "YYYY-MM-DD": "current_date",
    }

    # Template files to process
    TEMPLATE_FILES = [
        "README.md.template",
        "TODO.md.template",
        "EPICS.md.template",
        "CHANGELOG.md.template",
    ]

    def __init__(self, project_root: Path):
        """Initialize with project root directory."""
        self.project_root = project_root
        self.backup_dir = project_root / ".setup_backup"

    def validate_metadata(self, metadata: ProjectMetadata) -> None:
        """Validate user-provided metadata."""

        # Project name validation (human-readable)
        if not metadata.project_name or len(metadata.project_name.strip()) == 0:
            raise ValidationError("Project name cannot be empty")
        if len(metadata.project_name) > 80:
            raise ValidationError("Project name too long (max 80 characters)")

        # Project slug validation (URL-safe)
        slug_pattern = r"^[a-z0-9]+(-[a-z0-9]+)*$"
        if not re.match(slug_pattern, metadata.project_slug):
            raise ValidationError(
                f"Project slug must be lowercase with hyphens (got: '{metadata.project_slug}')"
            )

        # Package name validation (Python identifier)
        package_pattern = r"^[a-z][a-z0-9_]*$"
        if not re.match(package_pattern, metadata.package_name):
            raise ValidationError(
                f"Package name must be lowercase with underscores (got: '{metadata.package_name}')"
            )

        # Module name validation (Python identifier)
        if not re.match(package_pattern, metadata.module_name):
            raise ValidationError(
                f"Module name must be lowercase with underscores (got: '{metadata.module_name}')"
            )

        # Email validation (basic)
        email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(email_pattern, metadata.author_email):
            raise ValidationError(
                f"Invalid email format (got: '{metadata.author_email}')"
            )

        # GitHub username validation
        github_pattern = r"^[a-zA-Z0-9]([a-zA-Z0-9-])*[a-zA-Z0-9]$"
        if not re.match(github_pattern, metadata.github_username):
            raise ValidationError(
                f"Invalid GitHub username format (got: '{metadata.github_username}')"
            )

        # Description validation
        if not metadata.description or len(metadata.description.strip()) == 0:
            raise ValidationError("Project description cannot be empty")

    def create_backup(self) -> None:
        """Create backup of original template files."""
        if self.backup_dir.exists():
            shutil.rmtree(self.backup_dir)
        self.backup_dir.mkdir(exist_ok=True)

        for template_file in self.TEMPLATE_FILES:
            template_path = self.project_root / template_file
            if template_path.exists():
                shutil.copy2(template_path, self.backup_dir)

    def restore_backup(self) -> None:
        """Restore template files from backup in case of error."""
        if not self.backup_dir.exists():
            return

        for template_file in self.TEMPLATE_FILES:
            backup_path = self.backup_dir / template_file
            if backup_path.exists():
                shutil.copy2(backup_path, self.project_root)

    def cleanup_backup(self) -> None:
        """Remove backup directory after successful completion."""
        if self.backup_dir.exists():
            shutil.rmtree(self.backup_dir)

    def process_templates(self, metadata: ProjectMetadata) -> None:
        """Process all template files with user metadata."""

        # Generate version if not provided
        if not metadata.version:
            today = datetime.date.today()
            metadata.version = f"0.1.{today.strftime('%Y%m%d')}"

        # Create replacement mapping
        replacements = {
            placeholder: getattr(metadata, attr)
            for placeholder, attr in self.PLACEHOLDERS.items()
            if hasattr(metadata, attr)
        }
        replacements["YYYY-MM-DD"] = datetime.date.today().strftime("%Y-%m-%d")

        # Process each template file
        for template_file in self.TEMPLATE_FILES:
            template_path = self.project_root / template_file
            output_path = self.project_root / template_file.replace(".template", "")

            if not template_path.exists():
                print(f"Warning: Template file not found: {template_file}")
                continue

            try:
                with open(template_path, "r", encoding="utf-8") as f:
                    content = f.read()

                # Apply replacements
                for placeholder, value in replacements.items():
                    content = content.replace(placeholder, value)

                # Write processed content
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(content)

                print(f"✓ Processed {template_file} → {output_path.name}")

            except Exception as e:
                raise RuntimeError(f"Failed to process {template_file}: {e}")

    def rename_package_directory(self, old_name: str, new_name: str) -> None:
        """Rename package directory and update import statements."""

        old_dir = self.project_root / old_name
        new_dir = self.project_root / new_name

        if not old_dir.exists():
            print(f"Warning: Package directory not found: {old_name}")
            return

        if new_dir.exists():
            raise RuntimeError(f"Target package directory already exists: {new_name}")

        try:
            # Rename directory
            shutil.move(str(old_dir), str(new_dir))
            print(f"✓ Renamed package directory: {old_name} → {new_name}")

            # Update import statements in Python files
            self._update_import_statements(old_name, new_name)

        except Exception as e:
            raise RuntimeError(f"Failed to rename package directory: {e}")

    def _update_import_statements(self, old_package: str, new_package: str) -> None:
        """Update import statements in Python files."""

        python_files = list(self.project_root.rglob("*.py"))

        for py_file in python_files:
            try:
                with open(py_file, "r", encoding="utf-8") as f:
                    content = f.read()

                # Replace import statements
                patterns = [
                    (f"from {old_package}", f"from {new_package}"),
                    (f"import {old_package}", f"import {new_package}"),
                    (f'"{old_package}"', f'"{new_package}"'),
                    (f"'{old_package}'", f"'{new_package}'"),
                ]

                updated = False
                for old_pattern, new_pattern in patterns:
                    if old_pattern in content:
                        content = content.replace(old_pattern, new_pattern)
                        updated = True

                if updated:
                    with open(py_file, "w", encoding="utf-8") as f:
                        f.write(content)
                    print(
                        f"✓ Updated imports in {py_file.relative_to(self.project_root)}"
                    )

            except Exception as e:
                print(f"Warning: Could not update imports in {py_file}: {e}")

    def initialize_git_repository(self) -> None:
        """Initialize fresh Git repository."""

        try:
            # Remove existing git repository if present
            git_dir = self.project_root / ".git"
            if git_dir.exists():
                shutil.rmtree(git_dir)

            # Initialize new repository
            subprocess.run(
                ["git", "init"],
                cwd=self.project_root,
                check=True,
                capture_output=True,
                text=True,
            )

            # Add all files
            subprocess.run(
                ["git", "add", "."],
                cwd=self.project_root,
                check=True,
                capture_output=True,
                text=True,
            )

            # Create initial commit
            subprocess.run(
                ["git", "commit", "-m", "Initial commit from template"],
                cwd=self.project_root,
                check=True,
                capture_output=True,
                text=True,
            )

            print("✓ Initialized Git repository with initial commit")

        except subprocess.CalledProcessError as e:
            print(f"Warning: Git initialization failed: {e}")
        except FileNotFoundError:
            print("Warning: Git not found, skipping repository initialization")

    def setup_development_environment(self) -> None:
        """Set up Python development environment."""

        try:
            # Create virtual environment
            subprocess.run(
                ["uv", "venv"],
                cwd=self.project_root,
                check=True,
                capture_output=True,
                text=True,
            )

            # Install dependencies
            subprocess.run(
                ["uv", "pip", "install", "-e", ".[dev]"],
                cwd=self.project_root,
                check=True,
                capture_output=True,
                text=True,
            )

            print("✓ Created virtual environment and installed dependencies")

        except subprocess.CalledProcessError as e:
            print(f"Warning: Environment setup failed: {e}")
        except FileNotFoundError:
            print("Warning: UV not found, skipping environment setup")

    def validate_setup(self) -> Tuple[bool, List[str]]:
        """Validate the completed project setup."""

        issues = []

        # Check that template variables were replaced
        for template_file in self.TEMPLATE_FILES:
            output_file = template_file.replace(".template", "")
            output_path = self.project_root / output_file

            if not output_path.exists():
                issues.append(f"Missing output file: {output_file}")
                continue

            try:
                with open(output_path, "r", encoding="utf-8") as f:
                    content = f.read()

                # Check for unreplaced placeholders
                for placeholder in self.PLACEHOLDERS.keys():
                    if placeholder in content and placeholder != "YYYY-MM-DD":
                        issues.append(
                            f"Unreplaced placeholder '{placeholder}' in {output_file}"
                        )

            except Exception as e:
                issues.append(f"Could not validate {output_file}: {e}")

        # Check that package was renamed
        if (self.project_root / "python_package_template").exists():
            issues.append("Package directory was not renamed")

        return len(issues) == 0, issues

    def setup_project(self, metadata: ProjectMetadata) -> None:
        """Complete project setup process."""

        print(f"🚀 Setting up project: {metadata.project_name}")
        print("-" * 50)

        try:
            # Validate input
            print("1. Validating metadata...")
            self.validate_metadata(metadata)
            print("   ✓ All metadata validated")

            # Create backup
            print("2. Creating backup...")
            self.create_backup()
            print("   ✓ Template files backed up")

            # Process templates
            print("3. Processing template files...")
            self.process_templates(metadata)
            print("   ✓ All templates processed")

            # Rename package
            print("4. Renaming package directory...")
            self.rename_package_directory(
                "python_package_template", metadata.package_name
            )
            print("   ✓ Package directory renamed")

            # Initialize Git
            print("5. Initializing Git repository...")
            self.initialize_git_repository()

            # Setup environment
            print("6. Setting up development environment...")
            self.setup_development_environment()

            # Validate setup
            print("7. Validating setup...")
            success, issues = self.validate_setup()

            if success:
                print("   ✓ Setup validation passed")
                self.cleanup_backup()
                print("\n🎉 Project setup completed successfully!")
                print(f"\nNext steps:")
                print(f"  cd {metadata.project_slug}")
                print(f"  task test && task lint")
                print(f"  @developer /skill session-workflow")
            else:
                print("   ❌ Setup validation failed:")
                for issue in issues:
                    print(f"     - {issue}")
                self.restore_backup()
                print("\n❌ Setup failed, template files restored")

        except Exception as e:
            print(f"\n❌ Setup failed: {e}")
            self.restore_backup()
            print("Template files restored from backup")
            raise


def main():
    """Example usage of the TemplateProcessor."""

    # Example metadata
    metadata = ProjectMetadata(
        project_name="My Awesome API",
        project_slug="my-awesome-api",
        package_name="my_awesome_api",
        module_name="api_core",
        author_name="John Doe",
        author_email="john.doe@example.com",
        github_username="johndoe",
        description="A powerful REST API for awesome things",
    )

    # Process templates
    processor = TemplateProcessor(Path("."))
    processor.setup_project(metadata)


if __name__ == "__main__":
    main()
