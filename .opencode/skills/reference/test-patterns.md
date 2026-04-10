---
name: Test Patterns
description: Guidelines for writing tests with TDD approach
license: MIT
compatibility: opencode
metadata:
  audience: developers
  workflow: feature-development
---

## Test-Driven Development Patterns

### Test Naming Convention
Use descriptive names that explain the expected behavior:
```python
def test_when_[condition]_should_[expected_outcome]():
    """Test that describes behavior clearly."""
    pass

def test_given_[context]_when_[action]_then_[result]():
    """Test following Given-When-Then pattern."""
    pass
```

### Test Structure (AAA Pattern)

Organize each test with Arrange-Act-Assert:
```python
def test_when_valid_email_provided_should_return_jwt_token():
    """Test JWT generation with valid email."""
    # Arrange
    email = "user@example.com"
    auth_service = AuthService()
    
    # Act
    result = auth_service.generate_token(email)
    
    # Assert
    assert isinstance(result, str)
    assert len(result) > 0
    assert "." in result  # JWT has dots
```

### Test Categories and Markers
Use pytest markers to categorize tests:
```python
@pytest.mark.unit      # Unit tests
@pytest.mark.integration  # Integration tests  
@pytest.mark.smoke     # Smoke tests
@pytest.mark.property # Property-based tests
```

### Test File Organization
```
tests/
├── unit/
│   ├── test_auth_service.py
│   └── test_validators.py
├── integration/
│   ├── test_api_endpoints.py
│   └── test_database_operations.py
├── fixtures/
│   ├── conftest.py
│   └── sample_data.py
└── helpers/
    └── test_utilities.py
```

### Test Data Guidelines

**Embedding Data Directly in Tests**
- Copy test data from prototype runs directly into test files
- Use constants or fixtures defined in the test file itself
- Do NOT load from external prototype files

```python
# In test file - directly embedded:
API_RESPONSE_DATA = {"id": 1, "name": "Test", ...}

@pytest.fixture
def real_api_response():
    return API_RESPONSE_DATA
```

### Property-Based Testing with Hypothesis

#### When to use Hypothesis vs plain TDD

| Use plain TDD | Use Hypothesis |
|--------------|----------------|
| Side effects (DB, files, network) | Pure functions |
| Behavioral contracts ("when closed, ceases to exist") | Invariants over all valid inputs |
| Specific error messages | Round-trip properties |
| Integration between components | Algorithms, parsers, serializers |

**NEVER** use Hypothesis for side-effectful code — it is inefficient and produces flaky tests.

#### Basic property test
```python
from hypothesis import given, settings, strategies as st

@given(st.emails())
def test_when_any_valid_email_provided_should_generate_valid_jwt(email):
    """Property test: any valid email should produce valid JWT."""
    auth_service = AuthService()
    token = auth_service.generate_token(email)
    decoded = auth_service.verify_token(token)
    assert decoded is not None
    assert decoded["email"] == email
```

#### Settings profiles — match intensity to phase
```python
# Fast feedback during RED/GREEN cycle
@settings(max_examples=25, deadline=500)
@given(st.text(min_size=1))
def test_when_any_input_property_holds(value): ...

# Thorough check for CI / QA phase
@settings(max_examples=200, deadline=2000)
@given(st.text(min_size=1))
def test_when_any_input_property_holds_ci(value): ...
```

#### Composite strategies — build domain-valid objects
```python
from hypothesis import strategies as st

@st.composite
def valid_user_data(draw):
    """Generate valid user data that satisfies domain rules."""
    return {
        "email": draw(st.emails()),
        "name": draw(st.text(min_size=1, max_size=100,
                             alphabet=st.characters(blacklist_characters="\n\r\t"))),
        "age": draw(st.integers(min_value=13, max_value=120)),
    }

@given(valid_user_data())
def test_when_valid_user_data_provided_should_always_create_successfully(data):
    user = User.create(**data)
    assert user.email == data["email"]
```

#### Round-trip invariant — classic Hypothesis use case
```python
@given(st.builds(MyModel, name=st.text(min_size=1)))
def test_when_model_serialized_and_deserialized_should_be_equal(model):
    assert MyModel.from_dict(model.to_dict()) == model
```

#### Stateful testing — for state machines with interleaved operations
```python
from hypothesis.stateful import RuleBasedStateMachine, rule, initialize, invariant

class ConnectionMachine(RuleBasedStateMachine):
    """Explores all reachable connection state transitions."""

    @initialize()
    def setup(self):
        self.conn = Connection.open()

    @rule()
    def close(self):
        self.conn.close()

    @invariant()
    def closed_connection_is_inactive(self):
        if self.conn.is_closed():
            assert not self.conn.is_active()

TestConnectionLifecycle = ConnectionMachine.TestCase
```

### Test Fixtures and Factories
```python
@pytest.fixture
def valid_user_data():
    """Standard valid user for testing."""
    return {
        "email": "test@example.com",
        "name": "Test User",
        "created_at": datetime.utcnow()
    }

class UserFactory:
    """Factory for creating test users."""
    
    @staticmethod
    def create_valid_user(**overrides):
        defaults = {"email": "user@example.com", "name": "Test User", "active": True}
        defaults.update(overrides)
        return User(**defaults)
```

### Red-Green-Refactor Cycle

1. **RED** - Write failing test first
2. **GREEN** - Make test pass with minimal code
3. **REFACTOR** - Clean up code while keeping tests green

### Coverage and Quality Requirements

- All public methods should have tests
- Coverage must meet project minimum (e.g., 80%)
- Use property-based testing for robustness

### Anti-Patterns to Avoid

- ❌ Loading test data from prototype files
- ❌ Referencing prototype directory in tests
- ❌ Complex setup in fixtures (keep simple)
- ❌ Testing multiple things in one test

### Best Practices

- ✅ One assertion per test (or few closely related)
- ✅ Descriptive test names explain intent
- ✅ Test data embedded directly in test file
- ✅ Use property-based tests for edge cases
- ✅ Follow AAA pattern consistently
