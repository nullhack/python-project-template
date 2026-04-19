---
name: verify
description: Step 4 — run all verification commands, review code quality, and produce a written report
version: "4.0"
author: reviewer
audience: reviewer
workflow: feature-lifecycle
---

# Verify

This skill guides the reviewer through Step 4: independent verification that the feature works correctly and meets quality standards. The output is a written report with a clear APPROVED or REJECTED decision.

**Your default hypothesis is that the code is broken despite passing automated checks. Your job is to find the failure mode. If you cannot find one after thorough investigation, APPROVE. If you find one, REJECTED.**

**Every PASS/FAIL cell must have evidence.** Empty evidence = UNCHECKED = REJECTED.

**You never move `.feature` files.** After producing an APPROVED report: update TODO.md `Next:` to `Run @product-owner — accept feature <name> at Step 5.` then stop. The PO accepts the feature and moves the file.

## When to Use (Step 4)

After the software-engineer signals Step 3 is complete and all self-verification checks pass. Do not start verification until the software-engineer has committed all work and communicated the Self-Declaration verbally in the handoff message.

The reviewer produces one written report (see template below) that includes: all gate results, the SE Self-Declaration Audit, the **Reviewer Stance Declaration**, and the final APPROVED/REJECTED verdict.

## Step-by-Step

### 1. Read the Feature Docs

Read `docs/features/in-progress/<name>.feature`. Extract:
- All `@id` tags and their Example titles from `Rule:` blocks
- The interaction model (if the feature involves user interaction)
- The architectural decisions in `docs/architecture.md` relevant to this feature
- The software-engineer's Self-Declaration (communicated verbally in the handoff message)

### 2. pyproject.toml Gate

```bash
git diff main -- pyproject.toml
```

Any change → REJECT immediately. The software-engineer must revert and get stakeholder approval.

### 3. Check Commit History

```bash
git log --oneline -20
git status
```

Verify:
- Commits follow conventional commit format
- No "fix tests", "wip", "temp" commits
- No uncommitted changes: `git status` should be clean

### 4. Production-Grade Gate

Run before code review. If any row is FAIL, stop immediately with REJECTED.

| Check | How to check | PASS | FAIL | Fix |
|---|---|---|---|---|
| App exits cleanly | `timeout 10s uv run task run` | Exit 0 or non-124 | Exit 124 (timeout/hang) | Fix the hang |
| Output changes when input changes | Run app, change an input or condition, observe output | Output changes accordingly | Output is static | Implement real logic |

### 5. Self-Declaration Audit

Read the software-engineer's Self-Declaration from the handoff message.

For every **AGREE** claim:
- Find the `file:line` — does it hold?

For every **DISAGREE** claim:
- Read the justification carefully.
- If the constraint genuinely falls outside the SE's control (e.g. external library forces method chaining, dataclass/Pydantic/TypedDict exemption for ≤2 ivars): accept with a note in the report and suggest the closest compliant alternative if one exists.
- If the justification is weak, incomplete, or a best-practice alternative exists that the SE did not consider: REJECT with the specific alternative stated.
- If there is no justification: REJECT.

Undeclared violations found during code review → REJECT.

### 6. Code Review

Read the source files changed in this feature. **Do this before running lint/static-check/test** — if code review finds a design problem, commands will need to re-run after the fix anyway.

**Stop on first failure category — do not accumulate issues.**

#### 6a. Correctness — any FAIL → REJECTED

| Check | How to check | PASS | FAIL | Fix |
|---|---|---|---|---|
| No dead code | Read for unreachable statements, unused variables, impossible branches | None found | Any found | Remove or fix |
| No duplicate logic (DRY) | Search for repeated blocks doing the same thing | None found | Duplication found | Extract to shared function |
| No over-engineering (YAGNI) | Check for abstractions with no current use | None found | Unused abstraction | Remove unused code |

#### 6b. Simplicity (KISS) — any FAIL → REJECTED

| Check | How to check | PASS | FAIL | Fix |
|---|---|---|---|---|
| Functions do one thing | Read each function; can you describe it without `and`? | Yes | No | Split into focused functions |
| Nesting ≤ 2 levels | Count indent levels in each function | ≤ 2 | > 2 | Extract inner block |
| Functions ≤ 20 lines | Count lines | ≤ 20 | > 20 | Extract helper |
| Classes ≤ 50 lines | Count lines | ≤ 50 | > 50 | Split class |

#### 6c. SOLID — any FAIL → REJECTED

| Principle | Why it matters | What to check | How to check |
|---|---|---|---|
| SRP | Multiple change-reasons accumulate bugs | Each class/function has one reason to change | Count distinct concerns |
| OCP | Modifying existing code invalidates tests | New behavior via extension, not modification | Check if adding new case required editing existing class |
| LSP | Substitution failures cause silent errors | Subtypes behave identically to base | Check for narrowed contracts |
| ISP | Fat interfaces force unused methods | No Protocol forces stub implementations | Check for NotImplementedError |
| DIP | Concrete I/O makes unit testing impossible | High-level depends on abstractions | Check domain imports no I/O/DB |

#### 6d. Object Calisthenics — any FAIL → REJECTED

Load `skill design-patterns` and apply the full OC checklist (9 rules). Record a PASS/FAIL with `file:line` evidence for each rule. Rules 1 and 7 (nesting and entity size) share thresholds with 6b above.

#### 6e. Design Patterns — any FAIL → REJECTED

| Code smell | Pattern missed | How to check |
|---|---|---|
| Multiple if/elif on type/state | State or Strategy | Search for `isinstance` chains |
| Complex `__init__` | Factory or Builder | Check line count and side effects |
| Callers know multiple components | Facade | Check caller coupling |
| External dep without Protocol | Repository/Adapter | Check dep injection |
| 0 domain classes, many functions | Missing domain model | Count classes vs functions |

