{%- if cookiecutter.include_examples == "true" -%}"""This file contains examples of how to write tests using pytest!

Some good practices for writting great Python tests:

Source: https://www.nerdwallet.com/blog/engineering/5-pytest-best-practices/

  *  Prefer mocker over mock
  *  Parametrize the same behavior, have different tests for different behaviors
  *  Don’t modify fixture values in other fixtures
  *  Prefer responses over mocking outbound HTTP requests
  *  Prefer tmpdir over global test artifacts

"""
from typing import TypeVar

import pytest

from {{cookiecutter.package_name}} import {{cookiecutter.module_name}} as m

Self = TypeVar("Self", bound="TestGroup")


@pytest.mark.parametrize(
    ("param1", "param2"),
    [
        ("a", "b"),
        ("c", "d"),
    ],
)
class TestGroup:
    """A class with common parameters, `param1` and `param2`."""

    @pytest.fixture()
    def fixt(self: Self) -> int:
        """This fixture will only be available within the scope of TestGroup.

        Returns:
            int: A common value to be used by multiple tests

        """
        return 123

    def test_one(self: Self, param1: str, param2: str, fixt: int) -> None:
        """Run the first test using the fixture.

        Args:
            param1 (str): First parameter.
            param2 (str): Second parameter.
            fixt (int): Value from fixture.

        """
        print("\ntest_one", param1, param2, fixt)


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (1, 1, 1),
        (42, 1, 42),
        (84, 2, 42),
    ],
)
def test_divide_ok(a: float, b: float, expected: float) -> None:
    """Check if divide works for expected entries.

    Args:
        a (float): Dividend.
        b (float): Divisor.
        expected (float): expected result.

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
    """Check if divide returns correct Exceptions for known entries.

    Issue raised by https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/issues/1337

    Args:
        a (float): Dividend.
        b (float): Divisor.
        expected (Exception): expected Exception.

    """
    with pytest.raises(expected):
        m.Calculator.divide(a, b)
{%- elif cookiecutter.include_examples != "true" -%}
"""Pytest test module."""


def test_basics() -> None:
    """A test that is always True."""
    assert True is True

{% endif %}
