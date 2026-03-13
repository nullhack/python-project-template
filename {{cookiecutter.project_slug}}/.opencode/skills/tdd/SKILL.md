---
name: tdd
description: Implement Test-Driven Development with descriptive naming conventions and pytest best practices
license: MIT
compatibility: opencode
metadata:
  audience: developers
  workflow: feature-development
---
## What I do
Guide the creation of tests using TDD methodology with descriptive naming conventions, using pytest, coverage, and hypothesis for robust testing.

## When to use me
Use this after prototype validation to create comprehensive tests before implementing the actual feature code.

## TDD Process

### 1. Test Naming Convention
```python
def test_when_[condition]_should_[expected_outcome]():
    """Test that describes behavior clearly."""
    pass

def test_given_[context]_when_[action]_then_[result]():
    """Test following Given-When-Then pattern."""
    pass
```

### 2. Test Structure (AAA Pattern)
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

### 3. Test Categories and Markers
Use pytest markers to categorize tests:
```python
import pytest

@pytest.mark.unit
def test_when_email_is_valid_should_pass_validation():
    """Unit test for email validation."""
    pass

@pytest.mark.integration 
def test_when_api_called_should_return_expected_response():
    """Integration test for API endpoint."""
    pass

@pytest.mark.smoke
def test_when_system_starts_should_be_responsive():
    """Smoke test for basic functionality."""
    pass
```

### 4. Test File Organization
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

### 5. Using Real Data from Prototypes
```python
import json
from pathlib import Path

class TestDataLoader:
    """Load real data captured from prototypes."""
    
    @staticmethod
    def load_prototype_data(filename: str):
        """Load data from prototype testing."""
        data_file = Path("prototypes") / "sample_responses" / filename
        if data_file.exists():
            with open(data_file) as f:
                return json.load(f)
        return {}

@pytest.fixture
def real_api_response():
    """Real API response from prototype testing."""
    return TestDataLoader.load_prototype_data("api_response.json")

def test_when_parsing_real_api_response_should_extract_correct_fields(real_api_response):
    """Test with actual API data structure."""
    parser = ApiResponseParser()
    
    result = parser.parse(real_api_response)
    
    assert "id" in result
    assert "name" in result
    assert isinstance(result["id"], int)
```

### 6. Hypothesis Property-Based Testing
```python
from hypothesis import given, strategies as st

@given(st.emails())
def test_when_any_valid_email_provided_should_generate_valid_jwt(email):
    """Property test: any valid email should produce valid JWT."""
    auth_service = AuthService()
    
    token = auth_service.generate_token(email)
    
    # Property: all tokens should be decodable
    decoded = auth_service.verify_token(token)
    assert decoded is not None
    assert decoded["email"] == email

@given(st.text(min_size=1, max_size=100))
def test_when_any_text_provided_to_sanitizer_should_return_safe_string(input_text):
    """Property test: sanitizer should handle any text safely."""
    sanitizer = TextSanitizer()
    
    result = sanitizer.clean(input_text)
    
    # Properties that should always hold
    assert isinstance(result, str)
    assert len(result) <= len(input_text)  # Should not grow
    assert "<script>" not in result.lower()  # Should remove dangerous content
```

### 7. Test Fixtures and Factories
```python
# conftest.py
import pytest
from datetime import datetime, timedelta

@pytest.fixture
def valid_user_data():
    """Standard valid user for testing."""
    return {
        "email": "test@example.com",
        "name": "Test User",
        "created_at": datetime.utcnow()
    }

@pytest.fixture  
def auth_service():
    """Configured auth service instance."""
    return AuthService(secret_key="test_secret_key")

class UserFactory:
    """Factory for creating test users."""
    
    @staticmethod
    def create_valid_user(**overrides):
        defaults = {
            "email": "user@example.com",
            "name": "Test User",
            "active": True
        }
        defaults.update(overrides)
        return User(**defaults)
    
    @staticmethod
    def create_expired_user():
        return UserFactory.create_valid_user(
            created_at=datetime.utcnow() - timedelta(days=365)
        )
```

### 8. Coverage and Quality Requirements
```python
# Test that ensures coverage targets are met
def test_coverage_meets_requirements():
    """Verify test coverage meets project standards."""
    # This test runs coverage analysis
    # Fails if coverage < {{cookiecutter.minimum_coverage}}%
    pass

def test_all_public_methods_have_tests():
    """Ensure all public methods are tested."""
    # Use inspection to verify all public methods have corresponding tests
    pass
```

