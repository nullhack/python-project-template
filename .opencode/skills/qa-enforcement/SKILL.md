---
name: qa-enforcement
description: Comprehensive quality enforcement with SOLID principles, Object Calisthenics, BDD validation, and zero-tolerance bypass policy
license: MIT
compatibility: opencode
metadata:
  audience: quality-assurance
  workflow: mandatory-checkpoints
---

## What I do
Enforce comprehensive quality standards including all 9 Object Calisthenics rules, SOLID/DRY/KISS/YAGNI principles, BDD docstring validation, and maintain zero tolerance for quality bypasses.

## When to use me
- During overseer QA checkpoints at each development phase
- Before feature completion and PR creation
- When quality violations are detected
- As part of automated quality validation workflows

## Quality Standards Enforced

### 1. Object Calisthenics (ALL 9 RULES - ZERO TOLERANCE)

#### Rule 1: One Level of Indentation Per Method
```python
# ❌ VIOLATION - Multiple nesting levels
def process_user_data(users):
    for user in users:
        if user.is_active:
            if user.has_permission:
                if user.email_verified:
                    # Too many levels!
                    process_user(user)

# ✅ COMPLIANT - Single level with early returns
def process_user_data(users):
    for user in users:
        if not user.is_active:
            continue
        if not user.has_permission:
            continue
        if not user.email_verified:
            continue
        process_user(user)
```

#### Rule 2: No ELSE Keyword
```python
# ❌ VIOLATION - Using else
def calculate_discount(user):
    if user.is_premium:
        return user.calculate_premium_discount()
    else:
        return user.calculate_standard_discount()

# ✅ COMPLIANT - Early return pattern
def calculate_discount(user):
    if user.is_premium:
        return user.calculate_premium_discount()
    return user.calculate_standard_discount()
```

#### Rule 3: Wrap All Primitives and Strings
```python
# ❌ VIOLATION - Naked primitives in business logic
class User:
    def __init__(self, name: str, age: int, email: str):
        self.name = name  # Naked string
        self.age = age    # Naked int
        self.email = email  # Naked string

# ✅ COMPLIANT - Wrapped in value objects
class User:
    def __init__(self, name: UserName, age: Age, email: EmailAddress):
        self.name = name
        self.age = age
        self.email = email

class UserName:
    def __init__(self, value: str):
        if not value or len(value.strip()) < 2:
            raise ValueError("User name must be at least 2 characters")
        self._value = value.strip()
    
    @property
    def value(self) -> str:
        return self._value
```

#### Rule 4: First Class Collections
```python
# ❌ VIOLATION - Collection + other instance variables
class UserManager:
    def __init__(self):
        self.users = []      # Collection
        self.admin_user = None  # Other instance variable
        self.settings = {}   # Another instance variable

# ✅ COMPLIANT - Collection wrapper with single responsibility  
class UserCollection:
    def __init__(self, users: List[User]):
        self._users = users
    
    def active_users(self) -> List[User]:
        return [user for user in self._users if user.is_active]

class UserManager:
    def __init__(self, users: UserCollection, admin: AdminUser):
        self._users = users
        self._admin = admin
```

#### Rule 5: One Dot Per Line (Law of Demeter)
```python
# ❌ VIOLATION - Multiple dots/method chaining
def get_user_city(user):
    return user.get_address().get_city().get_name()

# ✅ COMPLIANT - Tell, don't ask
def get_user_city(user):
    return user.get_city_name()  # Delegate to user object

# User class handles the complexity internally
class User:
    def get_city_name(self) -> str:
        return self._address.city_name()
```

#### Rule 6: No Abbreviations
```python
# ❌ VIOLATION - Abbreviations everywhere
def calc_tot_amt(usr_id, qty, prc):
    usr = get_usr(usr_id)
    tot = qty * prc
    return apply_disc(usr, tot)

# ✅ COMPLIANT - Clear, descriptive names
def calculate_total_amount(user_id: UserId, quantity: Quantity, price: Price):
    user = get_user(user_id)
    total = quantity.multiply_by(price)
    return apply_discount(user, total)
```

#### Rule 7: Keep Entities Small (Max 50 Lines)
```python
# ❌ VIOLATION - Massive class (100+ lines)
class UserService:
    # ... 20 methods, 100+ lines of complex logic

# ✅ COMPLIANT - Split into focused, small classes
class UserAuthenticator:          # 25 lines - focused on auth
    def authenticate(self, credentials): pass

class UserProfileManager:         # 30 lines - focused on profile
    def update_profile(self, user, data): pass

class UserNotificationSender:     # 20 lines - focused on notifications
    def send_welcome_email(self, user): pass
```

