---
name: code-quality
description: Enforce code quality using ruff, pytest coverage, hypothesis, and static type checking
license: MIT
compatibility: opencode
metadata:
  audience: developers
  workflow: feature-development
---
## What I do
Ensure code quality through automated tools including ruff linting/formatting, pytest coverage analysis, hypothesis property testing, and static type checking with pyright.

## When to use me
Use this after each implementation step and before final feature completion to maintain high code quality standards.

## Code Quality Tools

### 1. Ruff Linting and Formatting
```bash
# Check and fix code style issues
task lint

# Individual commands:
task ruff-check  # Check for linting issues and auto-fix
task ruff-format # Format code according to standards
```

#### Ruff Configuration (from pyproject.toml)
```toml
[tool.ruff.lint]
select = [
  "A",     # flake8-builtins
  "ANN",   # flake8-annotations  
  "ASYNC", # flake8-async
  "B",     # flake8-bugbear
  "C4",    # flake8-comprehensions
  "C9",    # mccabe complexity
  "D",     # pydocstyle
  "DTZ",   # flake8-datetimez
  "E",     # pycodestyle errors
  "ERA",   # eradicate
  "F",     # pyflakes
  "FURB",  # refurb
  "G",     # flake8-logging-format
  "I",     # isort
  "ICN",   # flake8-import-conventions
  "LOG",   # flake8-logging
  "N",     # pep8-naming
  "NPY",   # numpy
  "PD",    # pandas-vet
  "PT",    # flake8-pytest-style
  "PTH",   # flake8-use-pathlib
  "R",     # refactor
  "RUF",   # ruff-specific
  "S",     # flake8-bandit
  "SIM",   # flake8-simplify
  "T20",   # flake8-print
  "TD",    # flake8-todos
  "W",     # pycodestyle warnings
]
preview = true
mccabe.max-complexity = 10
pydocstyle.convention = "google"
```

### 2. Test Coverage with Pytest
```bash
# Run tests with coverage report
task test

# Generate detailed coverage report  
task test-report

# Coverage files generated:
# - docs/htmlcov/index.html (HTML report)
# - Terminal output with skip-covered option
```

#### Coverage Requirements
- Minimum coverage: {{cookiecutter.minimum_coverage}}%
- Excludes: pragma no cover, debug code, __repr__, assertions
- Fails build if coverage drops below minimum

#### Test Markers and Organization
```python
# Available test markers:
@pytest.mark.unit          # Unit tests
@pytest.mark.integration   # Integration tests  
@pytest.mark.system        # System tests
@pytest.mark.acceptance    # Acceptance tests
@pytest.mark.regression    # Regression tests
@pytest.mark.smoke         # Smoke tests
@pytest.mark.sanity        # Sanity tests
@pytest.mark.performance   # Performance tests
@pytest.mark.security      # Security tests
@pytest.mark.slow          # Slow tests (can skip with -m "not slow")
```

### 3. Hypothesis Property-Based Testing
```python
from hypothesis import given, strategies as st, settings
from hypothesis import HealthCheck

# Property-based testing for robust validation
@given(st.emails())
@settings(max_examples=100)
def test_email_validation_property(email):
    """Property: all valid emails should pass validation."""
    validator = EmailValidator()
    result = validator.is_valid(email)
    assert isinstance(result, bool)

@given(st.text(min_size=1, max_size=1000))
def test_sanitizer_properties(input_text):
    """Property: sanitizer should always return safe strings."""
    sanitizer = TextSanitizer()
    result = sanitizer.clean(input_text)
    
    # Properties that should always hold
    assert isinstance(result, str)
    assert len(result) <= len(input_text)
    assert "<script>" not in result.lower()

# Common strategies for domain objects
@st.composite
def valid_user_data(draw):
    """Generate valid user data for testing."""
    return {
        "email": draw(st.emails()),
        "name": draw(st.text(min_size=1, max_size=100, alphabet=st.characters(blacklist_characters="\n\r\t"))),
        "age": draw(st.integers(min_value=13, max_value=120))
    }

@given(valid_user_data())
def test_user_creation_properties(user_data):
    """Property: valid user data should always create user successfully."""
    user = User.create(user_data)
    assert user.email == user_data["email"]
    assert user.name == user_data["name"]
```

### 4. Static Type Checking with Pyright
```bash
# Run type checking
task static-check

# Direct pyright command
pyright
```

#### Type Checking Standards
- All functions must have type hints
- Return types must be specified
- Use modern typing (dict[str, Any] not Dict[str, Any])
- Protocol-based interfaces preferred
- Generic types where appropriate

