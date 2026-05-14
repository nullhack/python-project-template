"""Tests for help output story."""

import importlib.metadata
import subprocess
import sys


def test_help_output_contains_app_name_and_tagline() -> None:
    """
    Given: the application package is installed
    When: the user runs `python -m app --help`
    Then: the output contains the application name "temple8"
    And: the output contains the tagline
    And: the process exits with code 0
    """
    tagline = importlib.metadata.metadata("temple8")["Summary"]
    result = subprocess.run(
        [sys.executable, "-m", "app", "--help"],
        capture_output=True,
        text=True,
    )
    assert "temple8" in result.stdout
    assert " ".join(tagline.split()) in " ".join(result.stdout.split())
    assert result.returncode == 0


def test_help_output_lists_help_and_version_flags() -> None:
    """
    Given: the application package is installed
    When: the user runs `python -m app --help`
    Then: the output contains "--help"
    And: the output contains "--version"
    """
    result = subprocess.run(
        [sys.executable, "-m", "app", "--help"],
        capture_output=True,
        text=True,
    )
    assert "--help" in result.stdout
    assert "--version" in result.stdout
