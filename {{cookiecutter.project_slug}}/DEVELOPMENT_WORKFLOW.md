# Development Workflow Guide

This document describes the comprehensive development workflow for {{cookiecutter.project_name}} following SOLID principles, object calisthenics, and Test-Driven Development with architecture review.

## Overview

The workflow follows a structured 7-phase approach ensuring high-quality, well-tested, and architecturally sound code:

1. **Feature Definition** - Define requirements and acceptance criteria
2. **Prototype Validation** - Create quick scripts to validate concepts
3. **Test-Driven Development** - Write comprehensive tests first
4. **Signature Design** - Design clean interfaces and contracts
5. **Architecture Review** - Get approval from architect agent
6. **Implementation** - Implement using TDD methodology
7. **Quality Assurance** - Enforce quality standards

## Phase 1: Feature Definition

**Goal**: Establish clear requirements following SOLID principles.

**Agent/Skill**: `/skill feature-definition`

**Activities**:
- Define feature purpose and value proposition
- Create functional and non-functional requirements
- Write acceptance criteria in Given-When-Then format
- Plan for SOLID principles compliance
- Consider object calisthenics constraints

**Output**: Feature definition document with clear requirements and acceptance criteria.

**Example**:
```
Feature: User Authentication API
Purpose: Secure user login system
Value: Protects user data and provides personalized experience

Acceptance Criteria:
Given valid user credentials
When POST /auth/login is called
Then return 200 with JWT token and expiration
```

## Phase 2: Prototype Validation

**Goal**: Validate core functionality with real data before proper implementation.

**Agent/Skill**: `/skill prototype-script`

**Activities**:
- Create quick and dirty scripts to test concepts
- Validate API responses, data parsing, file operations
- Capture real input/output examples
- Test edge cases and error conditions
- Save prototype results for implementation reference

**Output**: Working prototype scripts and captured real data examples.

**Directory Structure**:
```
prototypes/
├── feature_name_prototype.py
├── sample_responses/
│   ├── api_response.json
│   └── error_response.json
└── test_data/
    └── sample_input.txt
```

## Phase 3: Test-Driven Development

**Goal**: Create comprehensive test suite using BDD naming before implementation.

**Agent/Skill**: `/skill tdd-bdd`

**Activities**:
- Write tests using BDD naming conventions
- Use real data from prototype phase
- Include unit, integration, and property-based tests
- Organize tests with pytest markers
- Ensure tests fail initially (RED phase)

**Test Categories**:
- `@pytest.mark.unit` - Unit tests for individual functions
- `@pytest.mark.integration` - Integration tests for component interaction
- `@pytest.mark.property` - Property-based tests with Hypothesis
- `@pytest.mark.smoke` - Basic functionality validation

**Example**:
```python
def test_when_valid_email_provided_should_return_jwt_token():
    """Test JWT generation with valid email."""
    # Use real data from prototype
    email = "user@example.com"
    auth_service = AuthService()
    
    result = auth_service.generate_token(email)
    
    assert isinstance(result, AuthToken)
    assert result.user_email == email
```

## Phase 4: Signature Design

**Goal**: Design clean, type-safe interfaces using modern Python.

**Agent/Skill**: `/skill signature-design`

**Activities**:
- Create function and class signatures with complete type hints
- Design protocols instead of inheritance hierarchies
- Use dataclasses and value objects for data
- Write comprehensive Google-style docstrings
- Include real examples from prototype data
- Follow object calisthenics principles

**Standards**:
- All functions have type hints and return types
- Use Protocol for interface definition
- Immutable data structures where possible
- One responsibility per class/function
- No primitive obsession - wrap in value objects

**Example**:
```python
@dataclass(frozen=True, slots=True)
class AuthToken:
    """Immutable authentication token."""
    token: str
    expires_at: datetime
    user_email: str

def generate_auth_token(
    user_email: str,
    *,
    expiry_hours: int = 24
) -> AuthToken:
    """Generate JWT authentication token.
    
    Example:
        >>> token = generate_auth_token("user@example.com")
        >>> token.token  # Real length from prototype: 157 chars
        'eyJ0eXAiOiJKV1QiLCJhbGci...'
    """
```

## Phase 5: Architecture Review

**Goal**: Ensure design meets architectural standards before implementation.

**Agent**: `@architect`

**Activities**:
- Present feature definition and design to architect agent
- Review SOLID principles compliance
- Validate object calisthenics adherence
- Check interface design and dependencies
- Address any architectural concerns

**Approval Criteria**:
- ✅ SOLID principles followed
- ✅ Object calisthenics rules applied
- ✅ Clean interfaces and minimal dependencies
- ✅ Proper error handling design
- ✅ Testable architecture

