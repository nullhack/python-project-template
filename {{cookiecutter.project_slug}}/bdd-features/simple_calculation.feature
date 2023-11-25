{%- if cookiecutter.include_examples == "true" -%}
Feature: divide
    The user should be able to divide two numbers.

    Scenario Outline: Divide 'a' by 'b'
        Given I have two numbers <a> and <b>

        When I divide <a> by <b>

        Then I should see <output>

        Examples:
        |   a   |   b   | output |
        |  2.0  |  2.0  |  1.0   |
        |  6.0  |  2.0  |  3.0   |
        |  1.0  |  2.0  |  0.5   |
{% endif %}