```python
# Good type hints
def process_data(
    items: list[dict[str, Any]], 
    processor: Callable[[dict[str, Any]], str]
) -> dict[str, list[str]]:
    """Process items using provided processor function."""
    ...

# Protocol usage
class DataProcessor(Protocol):
    def process(self, data: dict[str, Any]) -> str: ...

def handle_data(processor: DataProcessor) -> None:
    """Accept any object implementing DataProcessor protocol."""
    ...
```

### 5. Mutation Testing with Cosmic Ray
```bash
# Run mutation testing (optional, resource-intensive)
task mut-report

# Generates: docs/mut_report.html
```

Mutation testing validates test quality by introducing bugs and checking if tests catch them.

### 6. Quality Gates and Automation

#### Pre-commit Quality Checks
```bash
#!/bin/bash
# Quality gate script - all must pass

echo "🔍 Running linting..."
task ruff-check || exit 1

echo "🎨 Running formatting..."
task ruff-format || exit 1

echo "🔧 Running type checking..."
task static-check || exit 1

echo "🧪 Running tests with coverage..."
task test || exit 1

echo "✅ All quality checks passed!"
```

#### CI/CD Quality Pipeline
```yaml
# .github/workflows/quality.yaml
name: Code Quality

on: [push, pull_request]

jobs:
  quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v4
        with:
          python-version: '3.13'
      
      - name: Install dependencies
        run: |
          pip install uv
          uv pip install '.[dev]'
      
      - name: Lint with ruff
        run: task ruff-check
      
      - name: Check formatting
        run: task ruff-format --check
      
      - name: Type checking
        run: task static-check
      
      - name: Test with coverage
        run: task test
      
      - name: Upload coverage
        uses: codecov/codecov-action@v3
```

### 7. Code Quality Metrics

#### Complexity Limits
- Maximum cyclomatic complexity: 10
- Maximum function length: 20 lines
- Maximum class length: 50 lines
- Maximum file length: 500 lines

#### Documentation Requirements
- All public functions must have docstrings
- Google docstring format required
- Type hints on all signatures
- Examples in docstrings for complex functions

#### Test Quality Metrics
- Line coverage: {{cookiecutter.minimum_coverage}}%
- Branch coverage: >90%
- Mutation score: >80% (when mutation testing enabled)
- Test-to-code ratio: >1:1

### 8. Quality Issue Resolution

#### Common Ruff Issues and Fixes
```python
# Issue: ANN001 - Missing type hint for function argument
def bad_function(name):  # ❌
    return f"Hello {name}"

def good_function(name: str) -> str:  # ✅
    return f"Hello {name}"

# Issue: S101 - Use of assert detected
def validate_data(data):
    assert data is not None  # ❌ (except in tests)
    
def validate_data(data: Any) -> None:
    if data is None:  # ✅
        raise ValueError("Data cannot be None")

# Issue: C901 - Function is too complex
def complex_function(data):  # ❌ High complexity
    if condition1:
        if condition2:
            if condition3:
                # ... deeply nested logic
                
def simple_function(data):  # ✅ Extract methods
    if not self._is_valid_input(data):
        return None
    
    processed = self._preprocess(data)
    return self._transform(processed)
```

#### Coverage Issues and Solutions
```python
# Low coverage - missing edge cases
def divide(a: float, b: float) -> float:
    return a / b  # ❌ No zero division handling

def divide(a: float, b: float) -> float:  # ✅ Complete coverage
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

# Test for complete coverage
def test_divide_with_zero_should_raise_error():
    with pytest.raises(ZeroDivisionError):
        divide(10.0, 0.0)

def test_divide_with_valid_numbers_should_return_quotient():
    result = divide(10.0, 2.0)
    assert result == 5.0
```

### 9. Quality Enforcement Checklist

✅ **Before committing:**
- [ ] `task lint` passes without errors
- [ ] `task static-check` passes without errors  
- [ ] `task test` passes with required coverage
- [ ] All new code has type hints
- [ ] All new functions have docstrings
- [ ] Complex logic has property-based tests

✅ **Before merging:**
- [ ] All CI quality checks pass
- [ ] Coverage hasn't decreased
- [ ] No new high-complexity functions
- [ ] Documentation is updated
- [ ] Integration tests pass

✅ **Periodic quality review:**
- [ ] Run mutation testing
- [ ] Review complexity trends
- [ ] Update test strategies
- [ ] Refactor complex code
- [ ] Update quality standards