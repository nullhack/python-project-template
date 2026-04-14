---
name: verify
description: Step 5 — run all verification commands and review code quality, produce a written report
version: "1.0"
author: reviewer
audience: reviewer
workflow: feature-lifecycle
---

# Verify

This skill guides the reviewer through Step 5: independent verification that the feature works correctly and meets quality standards. The output is a written report with a clear APPROVED or REJECTED decision.

## When to Use

After the developer signals Step 4 is complete. Do not start verification until the developer has committed all work.

## Step-by-Step

### 1. Read the Feature Doc

Read `docs/features/in-progress/<feature-name>.md`. Extract:
- All UUIDs and their descriptions
- The test strategy for each criterion (unit/integration)

### 2. Check Commit History

```bash
git log --oneline -20
```

Verify:
- There is a commit per green test (not one giant commit at the end)
- Every step has a commit (`bootstrap`, `failing tests`, per-feature-name commits)
- No uncommitted changes: `git status` should be clean

### 3. Run Verification Commands (in order)

Run each command. Record the exact exit code and output summary.

```bash
task lint
```
Expected: exit 0, no issues. If ruff makes auto-fixes, that is a FAIL (developer should have run lint before handing off).

```bash
task static-check
```
Expected: exit 0, `0 errors, 0 warnings` from pyright.

```bash
task test
```
Expected: exit 0, all tests pass, coverage ≥ 100%.

```bash
timeout 10s task run
```
Expected: exit 0 (app completes) or any non-124 exit. **Exit code 124 means the process was killed by timeout — the app hung or is an infinite loop. This is a FAIL.** For interactive/long-running apps, check that startup completes without error before the timeout.

**If any command fails, stop here.** Record the failure and issue a REJECTED report. Do not continue checking.

### 4. UUID Traceability Check

For each acceptance criterion UUID in the feature doc:
- Find the corresponding test function using `grep -r "<uuid>" tests/`
- Verify the test function name follows `test_<condition>_should_<outcome>`
- Verify the test docstring contains the UUID on the first line

Flag any UUID with no corresponding test as UNCOVERED.

### 5. Code Review

Read the source files changed in this feature. Check:

**Correctness**
- No dead code (unreachable statements, unused variables, impossible branches)
- No duplicate logic
- No over-engineering (unused abstractions, premature generalization)

**Simplicity (KISS)**
- Functions do one thing
- Nesting no deeper than 2 levels
- Functions ≤ 20 lines
- Classes ≤ 50 lines

**SOLID**
- Single responsibility: each class/function has one reason to change
- Open/closed: new behavior via extension, not modification
- Liskov: subtypes are usable as their base types
- Interface segregation: no interface forces implementing unused methods
- Dependency inversion: high-level modules depend on abstractions

**Object Calisthenics** (check all 9)
1. One level of indentation per method
2. No `else` after `return`
3. Primitives wrapped (domain concepts use value objects, not raw strings/ints)
4. Collections wrapped in domain classes
5. One dot per line (no chaining: `a.b.c()`)
6. No abbreviations (`mgr`, `tmp`, `calc` are violations)
7. Small entities (see size limits above)
8. ≤ 2 instance variables per class
9. No getters/setters; use commands and queries

**Tests**
- Every test has UUID docstring: `<uuid>: <description>.` on the first line, blank line, then Given/When/Then
- Tests assert behavior, not structure (no `isinstance`, no `type()`, no internal attribute access)
- `# Given`, `# When`, `# Then` comments in test body
- No `pytest.skip`, no `pytest.mark.xfail` without explicit justification

**Build Consistency**
- `pyproject.toml` version matches `<package>/__version__`
- `--cov=<package>` in test config matches actual package name
- All packages listed in `[tool.setuptools] packages` exist in the codebase
- No `noqa` comments
- No `type: ignore` comments

### 6. Write the Report

```markdown
## Step 5 Verification Report — <feature-name>

### Commands
| Command | Result | Notes |
|---------|--------|-------|
| task lint | PASS / FAIL | <details if fail> |
| task static-check | PASS / FAIL | <errors if fail> |
| task test | PASS / FAIL | <failures or coverage% if fail> |
| timeout 10s task run | PASS / FAIL / TIMEOUT | <error or timeout if fail> |

### UUID Traceability
| UUID | Description | Test | Status |
|------|-------------|------|--------|
| `<uuid>` | <description> | `tests/unit/<file>:<function>` | COVERED / NOT COVERED |

### Code Review Findings
- PASS: <aspect>
- FAIL: `<file>:<line>` — <specific issue>

### Decision
**APPROVED** — work meets all standards. Developer may proceed to Step 6.
OR
**REJECTED** — fix the following before resubmitting:
1. `<file>:<line>` — <specific, actionable fix required>
```

## Standards Summary

| Check | Standard |
|---|---|
| Test coverage | 100% |
| Type errors | 0 |
| Lint errors | 0 |
| Function length | ≤ 20 lines |
| Class length | ≤ 50 lines |
| Max nesting | 2 levels |
| Instance variables | ≤ 2 per class |
| Uncovered UUIDs | 0 |
| `noqa` comments | 0 |
| `type: ignore` | 0 |
