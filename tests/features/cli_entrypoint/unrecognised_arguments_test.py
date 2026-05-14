"""Tests for unrecognised arguments story."""

import subprocess
import sys


def test_unrecognised_flag_exits_with_code_2() -> None:
    """
    Given: the application package is installed
    When: the user runs `python -m app --unknown-flag`
    Then: the process exits with code 2
    """
    result = subprocess.run(
        [sys.executable, "-m", "app", "--unknown-flag"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 2


def test_no_arguments_exits_with_code_0() -> None:
    """
    Given: the application package is installed
    When: the user runs `python -m app` with no arguments
    Then: the process exits with code 0
    """
    result = subprocess.run(
        [sys.executable, "-m", "app"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
