"""This file contains examples of how to write tests using pytest."""

import logging
import tomllib
from pathlib import Path
from typing import cast
from unittest.mock import patch

import pytest
from hypothesis import assume, example, given
from hypothesis import strategies as st

from app import version as m
from main import ValidVerbosity, main


@pytest.mark.unit
def test_version_called_should_return_correct_string() -> None:
    """
    Given: pyproject.toml exists with version
    When: version() is called
    Then: Should return version string from pyproject.toml
    """
    # Read expected version from same source
    pyproject_path = Path(__file__).parent.parent / "pyproject.toml"
    with Path(pyproject_path).open("rb") as f:
        expected = tomllib.load(f)["project"]["version"]

    result = m.version()
    assert result == expected


@pytest.mark.unit
def test_version_called_should_log_correct_message(caplog) -> None:
    """
    Given: pyproject.toml exists with version
    When: version() is called
    Then: Should log the exact version message format
    """
    # Read expected version from same source
    pyproject_path = Path(__file__).parent.parent / "pyproject.toml"
    with Path(pyproject_path).open("rb") as f:
        expected_version = tomllib.load(f)["project"]["version"]

    # Capture logs at INFO level
    with caplog.at_level(logging.INFO):
        result = m.version()

    # Verify the exact log message format
    assert f"Version: {expected_version}" in caplog.text
    assert result == expected_version


@pytest.mark.system
@example(verbosity="DEBUG")
@example(verbosity="INFO")
@given(verbosity=st.sampled_from(["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]))
def test_main_with_verbosity_level_should_control_version_output(
    verbosity: str,
) -> None:
    """
    Given: Different verbosity levels
    When: main() is called with that verbosity
    Then: Version should appear in logs for DEBUG and INFO levels,
          but not for WARNING and above
    """
    assume(verbosity != "CRITICAL")

    # Read expected version dynamically
    pyproject_path = Path(__file__).parent.parent / "pyproject.toml"
    with Path(pyproject_path).open("rb") as f:
        expected_version = tomllib.load(f)["project"]["version"]

    expected_level = getattr(logging, verbosity.upper())

    # Create a custom logger handler to capture messages instead of using caplog
    from io import StringIO

    log_stream = StringIO()
    handler = logging.StreamHandler(log_stream)
    handler.setLevel(expected_level)

    # Mock logging.basicConfig to use our custom handler instead
    def mock_basic_config(**kwargs):
        # Set up the logger with our custom handler for testing
        logger = logging.getLogger("app")
        logger.handlers.clear()
        logger.addHandler(handler)
        logger.setLevel(kwargs.get("level", logging.INFO))

    with patch(
        "main.logging.basicConfig", side_effect=mock_basic_config
    ) as mock_basic_config:
        # Call main() directly with the verbosity level (cast to satisfy type checker)
        main(cast(ValidVerbosity, verbosity))

        # Verify that logging.basicConfig was called with the correct level
        mock_basic_config.assert_called_once()
        _args, kwargs = mock_basic_config.call_args
        assert kwargs["level"] == expected_level

    # Check the captured log output
    log_output = log_stream.getvalue()

    # Standard logging behavior: DEBUG and INFO levels should show INFO messages
    # WARNING, ERROR, CRITICAL levels should NOT show INFO messages
    if verbosity in ["WARNING", "ERROR", "CRITICAL"]:
        # These levels should NOT show INFO messages since INFO < WARNING/ERROR/CRITICAL
        assert f"Version: {expected_version}" not in log_output, (
            f"Expected no version messages at {verbosity} level, "
            f"but got output: {log_output!r}"
        )
    else:
        # DEBUG and INFO levels should show INFO messages
        # since INFO >= DEBUG and INFO >= INFO
        assert f"Version: {expected_version}" in log_output, (
            f"Expected version message at {verbosity} level, "
            f"but got output: {log_output!r}"
        )


@pytest.mark.unit
def test_main_with_invalid_verbosity_should_raise_value_error() -> None:
    """
    Given: An invalid verbosity level
    When: main() is called with invalid verbosity
    Then: Should raise ValueError with helpful message
    """
    # Test that calling main() with invalid verbosity raises ValueError
    # Use cast to bypass type checking for this intentionally invalid test
    with pytest.raises(ValueError, match=r"Invalid verbosity level") as exc_info:
        main(cast(ValidVerbosity, "INVALID_LEVEL"))  # type: ignore[arg-type]

    # Verify the error message contains expected details
    error_message = str(exc_info.value)
    assert "Invalid verbosity level 'INVALID_LEVEL'" in error_message
    assert "Valid options: DEBUG, INFO, WARNING, ERROR, CRITICAL" in error_message