### 9. TDD Red-Green-Refactor Cycle
```python
# Step 1: RED - Write failing test first
def test_when_invalid_email_provided_should_raise_validation_error():
    """Test that invalid email raises proper error."""
    auth_service = AuthService()
    
    with pytest.raises(ValidationError) as exc_info:
        auth_service.generate_token("invalid-email")
    
    assert "Invalid email format" in str(exc_info.value)

# Step 2: GREEN - Make test pass with minimal code
# Implement just enough to pass the test

# Step 3: REFACTOR - Clean up code while keeping tests green
# Improve implementation without changing behavior
```

### 10. Test Documentation
```python
class TestAuthService:
    """Test suite for authentication service.
    
    Tests cover:
    - Token generation with valid inputs
    - Token validation and expiration
    - Error handling for invalid inputs
    - Edge cases and boundary conditions
    """
    
    def test_when_valid_credentials_provided_should_return_jwt_token(self):
        """
        Given: A valid email address
        When: generate_token is called
        Then: A valid JWT token should be returned
        
        This test validates the core authentication flow.
        """
        pass
```

## Example Complete Test Suite
```python
"""
Tests for user authentication feature.
Following TDD approach with real prototype data.
"""
import pytest
import json
from datetime import datetime, timedelta
from hypothesis import given, strategies as st
from pathlib import Path

from {{cookiecutter.package_name}}.auth import AuthService, ValidationError

class TestAuthService:
    """Authentication service test suite."""
    
    @pytest.fixture
    def auth_service(self):
        """Configured auth service for testing."""
        return AuthService(secret_key="test_key_for_testing")
    
    @pytest.fixture
    def prototype_jwt_data(self):
        """Real JWT data from prototype testing."""
        data_file = Path("prototypes/jwt_prototype_results.json")
        if data_file.exists():
            with open(data_file) as f:
                return json.load(f)
        return {}
    
    @pytest.mark.unit
    def test_when_valid_email_provided_should_return_jwt_token(self, auth_service):
        """Test JWT generation with valid email."""
        # Arrange
        email = "user@example.com"
        
        # Act
        token = auth_service.generate_token(email)
        
        # Assert
        assert isinstance(token, str)
        assert len(token) > 0
        assert token.count('.') == 2  # JWT structure: header.payload.signature
    
    @pytest.mark.unit
    def test_when_invalid_email_provided_should_raise_validation_error(self, auth_service):
        """Test that invalid email raises proper error."""
        # Arrange
        invalid_email = "not-an-email"
        
        # Act & Assert
        with pytest.raises(ValidationError) as exc_info:
            auth_service.generate_token(invalid_email)
        
        assert "Invalid email format" in str(exc_info.value)
    
    @pytest.mark.unit
    def test_when_valid_token_provided_should_return_decoded_payload(self, auth_service):
        """Test JWT verification with valid token."""
        # Arrange
        email = "test@example.com"
        token = auth_service.generate_token(email)
        
        # Act
        payload = auth_service.verify_token(token)
        
        # Assert
        assert payload is not None
        assert payload["email"] == email
        assert "exp" in payload
        assert "iat" in payload
    
    @pytest.mark.integration
    def test_when_using_prototype_data_should_match_expected_structure(
        self, auth_service, prototype_jwt_data
    ):
        """Test that implementation matches prototype results."""
        if not prototype_jwt_data:
            pytest.skip("No prototype data available")
        
        # Arrange
        test_email = prototype_jwt_data["input_email"]
        
        # Act
        token = auth_service.generate_token(test_email)
        decoded = auth_service.verify_token(token)
        
        # Assert - structure should match prototype
        assert isinstance(token, str)
        assert len(token) > 50  # Reasonable JWT length
        assert decoded["email"] == test_email
    
    @given(st.emails())
    @pytest.mark.property
    def test_when_any_valid_email_provided_should_generate_valid_jwt(
        self, auth_service, email
    ):
        """Property test: any valid email should produce valid JWT."""
        # Act
        token = auth_service.generate_token(email)
        decoded = auth_service.verify_token(token)
        
        # Assert - properties that should always hold
        assert decoded is not None
        assert decoded["email"] == email
        assert isinstance(decoded["exp"], int)
        assert decoded["exp"] > datetime.utcnow().timestamp()
    
    @pytest.mark.smoke
    def test_when_auth_service_created_should_be_ready(self):
        """Smoke test: service should initialize properly."""
        # Act
        service = AuthService()
        
        # Assert
        assert service is not None
        assert hasattr(service, 'generate_token')
        assert hasattr(service, 'verify_token')
```