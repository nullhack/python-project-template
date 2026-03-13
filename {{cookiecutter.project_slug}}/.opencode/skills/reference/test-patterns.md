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
```python
from hypothesis import given, strategies as st

@given(st.emails())
def test_when_any_valid_email_provided_should_generate_valid_jwt(email):
    """Property test: any valid email should produce valid JWT."""
    auth_service = AuthService()
    token = auth_service.generate_token(email)
    decoded = auth_service.verify_token(token)
    assert decoded is not None
    assert decoded["email"] == email
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
