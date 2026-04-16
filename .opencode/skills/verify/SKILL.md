---
name: verify
description: Step 5 — run all verification commands, review code quality, and produce a written report
version: "2.0"
author: reviewer
audience: reviewer
workflow: feature-lifecycle
---

# Verify

This skill guides the reviewer through Step 5: independent verification that the feature works correctly and meets quality standards. The output is a written report with a clear APPROVED or REJECTED decision.

**Your default hypothesis is that the code is broken despite passing automated checks. Your job is to find the failure mode. If you cannot find one after thorough investigation, APPROVE. If you find one, REJECTED.**

**Every PASS/FAIL cell must have evidence.** Empty evidence = UNCHECKED = REJECTED.

## When to Use

After the developer signals Step 4 is complete. Do not start verification until the developer has committed all work.

## Step-by-Step

### 1. Read the Feature Docs

Read the feature folder `docs/features/in-progress/<name>/`. Extract:
- All `@id` tags and their Example titles from `.feature` files
- The interaction model (if the feature involves user interaction)
- The developer's pre-mortem (if present in the Architecture section of `discovery.md`)
- The Rules and Constraints sections from `discovery.md`

### 2. Check Commit History

```bash
git log --oneline -20
git status
```

Verify:
- There is a commit per green test (not one giant commit at the end)
- Every step has a commit (architecture, failing tests, per-feature-name commits)
- No uncommitted changes: `git status` should be clean

### 3. Production-Grade Gate

Run before code review. If any row is FAIL, stop immediately with REJECTED.

| Check | How to check | PASS | FAIL | Fix |
|---|---|---|---|---|
| Developer declared production-grade | Read feature doc pre-mortem or handoff message | Explicit statement present | Absent or says "demo" or "incomplete" | Developer must complete the implementation |
| App exits cleanly | `timeout 10s uv run task run` | Exit 0 or non-124 | Exit 124 (timeout/hang) | Developer must fix the hang |
| Output changes when input changes | Run app, change an input or condition, observe output | Output changes accordingly | Output is static regardless of input | Developer must implement real logic |

### 4. Code Review

Read the source files changed in this feature. **Do this before running lint/static-check/test** — if code review finds a design problem, commands will need to re-run after the fix anyway.

**If any check FAILs at any stage, STOP and send back to developer.** Do not accumulate issues — stop on first failure category.

#### 4a. Correctness — any FAIL → REJECTED

| Check | How to check | PASS | FAIL | Fix |
|---|---|---|---|---|
| No dead code | Read for unreachable statements, unused variables, impossible branches | None found | Any found | Remove or fix the unreachable path |
| No duplicate logic (DRY) | Search for repeated blocks doing the same thing | None found | Duplication found | Extract to shared function |
| No over-engineering (YAGNI) | Check for abstractions with no current use | None found | Unused abstraction or premature generalization | Remove unused code |

#### 4b. Simplicity (KISS) — any FAIL → REJECTED

| Check | How to check | PASS | FAIL | Fix |
|---|---|---|---|---|
| Functions do one thing | Read each function; can you describe it without `and`? | Yes | No | Split into focused functions |
| Nesting ≤ 2 levels | Count indent levels in each function | ≤ 2 | > 2 | Extract inner block to helper |
| Functions ≤ 20 lines | Count lines | ≤ 20 | > 20 | Extract helper |
| Classes ≤ 50 lines | Count lines | ≤ 50 | > 50 | Split class |

#### 4c. SOLID — any FAIL → REJECTED

| Principle | Why it matters | What to check | How to check | PASS/FAIL | Evidence (`file:line`) |
|---|---|---|---|---|---|
| SRP | Multiple change-reasons accumulate bugs at every change site | Each class/function has one reason to change | Count distinct concerns; each `and` in its description = warning sign | | |
| OCP | Modifying existing code for new behavior invalidates existing tests | New behavior via extension, not modification | Check if adding the new case required editing existing class bodies | | |
| LSP | Substitution failures cause silent runtime errors tests miss | Subtypes behave identically to base type at all call sites | Check if any subtype narrows a contract or raises where base does not | | |
| ISP | Fat interfaces force implementors to have methods they cannot meaningfully implement | No Protocol/ABC forces unused method implementations | Check if any implementor raises `NotImplementedError` or passes on inherited methods | | |
| DIP | Depending on concrete I/O makes unit testing impossible | High-level modules depend on abstractions (Protocols) | Check if any domain class imports from I/O, DB, or framework layers directly | | |

#### 4d. Object Calisthenics — any FAIL → REJECTED