**Architecture Review Response**:
```
## Architecture Review: Feature Name

### ✅ APPROVED with suggestions
**Strengths**: Clean separation, proper protocols, immutable objects
**Suggestions**: Extract email validation, focus TokenProvider interface
**Implementation may proceed** - address suggestions in iteration
```

## Phase 6: Implementation

**Goal**: Implement functionality using TDD methodology with architect-approved design.

**Agent/Skill**: `/skill implementation`

**Activities**:
- Implement one method/function at a time
- Use real data from prototype scripts
- Ensure tests pass after each method completion
- Follow exact signatures from design phase
- Maintain RED-GREEN-REFACTOR cycle

**Implementation Strategy**:
1. Start with failing tests (RED)
2. Implement minimal code to pass tests (GREEN)  
3. Refactor while keeping tests green (REFACTOR)
4. Use prototype data for validation
5. Run tests after each method

**Quality Gates**:
- All related tests pass after each method
- Code coverage maintained at {{cookiecutter.minimum_coverage}}%
- No linting errors introduced
- Type checking passes

## Phase 7: Quality Assurance

**Goal**: Enforce comprehensive code quality standards.

**Agent/Skill**: `/skill code-quality`

**Activities**:
- Run ruff linting and formatting: `task lint`
- Execute type checking: `task static-check`
- Verify test coverage: `task test`
- Run property-based tests with Hypothesis
- Validate complexity limits (max 10)
- Check documentation completeness

**Quality Standards**:
- **Coverage**: Minimum {{cookiecutter.minimum_coverage}}%
- **Complexity**: Maximum 10 per function
- **Type Safety**: All functions type-hinted
- **Documentation**: Google docstrings on all public functions
- **Testing**: Unit, integration, and property tests

**Quality Commands**:
```bash
task lint          # Linting and formatting
task static-check  # Type checking  
task test          # Tests with coverage
task test-report   # Detailed coverage report
task mut-report    # Mutation testing (optional)
```

## Architectural Principles

### SOLID Principles

- **S**ingle Responsibility: Each class has one reason to change
- **O**pen/Closed: Open for extension, closed for modification
- **L**iskov Substitution: Derived classes must be substitutable
- **I**nterface Segregation: Clients shouldn't depend on unused methods
- **D**ependency Inversion: Depend on abstractions, not concretions

### Object Calisthenics Rules

1. Only one level of indentation per method
2. Don't use the ELSE keyword (use guard clauses)
3. Wrap all primitives and strings (value objects)
4. First class collections only (wrap in dedicated classes)
5. One dot per line (avoid chaining)
6. Don't abbreviate names (be explicit)
7. Keep all entities small (<50 lines per class)
8. No more than two instance variables per class
9. No getters/setters/properties (behavior-rich objects)

## Example Complete Workflow

```bash
# 1. Feature Definition
/skill feature-definition
# → Define user authentication feature

# 2. Prototype Validation  
/skill prototype-script
# → Create JWT prototype, capture real data

# 3. Test-Driven Development
/skill tdd-bdd  
# → Write comprehensive test suite

# 4. Signature Design
/skill signature-design
# → Design AuthService, AuthToken interfaces

# 5. Architecture Review
@architect
# → Review design, get approval

# 6. Implementation
/skill implementation
# → Implement method by method with TDD

# 7. Quality Assurance
/skill code-quality
# → Run all quality checks

# Final validation
task lint && task static-check && task test
```

## Skills and Agents Reference

### Available Skills
- **feature-definition**: Plan features with SOLID principles
- **prototype-script**: Quick validation scripts  
- **tdd-bdd**: Test-driven development with BDD naming
- **signature-design**: Modern Python interface design
- **implementation**: TDD implementation methodology
- **code-quality**: Quality enforcement tools
- **create-skill**: Create new OpenCode skills
- **create-agent**: Create new OpenCode agents

### Available Agents
- **@developer**: Main development agent with full workflow
- **@architect**: Architecture review and approval agent
- Primary OpenCode agents: Build, Plan, General, Explore

## Quality Metrics

- **Test Coverage**: {{cookiecutter.minimum_coverage}}% minimum
- **Cyclomatic Complexity**: Maximum 10 per function
- **Documentation**: Google docstrings required
- **Type Safety**: Complete type hints
- **Code Quality**: Ruff linting compliance
- **Architecture**: SOLID + Object Calisthenics compliance

This workflow ensures maintainable, well-tested, and architecturally sound code that follows modern Python best practices and design principles.