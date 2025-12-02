{%- if cookiecutter.include_examples == "true" -%}from hypothesis import given, example, strategies as st
import math

from {{cookiecutter.package_name}} import {{cookiecutter.module_name}} as m


@example(a=6, b=3)      # result = 2
@example(a=-8, b=2)     # result = -4
@example(a=0, b=5)      # zero dividend
@example(a=579, b=9105) # the earlier failing example (float rounding)
@given(
    a=st.integers(min_value=-10_000, max_value=10_000),
    b=st.integers(min_value=-10_000, max_value=10_000).filter(lambda x: x != 0),
)
def test_divide_inverse(a: int, b: int) -> None:
    """Check that multiplication is the inverse of division (within float tolerance)."""
    result = m.Calculator.divide(a, b)

    assert math.isclose(result * b, a, rel_tol=1e-12, abs_tol=1e-12)
{% endif %}