#### Rule 8: No Classes With More Than 2 Instance Variables
```python
# ❌ VIOLATION - Too many instance variables
class User:
    def __init__(self, name, email, age, address, phone, preferences):
        self.name = name           # 1
        self.email = email         # 2  
        self.age = age            # 3 - TOO MANY!
        self.address = address     # 4
        self.phone = phone        # 5
        self.preferences = preferences  # 6

# ✅ COMPLIANT - Composition with max 2 variables
class User:
    def __init__(self, identity: UserIdentity, profile: UserProfile):
        self._identity = identity    # 1
        self._profile = profile      # 2

class UserIdentity:
    def __init__(self, name: UserName, email: EmailAddress):
        self._name = name           # 1
        self._email = email         # 2

class UserProfile:
    def __init__(self, demographics: Demographics, contact: ContactInfo):
        self._demographics = demographics  # 1  
        self._contact = contact           # 2
```

#### Rule 9: No Getters/Setters (Tell, Don't Ask)
```python
# ❌ VIOLATION - Exposing internal state with getters/setters
class BankAccount:
    def get_balance(self): return self._balance
    def set_balance(self, amount): self._balance = amount

# Client code that violates encapsulation
account = BankAccount()
if account.get_balance() > 100:  # Asking for data
    account.set_balance(account.get_balance() - 100)  # Manipulating externally

# ✅ COMPLIANT - Tell objects what to do
class BankAccount:
    def withdraw(self, amount: Money) -> WithdrawalResult:
        if self._balance.is_sufficient_for(amount):
            self._balance = self._balance.subtract(amount)
            return WithdrawalResult.success()
        return WithdrawalResult.insufficient_funds()

# Client code that respects encapsulation  
account = BankAccount()
result = account.withdraw(Money(100))  # Telling what to do
if result.is_successful():
    # Handle success
```

### 2. SOLID Principles Enforcement

#### Single Responsibility Principle (SRP)
- Each class should have only one reason to change
- Functions should do one thing well
- Modules should have single, well-defined purpose

#### Open/Closed Principle (OCP)
- Classes should be open for extension, closed for modification
- Use composition, inheritance, and dependency injection
- Avoid modifying existing code when adding features

#### Liskov Substitution Principle (LSP)
- Derived classes must be substitutable for base classes
- Subtypes must honor the contract of their supertypes
- No strengthening preconditions or weakening postconditions

#### Interface Segregation Principle (ISP)
- Many specific interfaces are better than one general-purpose interface
- Clients shouldn't depend on interfaces they don't use
- Use protocols and abstract base classes appropriately

#### Dependency Inversion Principle (DIP)
- Depend on abstractions, not concretions
- High-level modules shouldn't depend on low-level modules
- Use dependency injection and inversion of control

### 3. Additional Quality Principles

#### DRY (Don't Repeat Yourself)
- No code duplication - extract common logic into reusable components
- Share constants, utilities, and common patterns
- Use inheritance, composition, and mixins appropriately

#### KISS (Keep It Simple, Stupid)
- Simplest solution that works is usually the best
- Avoid over-engineering and premature optimization
- Prefer readable code over clever code

#### YAGNI (You Aren't Gonna Need It)
- Don't implement features until they're actually needed
- Avoid speculative generality and future-proofing
- Focus on current requirements, not imagined future needs

### 4. BDD Test Quality Standards

#### Mandatory Docstring Format
All test functions must use proper Gherkin format with Example preference:

```python
def test_user_login_with_valid_credentials_should_grant_access():
    """
    Example: Successful user authentication
    Given: A registered user with valid credentials exists
    When: The user submits correct username and password  
    Then: Access should be granted to the application
    """
```

#### Required Elements
- **Function naming**: `test_<condition>_should_<outcome>` (STRICT)
- **File naming**: `*_test.py` suffix (STRICT)
- **Newline requirement**: `"""\n<content>\n"""` (STRICT)
- **Gherkin keywords**: Valid keywords with meaningful content
- **Format preference**: Example > Scenario > Feature

### 5. Zero Tolerance Policy

