"""This file contains examples of how to write tests using pytest!

Some good practices for writting great Python tests:

Source: https://www.nerdwallet.com/blog/engineering/5-pytest-best-practices/

  *  Prefer mocker over mock
  *  Parametrize the same behavior, have different tests for different behaviors
  *  Don't modify fixture values in other fixtures
  *  Prefer responses over mocking outbound HTTP requests
  *  Prefer tmpdir over global test artifacts

BDD Test Convention:
  *  Use descriptive naming: test_<condition>_should_<outcome>
  *  All tests should have Given/When/Then docstrings

"""

from typing import Self

import pytest

from python_package_template import python_module_template as m


@pytest.mark.parametrize(
    ("param1", "param2"),
    [
        ("a", "b"),
        ("c", "d"),
    ],
)
class TestGroup:
    """A class with common parameters, `param1` and `param2`."""

    @pytest.fixture
    def fixt(self: Self) -> int:
        """This fixture will only be available within the scope of TestGroup.

        Returns:
            int: A common value to be used by multiple tests

        """
        return 123

    def test_one(self: Self, param1: str, param2: str, fixt: int) -> None:
        """
        Given: Two different string parameters
        When: Test executes
        Then: Parameters should not be equal
        """
        assert param1 != param2


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (1, 1, 1),
        (42, 1, 42),
        (84, 2, 42),
    ],
)
def test_divide_ok(a: float, b: float, expected: float) -> None:
    """
    Given: Valid division inputs
    When: Calculator.divide(a, b) is called
    Then: Should return expected result
    """
    assert m.Calculator.divide(a, b) == expected


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (42, "b", TypeError),
        ("a", 42, TypeError),
        (42, 0, ZeroDivisionError),
    ],
)
def test_divide_error(
    a: str | float, b: str | float, expected: float | Exception
) -> None:
    """
    Given: Invalid division inputs
    When: Calculator.divide(a, b) is called
    Then: Should raise expected Exception
    """
    with pytest.raises(expected):
        m.Calculator.divide(a, b)
