---
name: implementation
description: Implement functions and classes using TDD approach with all tests passing after each method completion
license: MIT
compatibility: opencode
metadata:
  audience: developers
  workflow: feature-development
---
## What I do
Guide the implementation of functions and classes following Test-Driven Development, ensuring all tests pass after implementing each method using real data from prototypes.

## When to use me
Use this after architect approval to implement the actual functionality, working method by method with tests passing at each step.

## TDD Implementation Process

### 1. Implementation Strategy
- Implement one method/function at a time
- Use real data captured from prototype scripts
- Ensure all tests pass after each method completion
- Follow the designed signatures exactly
- Maintain code quality standards throughout

### 2. Red-Green-Refactor Cycle
```python
# RED: Test is already written and failing
def test_when_valid_email_provided_should_return_jwt_token():
    # This test exists from TDD phase and is currently failing
    pass

# GREEN: Implement minimal code to pass the test
def generate_token(email: str) -> str:
    # Minimal implementation using prototype data
    return "hardcoded_jwt_token_from_prototype"

# REFACTOR: Improve implementation while keeping tests green
def generate_token(email: str) -> str:
    # Real implementation using prototype findings
    payload = {"email": email, "exp": calculate_expiry()}
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")
```

### 3. Using Prototype Data for Implementation
```python
# Load real data captured during prototyping
def load_prototype_examples():
    """Load real examples from prototype testing."""
    with open("prototypes/jwt_prototype_results.json") as f:
        return json.load(f)

def generate_token(user_email: str, *, expiry_hours: int = 24) -> AuthToken:
    """Generate JWT token using proven approach from prototype.
    
    Implementation based on prototype validation that showed:
    - Token length: ~157 characters  
    - Structure: header.payload.signature
    - Successful encoding/decoding cycle
    """
    # Use the exact approach that worked in prototype
    payload = {
        "email": user_email,
        "exp": datetime.utcnow() + timedelta(hours=expiry_hours),
        "iat": datetime.utcnow()
    }
    
    token = jwt.encode(payload, self._secret_key, algorithm=self._algorithm)
    
    return AuthToken(
        token=token,
        expires_at=payload["exp"], 
        user_email=user_email
    )
```

### 4. Method-by-Method Implementation
```python
class JWTTokenProvider:
    """JWT token provider - implement each method individually."""
    
    def __init__(self, *, secret_key: str, algorithm: str = "HS256") -> None:
        """Step 1: Implement constructor.
        
        Tests should pass after this implementation.
        """
        self._secret_key = secret_key
        self._algorithm = algorithm
        # Run tests after this method - should pass constructor tests
    
    def generate_token(self, user_email: str, *, expiry_hours: int = 24) -> AuthToken:
        """Step 2: Implement token generation.
        
        Use real JWT library with prototype-validated approach.
        Tests should pass after this implementation.
        """
        # Validate email format first (as per test requirements)
        if not self._is_valid_email(user_email):
            raise ValidationError(f"Invalid email format: {user_email}")
        
        # Create payload based on prototype structure
        now = datetime.utcnow()
        expires = now + timedelta(hours=expiry_hours)
        
        payload = {
            "email": user_email,
            "exp": expires,
            "iat": now
        }
        
        # Generate token using prototype-proven method
        token = jwt.encode(payload, self._secret_key, algorithm=self._algorithm)
        
        return AuthToken(
            token=token,
            expires_at=expires,
            user_email=user_email
        )
        # Run tests after this method - token generation tests should pass
    
    def verify_token(self, token: str) -> Optional[dict[str, Any]]:
        """Step 3: Implement token verification.
        
        Use prototype-validated decoding approach.
        Tests should pass after this implementation.
        """
        try:
            payload = jwt.decode(
                token, 
                self._secret_key, 
                algorithms=[self._algorithm]
            )
            return payload
        except jwt.InvalidTokenError:
            return None
        # Run tests after this method - all tests should pass
    
    def _is_valid_email(self, email: str) -> bool:
        """Step 4: Implement email validation helper.
        
        Private method to support public methods.
        """
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
```

