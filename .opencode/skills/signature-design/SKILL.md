---
name: signature-design
description: Design function and class signatures using modern Python best practices, type hints, protocols, and Google docstrings
license: MIT
compatibility: opencode
metadata:
  audience: developers
  workflow: feature-development
---
## What I do
Create well-designed function and class signatures using modern Python features, proper type hints, protocols, dataclasses, and comprehensive Google-style docstrings with real examples.

## When to use me
Use this after TDD tests are written but before implementation to design clean, type-safe interfaces.

## Signature Design Principles

### 1. Modern Python Type Hints
```python
from typing import Protocol, TypeVar, Generic, Literal, overload
from collections.abc import Sequence, Mapping, Iterator
from datetime import datetime
from pathlib import Path

T = TypeVar('T')
K = TypeVar('K') 
V = TypeVar('V')

class Serializable(Protocol):
    """Protocol for objects that can be serialized."""
    
    def to_dict(self) -> dict[str, Any]: ...
    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Self: ...
```

### 2. Function Signatures with Real Examples
```python
from dataclasses import dataclass
from typing import Any, Optional

@dataclass(frozen=True)
class AuthToken:
    """Immutable authentication token."""
    token: str
    expires_at: datetime
    user_email: str
    
    def is_expired(self) -> bool:
        """Check if token has expired."""
        return datetime.utcnow() > self.expires_at

def generate_auth_token(
    user_email: str,
    *,
    expiry_hours: int = 24,
    secret_key: Optional[str] = None
) -> AuthToken:
    """Generate JWT authentication token for user.
    
    Creates a time-limited JWT token for authenticated user access.
    Uses HS256 algorithm with configurable expiration time.
    
    Args:
        user_email: Valid email address for the user.
        expiry_hours: Token validity period in hours. Defaults to 24.
        secret_key: Optional custom secret key. Uses environment default if None.
        
    Returns:
        AuthToken containing the JWT string and expiration info.
        
    Raises:
        ValidationError: If email format is invalid.
        ConfigurationError: If no secret key available.
        
    Example:
        Basic usage:
        >>> token = generate_auth_token("user@example.com")
        >>> token.token
        'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...'
        >>> token.user_email
        'user@example.com'
        
        Custom expiration:
        >>> short_token = generate_auth_token(
        ...     "admin@example.com",
        ...     expiry_hours=1
        ... )
        >>> short_token.expires_at
        datetime.datetime(2024, 1, 1, 13, 0, 0, 123456)
        
    Note:
        Token format follows JWT RFC 7519 standard.
        Expiration time is UTC-based for consistency.
    """
```

### 3. Class Design with Protocols
```python
from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable

@runtime_checkable
class TokenProvider(Protocol):
    """Protocol for token generation services."""
    
    def generate_token(self, user_email: str) -> AuthToken: ...
    def verify_token(self, token: str) -> Optional[dict[str, Any]]: ...

@runtime_checkable  
class UserRepository(Protocol):
    """Protocol for user data access."""
    
    def find_by_email(self, email: str) -> Optional['User']: ...
    def save(self, user: 'User') -> None: ...

class AuthService:
    """Authentication service with dependency injection."""
    
    def __init__(
        self,
        token_provider: TokenProvider,
        user_repository: UserRepository,
        *,
        max_login_attempts: int = 3
    ) -> None:
        """Initialize authentication service.
        
        Args:
            token_provider: Service for generating/verifying tokens.
            user_repository: Repository for user data operations.
            max_login_attempts: Maximum failed attempts before lockout.
            
        Example:
            >>> jwt_provider = JWTTokenProvider(secret_key="secret")
            >>> user_repo = DatabaseUserRepository(db_url="sqlite:///users.db")
            >>> auth_service = AuthService(jwt_provider, user_repo)
        """
        self._token_provider = token_provider
        self._user_repository = user_repository
        self._max_attempts = max_login_attempts
```

### 4. Dataclasses and Value Objects
```python
@dataclass(frozen=True, slots=True)
class EmailAddress:
    """Value object for validated email addresses."""
    address: str
    
    def __post_init__(self) -> None:
        """Validate email format on creation."""
        if not self._is_valid_email(self.address):
            raise ValidationError(f"Invalid email format: {self.address}")
    
    @staticmethod
    def _is_valid_email(email: str) -> bool:
        """Check if email format is valid using regex."""
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    
    @property
    def domain(self) -> str:
        """Extract domain part of email.
        
        Returns:
            Domain portion after @ symbol.
            
        Example:
            >>> email = EmailAddress("user@example.com")
            >>> email.domain
            'example.com'
        """
        return self.address.split('@')[1]

@dataclass(slots=True)
class User:
    """User entity with business logic."""
    email: EmailAddress
    name: str
    created_at: datetime
    is_active: bool = True
    failed_login_attempts: int = 0
    
    def lock_account(self) -> None:
        """Lock user account due to security concerns.
        
        Deactivates account and resets failed attempt counter.
        Should be called after maximum login attempts exceeded.
        
        Example:
            >>> user = User(EmailAddress("user@test.com"), "Test User", datetime.utcnow())
            >>> user.lock_account()
            >>> user.is_active
            False
        """
        self.is_active = False
        self.failed_login_attempts = 0
```

