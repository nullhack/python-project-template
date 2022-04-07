# -*- coding: utf-8 -*-

"""Module Docstring."""

import logging
from numbers import Real

# TODO({{cookiecutter.full_name}}): Check how to write todos!
# https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/issues/1337

logger = logging.getLogger("test")
logger.info("This is a {word}", extra={"word": "Log"})


class Calculator(object):
    """Class for simple calculator operations."""

    @staticmethod
    def divide(a: Real, b: Real) -> Real:
        """Divide a by b.

        Args:
            a (Real): Dividend.
            b (Real): Divisor.

        Returns:
            Real: The result of the division.

        Raises:
            ZeroDivisionError: if b is 0.
            TypeError: if a or b are not Real numbers.

        Examples:
            You can run this function as following.

            >>> Calculator.divide(2,1)
            2.0

        """
        if b == 0:
            raise ZeroDivisionError
        elif type(a) not in (Real, float, int) or type(b) not in (
            Real,
            float,
            int,
        ):
            print(type(a), type(b))
            raise TypeError
        return a / b


if __name__ == "__main__":
    print("RUNNING!")
