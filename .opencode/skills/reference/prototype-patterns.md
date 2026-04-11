---
name: Prototype Patterns
description: Guidelines for creating, using, and disposing prototype scripts
license: MIT
compatibility: opencode
metadata:
  audience: developers
  workflow: feature-development
---

## Prototype Script Guidelines

### Purpose
Prototypes are quick experiments to validate that a feature concept works and produces expected outputs. They exist temporarily to discover real data structures and behaviors before proper implementation.

### Creating Prototypes

#### When to Create
- After feature definition phase
- When you need to verify API responses, data flows, or core functionality
- When real output format is unknown and needs validation

#### Script Structure Guidelines
```python
# Basic prototype structure to follow:

#!/usr/bin/env python3
"""
Prototype script for [FEATURE_NAME]
Quick validation of core functionality
"""

# Hardcoded test data - use realistic examples
TEST_INPUT = "example data"

def prototype_main_function():
    """Quick and dirty implementation."""
    result = "mock result"  # TODO: Replace with proper implementation
    return result

if __name__ == "__main__":
    result = prototype_main_function()
    print(f"Result: {result}")
    print(f"Type: {type(result)}")
    assert result is not None
    print("✅ Prototype working!")
```

#### Common Patterns

**API Client Prototype**
- Make actual API calls
- Print response structure (keys, types, sample values)
- Capture real responses for analysis

**Data Processing Prototype**
- Test with multiple input variations
- Print transformation results
- Note edge cases discovered

**File Processing Prototype**
- Read actual files
- Extract relevant fields
- Validate output structure

### Using Prototypes

#### Running and Capturing Output
1. Run prototype: `python prototypes/<name>/prototype_<name>.py`
2. Capture console output
3. Note actual data structures returned
4. Identify edge cases and error conditions

#### Extracting Test Data
After running prototype:
1. Copy relevant output values directly into test file as fixtures/constants
2. Use exact values that prototype produced
3. Note expected types and formats

### Disposing Prototypes (MANDATORY)

**Prototypes are disposable** - they exist only to validate an idea.

**After getting the output:**
1. Run prototype and capture output
2. Copy relevant output values directly into test file as fixtures/constants
3. **DELETE the prototype directory**: `rm -rf prototypes/<name>/`
4. Tests read from test file fixtures, NOT from prototype files

**Why**: Prototypes are quick experiments, not permanent artifacts. Tests should be self-contained and not depend on external prototype files.

### File Layout During Prototype Phase

```
prototypes/
└── <feature_name>/
    ├── FEATURE.md                    # From feature-definition skill
    ├── prototype_<feature_name>.py   # Run once, then delete
    └── results_<name>.json          # Copy values to tests, then delete
```

### File Layout After Transition to TDD

```
prototypes/                           # DELETE entire directory
tests/
└── unit/
    └── <feature_name>_test.py        # Contains test data directly
```

### Anti-Patterns to Avoid

- ❌ Loading test data from prototype files in production code
- ❌ Keeping prototype files after extracting test values
- ❌ Referencing prototype directory in test fixtures
- ❌ Using prototype scripts as part of CI/CD

### Best Practices

- ✅ Copy values to test files immediately after running prototype
- ✅ Delete prototype directory before writing implementation
- ✅ Tests are self-contained with fixtures directly in test file
- ✅ Use descriptive test names following TDD conventions
- ✅ Include property-based tests with Hypothesis for robustness
