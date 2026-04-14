"""This file contains examples of how to write tests using pytest."""

import logging
import tomllib
from io import StringIO
from pathlib import Path
from typing import cast
from unittest.mock import patch

import pytest
from hypothesis import example, given
from hypothesis import strategies as st

from app import version as m
from main import ValidVerbosity, main


@pytest.mark.unit
def test_version_returns_string_from_pyproject() -> None:
    """3f2a1b4c-d5e6-7890-abcd-ef1234567890

    Given: pyproject.toml exists with a version field
    When: version() is called
    Then: The returned string matches the version in pyproject.toml
    """
    # Given
    pyproject_path = Path(__file__).parent.parent / "pyproject.toml"
    with Path(pyproject_path).open("rb") as f:
        expected = tomllib.load(f)["project"]["version"]
    # When
    result = m.version()
    # Then
    assert result == expected


@pytest.mark.unit
def test_version_logs_correct_message(caplog) -> None:
    """7a8b9c0d-e1f2-3456-bcde-f12345678901

    Given: pyproject.toml exists with a version field
    When: version() is called
    Then: An INFO log message in the format "Version: <version>" is emitted
    """
    # Given
    pyproject_path = Path(__file__).parent.parent / "pyproject.toml"
    with Path(pyproject_path).open("rb") as f:
        expected_version = tomllib.load(f)["project"]["version"]
    # When
    with caplog.at_level(logging.INFO):
        m.version()
    # Then
    assert f"Version: {expected_version}" in caplog.text


@pytest.mark.integration
@pytest.mark.slow
@example(verbosity="DEBUG")
@example(verbosity="INFO")
@given(verbosity=st.sampled_from(["DEBUG", "INFO"]))
def test_version_appears_in_logs_at_debug_and_info(
    verbosity: str,
) -> None:
    """a1b2c3d4-e5f6-7890-abcd-ef1234567890

    Given: A verbosity level of DEBUG or INFO is passed to main()
    When: main() is called
    Then: The version string appears in the log output
    """
    # Given
    pyproject_path = Path(__file__).parent.parent / "pyproject.toml"
    with Path(pyproject_path).open("rb") as f:
        expected_version = tomllib.load(f)["project"]["version"]
    expected_level = getattr(logging, verbosity.upper())
    log_stream = StringIO()
    handler = logging.StreamHandler(log_stream)
    handler.setLevel(expected_level)

    def mock_basic_config(**kwargs):
        logger = logging.getLogger("app")
        logger.handlers.clear()
        logger.addHandler(handler)
        logger.setLevel(kwargs.get("level", logging.INFO))

    # When
    with patch("main.logging.basicConfig", side_effect=mock_basic_config):
        main(cast(ValidVerbosity, verbosity))
    # Then
    log_output = log_stream.getvalue()
    assert f"Version: {expected_version}" in log_output, (
        f"Expected version message at {verbosity} level, but got output: {log_output!r}"
    )


@pytest.mark.integration
@pytest.mark.slow
@example(verbosity="WARNING")
@example(verbosity="ERROR")
@given(verbosity=st.sampled_from(["WARNING", "ERROR", "CRITICAL"]))
def test_version_absent_from_logs_at_warning_and_above(
    verbosity: str,
) -> None:
    """b2c3d4e5-f6a7-8901-bcde-f12345678901

    Given: A verbosity level of WARNING, ERROR, or CRITICAL is passed to main()
    When: main() is called
    Then: The version string does not appear in the log output
    """
    # Given
    pyproject_path = Path(__file__).parent.parent / "pyproject.toml"
    with Path(pyproject_path).open("rb") as f:
        expected_version = tomllib.load(f)["project"]["version"]
    expected_level = getattr(logging, verbosity.upper())
    log_stream = StringIO()
    handler = logging.StreamHandler(log_stream)
    handler.setLevel(expected_level)

    def mock_basic_config(**kwargs):
        logger = logging.getLogger("app")
        logger.handlers.clear()
        logger.addHandler(handler)
        logger.setLevel(kwargs.get("level", logging.INFO))

    # When
    with patch("main.logging.basicConfig", side_effect=mock_basic_config):
        main(cast(ValidVerbosity, verbosity))
    # Then
    log_output = log_stream.getvalue()
    assert f"Version: {expected_version}" not in log_output, (
        f"Expected no version messages at {verbosity} level, "
        f"but got output: {log_output!r}"
    )


@pytest.mark.unit
def test_invalid_verbosity_raises_value_error() -> None:
    """e5f6a7b8-c9d0-1234-defa-012345678903

    Given: An invalid verbosity string is passed to main()
    When: main() is called
    Then: A ValueError is raised with the invalid value and valid options listed
    """
    # Given
    invalid_verbosity = "INVALID_LEVEL"
    # When
    with pytest.raises(ValueError, match=r"Invalid verbosity level") as exc_info:
        main(cast(ValidVerbosity, invalid_verbosity))
    # Then
    error_message = str(exc_info.value)
    assert "Invalid verbosity level 'INVALID_LEVEL'" in error_message
    assert "Valid options: DEBUG, INFO, WARNING, ERROR, CRITICAL" in error_message