### 5. Error Handling Implementation
```python
# Implement custom exceptions as defined in signatures
class AuthenticationError(Exception):
    """Base authentication error - implement with real examples."""
    
    def __init__(
        self, 
        message: str, 
        *, 
        error_code: str,
        user_email: Optional[str] = None
    ) -> None:
        super().__init__(message)
        self.error_code = error_code
        self.user_email = user_email

class ValidationError(AuthenticationError):
    """Validation error - tested with real invalid inputs."""
    
    def __init__(self, message: str, user_email: Optional[str] = None) -> None:
        super().__init__(
            message,
            error_code="VALIDATION_ERROR",
            user_email=user_email
        )
```

### 6. Value Object Implementation
```python
@dataclass(frozen=True, slots=True)
class AuthToken:
    """Implement immutable token using prototype structure."""
    token: str
    expires_at: datetime
    user_email: str
    token_type: str = "Bearer"
    
    def is_expired(self) -> bool:
        """Implementation based on prototype timing tests."""
        return datetime.utcnow() > self.expires_at
    
    def __post_init__(self) -> None:
        """Validate token structure matches prototype format."""
        if not isinstance(self.token, str) or len(self.token) < 50:
            raise ValueError("Invalid token format")
        
        if self.token.count('.') != 2:
            raise ValueError("Token must be valid JWT format")
```

### 7. Test-Driven Implementation Workflow
```bash
# Step-by-step implementation process:

# 1. Start with failing tests
task test
# Tests should fail (RED phase)

# 2. Implement first method (constructor)
# Edit implementation file
task test
# Constructor tests should now pass

# 3. Implement second method (generate_token)
# Edit implementation file  
task test
# Token generation tests should now pass

# 4. Implement third method (verify_token)
# Edit implementation file
task test
# All tests should now pass (GREEN phase)

# 5. Refactor if needed
# Improve code quality while keeping tests green
task test
# Tests should still pass (REFACTOR phase)

# 6. Final validation
task lint
task static-check
# All quality checks should pass
```

### 8. Real Data Integration
```python
def implement_using_prototype_data():
    """Use real examples from prototype for implementation validation."""
    
    # Load actual prototype results
    with open("prototypes/jwt_prototype_results.json") as f:
        prototype_data = json.load(f)
    
    # Verify implementation produces similar results
    provider = JWTTokenProvider(secret_key="test_key")
    token = provider.generate_token(prototype_data["input_email"])
    
    # Validate against prototype findings
    assert len(token.token) > 100  # Prototype showed ~157 chars
    assert token.token.count('.') == 2  # JWT structure verified
    assert token.user_email == prototype_data["input_email"]
    
    # Verify round-trip works (prototype proved this)
    decoded = provider.verify_token(token.token)
    assert decoded["email"] == prototype_data["input_email"]
```

### 9. Quality Gates After Each Method
After implementing each method, verify:
- All related tests pass
- Code coverage remains at target level
- No linting errors introduced
- Type checking passes
- Documentation is complete

### 10. Final Integration Validation
```python
def integration_test_with_prototype_data():
    """Final test using all prototype scenarios."""
    
    # Test all scenarios that worked in prototype
    provider = JWTTokenProvider(secret_key="production_key")
    
    # Test cases from prototype validation
    test_scenarios = [
        "user@example.com",
        "admin@company.org", 
        "test.user+tag@domain.co.uk"
    ]
    
    for email in test_scenarios:
        # Generate token
        token = provider.generate_token(email)
        
        # Verify token
        payload = provider.verify_token(token.token)
        
        # Assertions based on prototype behavior
        assert payload is not None
        assert payload["email"] == email
        assert token.is_expired() is False
```

## Implementation Checklist

✅ **Before starting each method:**
- [ ] Understand what tests expect this method to do
- [ ] Review prototype data for this functionality
- [ ] Check the designed signature is correct

✅ **While implementing each method:**
- [ ] Use exact signature from design phase
- [ ] Implement using prototype-proven approach
- [ ] Handle errors as designed
- [ ] Add any necessary private helpers

✅ **After completing each method:**
- [ ] Run tests - should pass for this method
- [ ] Check code coverage hasn't dropped
- [ ] Run linting - should pass
- [ ] Verify type checking passes

✅ **After completing all methods:**
- [ ] All tests pass
- [ ] Coverage meets minimum requirement
- [ ] Linting passes
- [ ] Type checking passes
- [ ] Integration test with prototype data passes