### 5. Generic and Overloaded Functions
```python
T = TypeVar('T', bound='Serializable')

class Repository(Generic[T]):
    """Generic repository for any serializable entity."""
    
    def __init__(self, entity_type: type[T]) -> None:
        self._entity_type = entity_type
    
    def save(self, entity: T) -> None:
        """Save entity to storage."""
        ...
    
    def find_by_id(self, entity_id: str) -> Optional[T]:
        """Find entity by ID."""
        ...

@overload
def parse_response(data: str) -> dict[str, Any]: ...

@overload  
def parse_response(data: bytes) -> dict[str, Any]: ...

@overload
def parse_response(data: dict[str, Any]) -> dict[str, Any]: ...

def parse_response(
    data: str | bytes | dict[str, Any]
) -> dict[str, Any]:
    """Parse API response in various formats.
    
    Handles JSON strings, byte data, or already-parsed dictionaries.
    Normalizes all input types to consistent dictionary format.
    
    Args:
        data: Response data in string, bytes, or dict format.
        
    Returns:
        Parsed dictionary with normalized structure.
        
    Raises:
        ParseError: If data cannot be parsed as valid JSON.
        
    Examples:
        From JSON string:
        >>> parse_response('{"user": "john", "id": 123}')
        {'user': 'john', 'id': 123}
        
        From bytes:
        >>> parse_response(b'{"status": "ok"}')
        {'status': 'ok'}
        
        From dict (passthrough):
        >>> parse_response({"already": "parsed"})
        {'already': 'parsed'}
    """
```

### 6. Error Handling Design
```python
class AuthenticationError(Exception):
    """Base exception for authentication failures."""
    
    def __init__(
        self, 
        message: str,
        *,
        error_code: str,
        user_email: Optional[str] = None
    ) -> None:
        """Initialize authentication error.
        
        Args:
            message: Human-readable error description.
            error_code: Machine-readable error identifier.
            user_email: Optional user email for logging context.
            
        Example:
            >>> error = AuthenticationError(
            ...     "Invalid credentials provided",
            ...     error_code="AUTH_001",
            ...     user_email="user@example.com"
            ... )
        """
        super().__init__(message)
        self.error_code = error_code
        self.user_email = user_email
        
class ValidationError(AuthenticationError):
    """Validation-specific authentication error."""
    pass

class TokenExpiredError(AuthenticationError):
    """Token expiration error with refresh suggestion."""
    
    def __init__(self, expired_token: str) -> None:
        super().__init__(
            "Authentication token has expired",
            error_code="AUTH_002"
        )
        self.expired_token = expired_token
```

### 7. Complete Interface Example
```python
"""
Authentication module interface definitions.
Created from test data (values copied from prototype run, then prototype deleted)
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Optional, Protocol, runtime_checkable

@dataclass(frozen=True, slots=True)
class AuthToken:
    """Immutable authentication token with metadata."""
    token: str
    expires_at: datetime
    user_email: str
    token_type: str = "Bearer"
    
    def is_expired(self) -> bool:
        """Check if token has expired.
        
        Returns:
            True if current time is past expiration, False otherwise.
            
        Example:
            >>> from datetime import datetime, timedelta
            >>> past_time = datetime.utcnow() - timedelta(hours=1)
            >>> expired_token = AuthToken("abc123", past_time, "user@test.com")
            >>> expired_token.is_expired()
            True
        """
        return datetime.utcnow() > self.expires_at

@runtime_checkable
class TokenProvider(Protocol):
    """Protocol for authentication token services."""
    
    def generate_token(
        self,
        user_email: str,
        *,
        expiry_hours: int = 24
    ) -> AuthToken:
        """Generate authentication token for user.
        
        Args:
            user_email: Valid email address.
            expiry_hours: Token validity period in hours.
            
        Returns:
            AuthToken with JWT and expiration info.
        """
        ...
    
    def verify_token(self, token: str) -> Optional[dict[str, Any]]:
        """Verify and decode authentication token.
        
        Args:
            token: JWT token string to verify.
            
        Returns:
            Decoded token payload if valid, None if invalid.
        """
        ...

class JWTTokenProvider:
    """JWT implementation of TokenProvider protocol."""
    
    def __init__(
        self,
        *,
        secret_key: str,
        algorithm: str = "HS256"
    ) -> None:
        """Initialize JWT token provider.
        
        Args:
            secret_key: Secret key for JWT signing.
            algorithm: JWT signing algorithm (default: HS256).
            
        Example:
            >>> provider = JWTTokenProvider(secret_key="my-secret-key")
            >>> token = provider.generate_token("user@example.com")
            >>> isinstance(token, AuthToken)
            True
        """
        self._secret_key = secret_key
        self._algorithm = algorithm
    
    def generate_token(
        self,
        user_email: str,
        *,
        expiry_hours: int = 24
    ) -> AuthToken:
        """Generate JWT token for authenticated user.
        
        Creates signed JWT with user email and expiration time.
        Token includes issued-at time for security auditing.
        
        Args:
            user_email: Valid email address for token subject.
            expiry_hours: Hours until token expires (default: 24).
            
        Returns:
            AuthToken containing JWT string and expiration metadata.
            
        Raises:
            ValidationError: If email format is invalid.
            
        Example:
            Real example based on prototype testing:
            >>> provider = JWTTokenProvider(secret_key="test_secret")
            >>> token = provider.generate_token("user@example.com")
            >>> len(token.token)  # Actual length from prototype: 157
            157
            >>> token.user_email
            'user@example.com'
            >>> token.token_type
            'Bearer'
        """
```

### 8. Object Calisthenics Compliance
- **One level of indentation per method**: Use early returns and guard clauses
- **Don't use the ELSE keyword**: Use guard clauses and early returns
- **Wrap all primitives and strings**: Use value objects like EmailAddress
- **First class collections**: Wrap lists/dicts in dedicated classes
- **One dot per line**: Use intermediate variables for chained calls
- **Don't abbreviate**: Use full descriptive names
- **Keep all entities small**: Classes under 50 lines, methods under 10 lines
- **No classes with more than two instance variables**: Use composition
- **No getters/setters/properties**: Use behavior-rich objects