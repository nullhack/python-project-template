# -*- coding: utf-8 -*-


"""This file contains examples of how to write tests using pytest!

Some good practices for writting great Python tests:

Source: https://www.nerdwallet.com/blog/engineering/5-pytest-best-practices/

  *  Prefer mocker over mock
  *  Parametrize the same behavior, have different tests for different behaviors
  *  Don’t modify fixture values in other fixtures
  *  Prefer responses over mocking outbound HTTP requests
  *  Prefer tmpdir over global test artifacts

"""

import pytest

from {{cookiecutter.package_name}} import {{cookiecutter.module_name}} as m


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
    def fixt(self):
        """This fixture will only be available within the scope of TestGroup.

        Returns:
            int: A common value to be used by multiple tests

        """
        return 123

    def test_one(self, param1, param2, fixt):
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
def test_divide_ok(a, b, expected):
    """Check if divide works for expected entries.

    Args:
        a (Real): Dividend.
        b (Real): Divisor.
        expected (Real): expected result.

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
def test_divide_error(a, b, expected):
    """Check if divide returns correct Exceptions for known entries.

    Issue raised by https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/issues/1337

    Args:
        a (Real): Dividend.
        b (Real): Divisor.
        expected (Exception): expected Exception.

    """
    with pytest.raises(expected):
        m.Calculator.divide(a, b)