#### 6f. Tests — any FAIL → REJECTED

| Check | How to check | PASS | FAIL |
|---|---|---|---|
| Docstring format | Read each test docstring | Given/When/Then only | Extra metadata |
| Contract test | Would test survive internal rewrite? | Yes | No |
| No internal attribute access | Search for `_x` in assertions | None found | `_x`, `isinstance`, `type()` |
| Every `@id` has a mapped test | Match `@id` to test functions | All mapped | Missing test |
| No orphaned skipped stubs | Search for `@pytest.mark.skip` in `tests/features/` | None found | Any found — stub was written but never implemented |
| Function naming | Matches `test_<feature_slug>_<8char_hex>` | All match | Mismatch |
| Hypothesis tests have `@slow` | Read every `@given` for `@slow` marker | All present | Any missing |

#### 6g. Code Quality — any FAIL → REJECTED

| Check | How to check | PASS | FAIL |
|---|---|---|---|
| No `noqa` comments | `grep -r "noqa" <package>/` | None found | Any found |
| No `type: ignore` | `grep -r "type: ignore" <package>/` | None found | Any found |
| Public functions have type hints | Read signatures | All annotated | Missing |
| Public functions have docstrings | Read source | Google-style | Missing |

### 7. Run Verification Commands

```bash
uv run task lint
uv run task static-check
uv run task test
```

Expected for each: exit 0, no errors. Record exact output on failure.

If a command fails, stop and REJECT immediately. Do not run subsequent commands.

### 8. Interactive Verification

If the feature involves user interaction: run the app, provide real input, verify output changes.

Record what input was given and what output was observed.

### 8. Self-Declaration Audit

Read the software-engineer's Self-Declaration from the handoff message.

For every **AGREE** claim:
- Find the `file:line` — does it hold?

For every **DISAGREE** claim:
- REJECT — the software-engineer must fix before requesting review again.

Undeclared violations → REJECT.

### 9. Write the Report

```markdown
## Step 4 Verification Report — <feature-name>

### pyproject.toml Gate
| Check | Result | Notes |
|---|---|---|
| No changes from main | PASS / FAIL | |

### Production-Grade Gate
| Check | Result | Notes |
|---|---|---|
| App exits cleanly | PASS / FAIL / TIMEOUT | |
| Output driven by input | PASS / FAIL | |

### Commands
| Command | Result | Notes |
|---------|--------|-------|
| uv run task lint | PASS / FAIL | |
| uv run task static-check | PASS / FAIL | |
| uv run task test | PASS / FAIL | |

### Self-Declaration Audit
| Claim | Software-Engineer Claims | Reviewer Verdict | Evidence |
|------|-------------------------|------------------|----------|
| YAGNI | AGREE/DISAGREE | PASS/FAIL | |
| KISS | AGREE/DISAGREE | PASS/FAIL | |
| DRY | AGREE/DISAGREE | PASS/FAIL | |
| SOLID-S | AGREE/DISAGREE | PASS/FAIL | |
| SOLID-O | AGREE/DISAGREE | PASS/FAIL | |
| SOLID-L | AGREE/DISAGREE | PASS/FAIL | |
| SOLID-I | AGREE/DISAGREE | PASS/FAIL | |
| SOLID-D | AGREE/DISAGREE | PASS/FAIL | |
| OC-1 | AGREE/DISAGREE | PASS/FAIL | |
| OC-2 | AGREE/DISAGREE | PASS/FAIL | |
| OC-3 | AGREE/DISAGREE | PASS/FAIL | |
| OC-4 | AGREE/DISAGREE | PASS/FAIL | |
| OC-5 | AGREE/DISAGREE | PASS/FAIL | |
| OC-6 | AGREE/DISAGREE | PASS/FAIL | |
| OC-7 | AGREE/DISAGREE | PASS/FAIL | |
| OC-8 | AGREE/DISAGREE | PASS/FAIL | |
| OC-9 | AGREE/DISAGREE | PASS/FAIL | |
| Patterns Creational | AGREE/DISAGREE | PASS/FAIL | |
| Patterns Structural | AGREE/DISAGREE | PASS/FAIL | |
| Patterns Behavioral | AGREE/DISAGREE | PASS/FAIL | |
| Semantic | AGREE/DISAGREE | PASS/FAIL | |

### Reviewer Stance Declaration

Write this block **before** the Decision. Every `DISAGREE` must include an inline explanation. A `DISAGREE` with no explanation auto-forces `REJECTED`.

```markdown
## Reviewer Stance Declaration
As a reviewer I declare:
* Adversarial: I actively tried to find a failure mode, not just confirm passing — AGREE/DISAGREE | note:
* Manual trace: I traced at least one execution path manually beyond automated output — AGREE/DISAGREE | path:
* Boundary check: I checked the boundary conditions and edge cases of every Rule — AGREE/DISAGREE | gaps:
* Semantic read: I read each test against its AC and confirmed it tests the right observable behavior — AGREE/DISAGREE | mismatches:
* Independence: my verdict was not influenced by how much effort has already been spent — AGREE/DISAGREE
```

### Decision
**APPROVED** — all gates passed, no undeclared violations
OR
**REJECTED** — fix the following:
1. `<file>:<line>` — <specific, actionable fix>

### Next Steps
**If APPROVED**: Run `@product-owner` — accept the feature at Step 5.
**If REJECTED**: Run `@software-engineer` — apply the fixes listed above, re-run quality gate, update Self-Declaration, then signal Step 4 again.
```


