{%- if cookiecutter.include_examples == "true" -%}
"""Module Docstring."""

import logging

# TODO({{cookiecutter.full_name}}): Check how to write todos!
# https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/issues/1337

logger = logging.getLogger("{{cookiecutter.module_name}}")
logger.info("This is a {word}", extra={"word": "Log"})


class Calculator:
    """Class for simple calculator operations."""

    @staticmethod
    def divide(a: float, b: float) -> float:
        """Divide a by b.

        Args:
            a (float): Dividend.
            b (float): Divisor.

        Returns:
            float: The result of the division.

        Raises:
            ZeroDivisionError: if b is 0.
            TypeError: if a or b are not float numbers.

        Examples:
            You can run this function as following.

            >>> Calculator.divide(2,1)
            2.0

        """
        if b == 0:
            raise ZeroDivisionError
        elif type(a) not in (float, int) or type(b) not in (float, int):
            raise TypeError
        return a / b


if __name__ == "__main__":
    print("RUNNING!")
{%- elif cookiecutter.include_examples != "true" -%}
"""Module Docstring."""

import logging

logger = logging.getLogger("{{cookiecutter.module_name}}")


if __name__ == "__main__":
    print("RUNNING!"){% endif %}