| # | Rule | Why it matters | How to check | PASS/FAIL | Evidence (`file:line`) |
|---|---|---|---|---|---|
| 1 | One indent level per method | Reduces cognitive load per function | Count max nesting in source | | |
| 2 | No `else` after `return` | Eliminates hidden control flow paths | Search for `else` inside functions with early returns | | |
| 3 | Primitives wrapped | Prevents primitive obsession; enables validation at construction | Bare `int`/`str` in domain signatures = FAIL | | |
| 4 | Collections wrapped in classes | Encapsulates iteration and filtering logic | `list[X]` as domain value = FAIL | | |
| 5 | One dot per line | Reduces coupling to transitive dependencies | `a.b.c()` chains = FAIL | | |
| 6 | No abbreviations | Names are documentation; abbreviations lose meaning | `mgr`, `tmp`, `calc` = FAIL | | |
| 7 | Small entities | Smaller units are easier to test, read, and replace | Functions > 20 lines or classes > 50 lines = FAIL | | |
| 8 | ≤ 2 instance variables | Forces single responsibility through structural constraint | Count `self.x` assignments in `__init__` | | |
| 9 | No getters/setters | Enforces tell-don't-ask; behavior lives with data | `get_x()`/`set_x()` pairs = FAIL | | |

#### 4e. Design Patterns — any FAIL → REJECTED

| Code smell | Pattern missed | Why it matters | How to check | PASS/FAIL | Evidence (`file:line`) |
|---|---|---|---|---|---|
| Multiple if/elif on type/state | State or Strategy | Eliminates conditional complexity | Search for chains of `isinstance` or string-based dispatch | | |
| Complex `__init__` with side effects | Factory or Builder | Separates construction from use | Check `__init__` line count and side effects | | |
| Callers must know multiple internal components | Facade | Single entry point reduces coupling | Check how callers interact with the subsystem | | |
| External dep without Protocol | Repository/Adapter | Enables testing without real I/O; enforces DIP | Check if the dep is injected via abstraction | | |
| 0 domain classes, many functions | Missing domain model | Procedural code has no encapsulation boundary | Count classes vs functions in domain code | | |

#### 4f. Tests — any FAIL → REJECTED

| Check | How to check | PASS | FAIL | Fix |
|---|---|---|---|---|
| Docstring format | Read each test docstring | Given/When/Then lines only (no UUID) | Extra metadata or missing G/W/T | Fix docstring to match canonical format |
| Contract test | Would this test survive a full internal rewrite? | Yes | No | Rewrite assertion to test observable output, not internals |
| No internal attribute access | Search for `_x` in assertions | None found | `_x`, `isinstance`, `type()` found | Replace with public API assertion |
| Every `@id` has a mapped test | Match `@id` tags in `.feature` files to test functions | All mapped | Missing test | Write the missing test |
| No `@id` used by two functions | Check for duplicate `@id` hex in test function names | None | Duplicate found | Consolidate into Hypothesis `@given` + `@example` or escalate to PO |
| Function naming | Test names match `test_<feature_slug>_<8char_hex>` | All match | Mismatch | Rename function |

#### 4g. Code Quality — any FAIL → REJECTED

| Check | How to check | PASS | FAIL | Fix |
|---|---|---|---|---|
| No `noqa` comments | `grep -r "noqa" <package>/` | None found | Any found | Fix the underlying issue |
| No `type: ignore` comments | `grep -r "type: ignore" <package>/` | None found | Any found | Fix the underlying type error |
| All public functions have type hints | Read signatures | All annotated | Missing hints | Add type annotations |
| All public functions have docstrings | Read source | Google-style present | Missing docstring | Add docstring |
| Coverage target matches package | Check `--cov=<package>` in test config | Matches actual package | Wrong package name | Fix the `--cov` argument |
| All declared packages exist | Check `[tool.setuptools] packages` against filesystem | All present | Missing package | Add directory or remove declaration |

### 5. Run Verification Commands (in order, stop on first failure)

```bash
uv run task lint
uv run task static-check
uv run task test
```

Expected for each: exit 0, no errors. Record exact output on failure.

### 6. Interactive Verification

If the feature involves user interaction: run the app, provide real input, verify the output changes in response. An app that produces the same output regardless of input is NOT verified.

### 7. Write the Report

```markdown
## Step 5 Verification Report — <feature-name>

### Production-Grade Gate
| Check | Result | Notes |
|---|---|---|
| Developer declared production-grade | PASS / FAIL | |
| App exits cleanly | PASS / FAIL / TIMEOUT | |
| Output driven by real logic | PASS / FAIL | |

### Commands
| Command | Result | Notes |
|---------|--------|-------|
| uv run task lint | PASS / FAIL | <details if fail> |
| uv run task static-check | PASS / FAIL | <errors if fail> |
| uv run task test | PASS / FAIL | <failures or coverage% if fail> |

### @id Traceability
| @id | Example Title | Test | Status |
|-----|---------------|------|--------|
| `@id:a3f2b1c4` | <title> | `tests/features/<name>/<story>_test.py::test_<slug>_a3f2b1c4` | COVERED / NOT COVERED |

### Code Review Findings
- PASS: <aspect>
- FAIL: `<file>:<line>` — <specific issue>

### Gap Report (if any)
- `<suggested Example text>` — reported to PO for decision

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
| Uncovered `@id` tags | 0 |
| `noqa` comments | 0 |
| `type: ignore` | 0 |
| Semantic alignment mismatches | 0 |
| SOLID FAIL rows | 0 |
| ObjCal FAIL rows | 0 |
| Design pattern FAIL rows | 0 |
| Duplicate `@id` in tests | 0 |
| Empty evidence cells | 0 |
