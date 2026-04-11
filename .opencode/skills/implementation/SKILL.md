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

## Implementation Strategy

- Implement one method/function at a time
- Use test data embedded in test files (copied from prototypes)
- Ensure all tests pass after each method completion
- Follow the designed signatures exactly
- Maintain code quality standards throughout

## Using Test Data

After prototype phase:
1. Test data is embedded directly in test files
2. Implementation uses this test data to validate correctness
3. Prototype directory has been deleted

For test data patterns, see: [Reference: Test Patterns](../reference/test-patterns.md)

## Red-Green-Refactor Cycle

1. **RED**: Tests are already written and failing
2. **GREEN**: Implement minimal code to pass the test
3. **REFACTOR**: Improve implementation while keeping tests green

## Method-by-Method Implementation

Implement one method at a time:
1. Start with constructor/\_\_init\_\_
2. Implement one public method
3. Run tests - should pass for this method
4. Continue to next method

## Quality Gates After Each Method

After implementing each method, verify:
- All related tests pass
- Code coverage remains at target level
- No linting errors introduced
- Type checking passes

## Running Tests

```bash
# Run tests after implementing each method
task test

# Check coverage
task test --cov

# Run linting
task lint

# Run type checking
task static-check
```

## Implementation Checklist

✅ **Before starting each method:**
- Understand what tests expect this method to do
- Review test data for expected values

✅ **After completing each method:**
- Run tests - should pass for this method
- Check code coverage hasn't dropped
- Run linting - should pass
- Verify type checking passes

✅ **After completing all methods:**
- All tests pass
- Coverage meets minimum requirement
- Linting passes
- Type checking passes