#### Forbidden Quality Bypasses
```python
# ❌ NEVER ALLOWED - Quality bypasses
# noqa: E501         # Bypassing line length
# type: ignore       # Bypassing type checking (without justification)
pytest.skip()       # Skipping tests without valid reason
@pytest.mark.skip   # Marking tests to skip
```

#### Required Actions for Bypasses
1. **Identify root cause** of the quality issue
2. **Fix the underlying problem** rather than bypass
3. **Refactor code** to meet quality standards
4. **No exceptions** - find proper solutions

## Validation Workflows

### 1. Object Calisthenics Validation
```python
def validate_object_calisthenics(file_path: str) -> ValidationResult:
    """Validate all 9 Object Calisthenics rules against code file."""
    violations = []
    
    # Rule 1: Check indentation levels
    violations.extend(check_indentation_levels(file_path))
    
    # Rule 2: Check for else keywords  
    violations.extend(check_else_usage(file_path))
    
    # Rule 3: Check for primitive wrapping
    violations.extend(check_primitive_wrapping(file_path))
    
    # ... all 9 rules
    
    return ValidationResult(
        is_compliant=len(violations) == 0,
        violations=violations,
        suggestions=generate_calisthenics_suggestions(violations)
    )
```

### 2. SOLID Principles Analysis
```python
def analyze_solid_compliance(module_path: str) -> SolidAnalysis:
    """Analyze code for SOLID principle compliance."""
    return SolidAnalysis(
        srp_violations=check_single_responsibility(module_path),
        ocp_violations=check_open_closed(module_path),
        lsp_violations=check_liskov_substitution(module_path),
        isp_violations=check_interface_segregation(module_path),
        dip_violations=check_dependency_inversion(module_path)
    )
```

### 3. BDD Format Validation
```python
def validate_bdd_compliance(test_file: str) -> BddValidationResult:
    """Validate BDD format compliance in test files."""
    # Use gherkin-validation skill
    from gherkin_validation import validate_test_docstring
    
    test_functions = extract_test_functions(test_file)
    results = []
    
    for func in test_functions:
        # Check function naming
        if not func.name.matches_pattern("test_*_should_*"):
            results.append(f"Function {func.name} violates naming convention")
        
        # Check docstring format
        validation = validate_test_docstring(func.docstring)
        if not validation.is_valid:
            results.append(f"Function {func.name}: {validation.issues}")
    
    return BddValidationResult(is_compliant=len(results) == 0, issues=results)
```

## Quality Gate Checklist

### Pre-Implementation Gate
- [ ] Requirements align with business value
- [ ] Acceptance criteria use Example format
- [ ] Technical design follows SOLID principles
- [ ] Architecture supports Object Calisthenics compliance

### Post-TDD Gate  
- [ ] All test functions follow `test_<condition>_should_<outcome>` naming
- [ ] All test files use `*_test.py` naming convention
- [ ] All test docstrings use proper Gherkin format with newlines
- [ ] Example format preferred, alternatives acceptable
- [ ] Test coverage strategy is comprehensive

### Post-Implementation Gate
- [ ] All 9 Object Calisthenics rules satisfied
- [ ] SOLID principles followed throughout
- [ ] DRY principle maintained (no duplication)
- [ ] KISS principle applied (appropriate simplicity)
- [ ] YAGNI principle respected (no over-engineering)
- [ ] Zero quality bypasses (no noqa, type: ignore without justification)

### Final Quality Gate
- [ ] All linting passes: `task lint`
- [ ] All type checking passes: `task static-check`
- [ ] All tests pass: `task test`
- [ ] 100% test coverage maintained
- [ ] No security vulnerabilities detected
- [ ] Performance meets requirements

## Integration with Overseer Agent

### Auto-Delegation Triggers
When violations are detected:
- **Object Calisthenics violations** → Auto-delegate to `@architect`
- **BDD format violations** → Auto-delegate to `@developer`  
- **Naming convention violations** → Auto-delegate to `@developer`
- **SOLID violations** → Auto-delegate to `@architect`
- **Quality bypasses** → Auto-delegate to `@developer`

### Blocking Authority
- Development cannot proceed without QA approval
- No exceptions for quality standards
- No bypasses allowed without fixing root cause
- Manual retry required after fixes

Remember: Quality is not negotiable. These standards ensure maintainable, robust, and professional code that stands the test of time. Every rule exists for a reason - enforce them consistently and help developers understand the "why" behind quality requirements.