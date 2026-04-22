"""Tests for version output story."""

import pytest


@pytest.mark.skip(reason="not yet implemented")
def test_cli_entrypoint_c9d0e1f2() -> None:
    """
    Given: the application package is installed
    When: the user runs `python -m app --version`
    Then: the output contains "temple8"
    And: the output contains the version string from package metadata
    And: the process exits with code 0
    """
    raise NotImplementedError


@pytest.mark.skip(reason="not yet implemented")
def test_cli_entrypoint_a3b4c5d6() -> None:
    """
    Given: the application package is installed
    When: the user runs `python -m app --version`
    Then: the version in the output matches `importlib.metadata.version("temple8")`
    """
    raise NotImplementedError

