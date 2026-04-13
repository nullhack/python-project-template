---
name: gherkin-validation
description: Validate BDD docstrings with UUID format preference and proper Gherkin syntax
license: MIT
compatibility: opencode
metadata:
  audience: developers
  workflow: quality-assurance
---

## What I do
Validate BDD docstrings in test functions using UUID format for traceability. Ensure proper newline formatting and provide helpful suggestions.

## When to use me
- During TDD phase to validate test docstring formats
- In QA enforcement to check BDD compliance
- When reviewing test files for documentation standards
- As part of automated quality checks

## Required Format: UUID-based Traceability

All test docstrings MUST use acceptance criteria UUID for traceability:

```python
def test_user_login_with_valid_credentials_should_grant_access():
    """123e4567-e89b-12d3-a456-426614174000: Successful user authentication.

    Given: A registered user with valid credentials exists in the system  
    When: The user submits correct username and password
    Then: Access should be granted to the application
    """
```

### Structure
- UUID followed by colon and brief description (ends with period)
- Blank line after description
- Gherkin steps: Given/When/Then with mandatory newlines
- Each step on its own line

### Extended Gherkin Keywords
All valid Gherkin keywords are supported:
- **Given**: Preconditions or context
- **When**: Action or trigger
- **Then**: Expected outcome
- **And**: Additional conditions
- **But**: Contradiction conditions

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

## Validation Guidelines

### Docstring Validation Checklist
- [ ] Docstring starts with newline: `"""\n`
- [ ] Docstring ends with newline before closing quotes
- [ ] Valid Gherkin keywords present (Given, When, Then, etc.)
- [ ] Keywords followed by meaningful content (not empty)
- [ ] Proper colon after each keyword

### Suggestion Messages
For improving docstrings to required UUID format:
```python
# For missing UUID
"Test docstring must start with acceptance criteria UUID for traceability"

# For missing structure
"Add 'Given:' context and 'When:' action to complete the test scenario"
```

### suggest_uuid_format(docstring: str) -> str
Convert legacy formats to required UUID format:
```python
# Input: Legacy format
original = """
User login validation.
Given: Valid credentials
When: Login submitted
Then: Access granted
"""

# Output: UUID-based format
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
  strictness: "uuid_required"  # "uuid_required", "accept_any"
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
4. **Validate UUID traceability** format
5. **Generate suggestions** if not using required UUID format
6. **Report results** with specific improvement guidance

Remember: All test docstrings MUST use UUID traceability format.