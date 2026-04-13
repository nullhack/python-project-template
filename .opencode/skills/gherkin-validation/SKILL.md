---
name: gherkin-validation
description: Validate BDD docstrings with Example format preference and proper Gherkin syntax
license: MIT
compatibility: opencode
metadata:
  audience: developers
  workflow: quality-assurance
---

## What I do
Validate BDD docstrings in test functions, with a preference for Example format while accepting any valid Gherkin syntax. Ensure proper newline formatting and provide helpful suggestions.

## When to use me
- During TDD phase to validate test docstring formats
- In QA enforcement to check BDD compliance
- When reviewing test files for documentation standards
- As part of automated quality checks

## Required Format: UUID-based Traceability

All test docstrings must use acceptance criteria UUID for traceability, followed by Gherkin steps:

```python
def test_user_login_with_valid_credentials_should_grant_access():
    """123e4567-e89b-12d3-a456-426614174000: Successful user authentication.

    Given: A registered user with valid credentials exists in the system  
    When: The user submits correct username and password
    Then: Access should be granted to the application
    """
```

## Alternative Formats Accepted

### Scenario-based Format
```python
def test_invalid_login_should_reject_access():
    """
    Scenario: Invalid login attempt
    Given: A user with incorrect credentials
    When: Login is attempted
    Then: Access should be denied
    And: Error message should be displayed
    """
```

### Feature-based Format
```python
def test_password_reset_flow_should_work():
    """
    Feature: Password reset functionality
    Scenario: User requests password reset
    Given: A registered user exists
    When: Password reset is requested
    Then: Reset email should be sent
    And: Temporary token should be generated
    """
```

### Extended Gherkin Keywords
All valid Gherkin keywords are supported:
- **Feature**: High-level description
- **Scenario**: Specific test case
- **Example**: Concrete illustration (preferred)
- **Given**: Preconditions or context
- **When**: Actions or events
- **Then**: Expected outcomes
- **And**: Additional conditions/actions/outcomes
- **But**: Negative conditions/actions/outcomes
- **Background**: Common setup for multiple scenarios
- **Rule**: Business rule description

## Validation Rules

### 1. Newline Requirements (STRICT)
Docstrings MUST start and end with newlines:
```python
# ✅ CORRECT
"""123e4567-e89b-12d3-a456-426614174000: Valid format.

Given: Proper newlines
When: Validation runs
Then: Should pass
"""

# ❌ WRONG - Missing newlines
"""123e4567-e89b-12d3-a456-426614174000: Invalid format.
Given: No starting newline"""

# ❌ WRONG - Missing ending newline  
"""
123e4567-e89b-12d3-a456-426614174000: Invalid format.
Given: No ending newline"""
```

### 2. Gherkin Keyword Validation
- Must use valid Gherkin keywords
- Keywords must be followed by a colon `:`
- Content after colon must be meaningful (not empty)

### 3. Structure Requirements
- At minimum: One Gherkin keyword with content
- Recommended: Logical flow (Given → When → Then)
- Example format preferred but not required

## Validation Guidelines

### Docstring Validation Checklist
- [ ] Docstring starts with newline: `"""\n`
- [ ] Docstring ends with newline before closing quotes
- [ ] Valid Gherkin keywords present (Given, When, Then, etc.)
- [ ] Keywords followed by meaningful content (not empty)
- [ ] Proper colon after each keyword

### Suggestion Messages
For improving docstrings when not using required UUID format:
```python
# For missing UUID
"Test docstring must start with acceptance criteria UUID for traceability"

# For old Example format  
"Convert 'Example:' to UUID format: 'uuid: description.' with blank line before Gherkin steps"

# For missing structure
"Add 'Given:' context and 'When:' action to complete the test scenario"
```

### suggest_uuid_format(docstring: str) -> str
Convert other formats to required UUID format:
```python
# Input: Old Example format
original = """
Example: User login
Given: Valid credentials
When: Login submitted
Then: Access granted
"""

# Output: UUID-based suggestion
suggested = suggest_uuid_format(original)
# """
# 123e4567-e89b-12d3-a456-426614174000: User login validation.
# 
# Given: Valid credentials exist in system
# When: Login credentials are submitted
# Then: Access should be granted to user
# """
```

## Common Issues & Solutions

### Issue: Missing Newlines
```python
# Problem
"""Given: Something
When: Action
Then: Result"""

# Solution  
"""
Given: Something
When: Action  
Then: Result
"""
```

### Issue: Invalid Gherkin Keywords
```python
# Problem
"""
Provided: Invalid keyword
During: Wrong keyword
Should: Not a Gherkin keyword
"""

# Solution
"""
Given: Valid precondition
When: Action occurs
Then: Expected outcome
"""
```

### Issue: Empty Content
```python
# Problem
"""
Given:
When:
Then:
"""

# Solution
"""
Given: Meaningful precondition description
When: Specific action or trigger
Then: Clear expected outcome
"""
```

## Quality Guidance

### Require UUID Format
When creating new tests, enforce UUID traceability format:
- Links tests to specific acceptance criteria
- Provides bidirectional traceability
- Enables coverage verification
- Supports compliance requirements

### Suggestion Messages
```python
# For missing UUID
"Test docstring must start with acceptance criteria UUID for traceability"

# For old Example format  
"Convert 'Example:' to UUID format with blank line before Gherkin steps"

# For missing structure
"Add 'Given:' context and 'When:' action to complete the test scenario"
```

## Manual Validation Checklist

When reviewing test files manually, check:

1. **Newline Formatting**
   - Docstrings must start with newline: `"""\n`
   - Docstrings must end with newline: `\n"""`

2. **UUID Traceability**
   - First line must be UUID: description format
   - UUID must match acceptance criteria from feature doc
   - Blank line required after UUID line

3. **Gherkin Keywords**
   - Use Given:, When:, Then:, And:, But:
   - Each keyword must have content after the colon
   - Follow logical flow from precondition to outcome

4. **Structure Validation**
   - UUID line + blank line + Gherkin steps
   - At minimum: Given/When/Then structure
   - Ensure logical flow from precondition to outcome

## Configuration Options

### Strictness Levels
```yaml
gherkin_validation:
  strictness: "prefer_example"  # "prefer_example", "accept_any", "require_example"
  require_newlines: true
  min_keywords: 2  # Minimum Given/When/Then structure
  allow_empty_sections: false
```

### Project Integration
```python
# In pyproject.toml
[tool.gherkin-validation]
preferred_format = "example"
strict_newlines = true
suggest_improvements = true
fail_on_invalid = true
```

## Validation Workflow

1. **Parse docstring** for Gherkin keywords
2. **Check newline formatting** (strict requirement)
3. **Validate keyword syntax** and content
4. **Determine format type** (Example, Scenario, Feature, etc.)
5. **Generate suggestions** if not using preferred format
6. **Report results** with specific improvement guidance

Remember: The goal is to guide developers toward the preferred Example format while maintaining flexibility and not breaking existing valid Gherkin documentation.