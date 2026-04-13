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

## Preferred Format: Example-based

The **preferred** format uses `Example:` followed by `Given:`/`When:`/`Then:` with mandatory newlines:

```python
def test_user_login_with_valid_credentials_should_grant_access():
    """
    Example: Successful user authentication
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
"""
Example: Valid format
Given: Proper newlines
When: Validation runs
Then: Should pass
"""

# ❌ WRONG - Missing newlines
"""Example: Invalid format
Given: No starting newline"""

# ❌ WRONG - Missing ending newline  
"""
Example: Invalid format
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
For improving docstrings when not using preferred Example format:
```python
# For Scenario format
"Consider using 'Example:' instead of 'Scenario:' for more concrete test documentation"

# For Feature format  
"Feature-level docstring detected. Consider 'Example:' for individual test cases"

# For missing structure
"Add 'Given:' context and 'When:' action to complete the test scenario"
```

### suggest_example_format(docstring: str) -> str
Convert other formats to preferred Example format:
```python
# Input: Scenario-based
original = """
Scenario: User login
Given: Valid credentials
When: Login submitted
Then: Access granted
"""

# Output: Example-based suggestion
suggested = suggest_example_format(original)
# """
# Example: User login validation
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

### Prefer Example Format
When creating new tests, guide developers toward Example format:
- More concrete and illustrative
- Clearly shows what the test demonstrates
- Better documentation value
- Easier to understand for stakeholders

### Suggestion Messages
```python
# For Scenario format
"Consider using 'Example:' instead of 'Scenario:' for more concrete test documentation"

# For Feature format  
"Feature-level docstring detected. Consider 'Example:' for individual test cases"

# For missing structure
"Add 'Given:' context and 'When:' action to complete the test scenario"
```

## Manual Validation Checklist

When reviewing test files manually, check:

1. **Newline Formatting**
   - Docstrings must start with newline: `"""\n`
   - Docstrings must end with newline: `\n"""`

2. **Gherkin Keywords**
   - Use Example:, Given:, When:, Then:, And:, But:
   - Feature: and Scenario: also valid
   - Each keyword must have content after the colon

3. **Format Preference**
   - Guide toward Example format for new tests
   - Accept Scenario and Feature formats as alternatives
   - Provide suggestions for improvement

4. **Structure Validation**
   - At minimum: Given/When/Then structure
   - Preferred: Complete Example with Given/When/Then
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