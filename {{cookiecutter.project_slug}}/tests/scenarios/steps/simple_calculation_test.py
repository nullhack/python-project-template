{%- if cookiecutter.include_examples == "true" -%}
"""Feature steps implementation.

This script defines three steps for a BDD test using pytest-bdd. The test scenario is described in the simple_calculation.feature file.

"""

from pytest_bdd import given, parsers, scenarios, then, when

from {{cookiecutter.package_name}}.{{cookiecutter.module_name}} import Calculator

scenarios("simple_calculation.feature")


@given(
    parsers.parse("I have two numbers {a:f} and {b:f}"), target_fixture="varl"
)
def given_numbers(a: float, b: float) -> dict:
    """Set the initial values for the calculator test.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        dict: A dictionary with keys "a" and "b" and their corresponding values.

    """
    return {"a": a, "b": b}


@when(parsers.parse("I divide {a:f} by {b:f}"))
def when_divide(varl: dict, a: float, b: float) -> None:
    """Perform a division operation using the calculator.

    Args:
        varl (dict): A dictionary with the initial values for the calculator.
        a (float): The dividend.
        b (float): The divisor.

    Returns:
        None
    """
    calc = Calculator()
    varl["output"] = calc.divide(varl["a"], varl["b"])


@then(parsers.parse("I should see {output:f}"))
def then_should_see(varl: dict, output: float) -> None:
    """Verify if the result of the operation matches the expected output.

    Args:
        varl (dict): A dictionary with the initial values for the calculator and the result of the operation.
        output (float): The expected output.

    Returns:
        None
    """
    assert varl["output"] == output
{%- elif cookiecutter.include_examples != "true" -%}
"""Feature steps implementation.

This script defines three steps for a BDD test using pytest-bdd. The test scenario is described in the simple_calculation.feature file.

"""{% endif %}
