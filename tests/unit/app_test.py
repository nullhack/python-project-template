"""Unit tests for the application entry point."""

import pytest
from hypothesis import example, given
from hypothesis import strategies as st

from app.__main__ import main


@pytest.mark.unit
@given(verbosity=st.sampled_from(["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]))
@example(verbosity="INFO")
def test_app_main_runs_with_valid_verbosity(verbosity: str) -> None:
    """
    Given: A valid verbosity level string
    When: main() is called with that verbosity
    Then: It completes without raising an exception
    """
    main(verbosity)
