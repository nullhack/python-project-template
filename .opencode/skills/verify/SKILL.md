---
name: verify
description: Step 4 — adversarial design review and Step 4B — completion verification
version: "7.0"
author: system-architect
audience: system-architect
workflow: feature-lifecycle
---

# Verify

Two-phase adversarial verification. The system-architect reviews design (Step 4) and completion (Step 4B) as separate passes with separate handoffs.

## Critical Rules

1. **Fail-fast**: Stop at the first failure. Write a minimal REJECTED report. Do not accumulate issues.
2. **SA never fixes code**: The only outputs are APPROVED or REJECTED reports. Never edit, create, or modify any file.
3. **Priority order**: Design correctness > self-declaration audit > feature verification > coverage > quality tooling

## When to Use

Load this skill when the software-engineer signals Step 3A complete (design review) or Step 3B complete (completion verification).

---

## Step 4 — Design Verification

### 1. Read the Feature Docs

| Read | Why |
|---|---|
| In-progress `.feature` file | All `@id` tags, Example titles, interaction model |
| `docs/system.md` | Current-state overview and Domain Model — verify naming consistency |
| `docs/glossary.md` | Verify domain terms are used correctly |
| SE Design Self-Declaration | Communicated verbally in the handoff message |

Read specific ADR files on demand only — reference Key Decisions in `system.md` first.

### 2. pyproject.toml Gate

```bash
git diff main -- pyproject.toml
```

Any change → REJECT immediately.

### 3. Branch Gate

```bash
git branch --show-current    # must be feat/<stem> or fix/<stem>
git log main..HEAD --oneline  # must show 1+ commits
git merge-tree $(git merge-base HEAD main) HEAD main  # must be empty (no conflicts)
```

### 4. Commit History

```bash
git log --oneline -20
git status
```

Verify: conventional commit format, no "fix tests" / "wip" / "temp" commits, no uncommitted changes.

### 5. Feature Verification

Choose the appropriate check for the feature type:

| Feature Type | Verification |
|---|---|
| CLI | `timeout 10s uv run task run` — must exit 0 or non-124; output must change when input changes |
| Library | `uv run python -c "import <package>; <public_api_call>"` — must import and call without error |
| Mixed | Both CLI and library checks |

If any check FAILS → REJECT immediately.

### 6. Self-Declaration Audit

**Completeness check (hard gate)**: Verify every claim is present and numbered. Missing or empty → REJECT immediately.

For every AGREE claim: find the `file:line` and verify it holds.
For every DISAGREE claim: read the justification. Accept if outside SE's control; REJECT if weak or missing.

See [[software-craft/self-declaration]] for the full audit protocol.

### 7. Design Review

Read the source files changed in this feature. **Do this before running any commands.**

**Stop on first failure category — do not accumulate issues.**

See [[software-craft/verification-philosophy]] for adversarial review principles.

#### 7a. Correctness

| Check | PASS | FAIL |
|---|---|---|
| No dead code | None found | Any found → remove or fix |
| No duplicate logic (DRY) | None found | Duplication found → extract |
| No over-engineering (YAGNI) | None found | Unused abstraction → remove |

#### 7b. Simplicity (KISS)

| Check | PASS | FAIL |
|---|---|---|
| Functions do one thing | Can describe without "and" | Split |
| Nesting ≤ 2 levels | ≤ 2 | > 2 → extract |
| Functions ≤ 20 lines | ≤ 20 | > 20 → extract |
| Classes ≤ 50 lines | ≤ 50 | > 50 → split |

#### 7c. Naming Consistency

| Check | PASS | FAIL |
|---|---|---|
| Classes match domain model | New names appear in `system.md` or justified | REJECT |
| Methods match glossary | Terms from `glossary.md` used | REJECT |
| No invented synonyms | Same concept uses same name everywhere | REJECT |

#### 7d. SOLID — see [[software-craft/solid]]

#### 7e. Object Calisthenics — see [[software-craft/object-calisthenics]]

For OC-9 (Tell, Don't Ask): run `grep -rn "@property\|def get_\|def set_" <package>/` to find getter/setter patterns, then manually review for Ask-pattern violations. "No getter/setter patterns found" is a conclusion, not evidence.

#### 7f. Design Patterns — see [[software-craft/design-patterns]]

#### 7g. Tests — see [[software-craft/test-conventions]] and [[software-craft/test-design]]

### Design Review Decision

If any check in 7a–7g FAILS → **REJECTED**. Back to Step 3A.

If all checks PASS → **APPROVED**. Signal `step-3b-ready` and update the session file in `.flowr/sessions/`.

---

## Step 4B — Completion Verification

Start only after Step 4 (Design Verification) is APPROVED and Step 3B (Completion) handoff is received.

### 8. Coverage Gate

```bash
uv run task test-coverage
```

Must meet the threshold configured in `pyproject.toml`. If below → REJECT: instruct SE to add `tests/unit/` tests for uncovered branches (NOT `@id` tests).

### 9. Run Verification Commands

```bash
uv run task lint
uv run task static-check
uv run task test
```

Expected: exit 0, no errors. Record exact output on failure. If a command fails, stop and REJECT immediately.

### 10. Interactive Verification

If the feature involves user interaction: run the app, provide real input, verify output changes. Record input and output.

### 11. Write the Report

```markdown
## Step 4B Completion Verification Report — <feature-stem>

### Coverage Gate
| Check | Result | Notes |
|---|---|---|
| Coverage threshold met | PASS / FAIL | % |

### Commands
| Command | Result | Notes |
|---|---|---|
| uv run task lint | PASS / FAIL | |
| uv run task static-check | PASS / FAIL | |
| uv run task test | PASS / FAIL | |

### Interactive Verification
| Check | Result | Notes |
|---|---|---|
| (if applicable) | PASS / FAIL / N/A | |

### Decision
**APPROVED** — all gates passed
OR
**REJECTED** — fix the following:
1. `<file>:<line>` — <specific, actionable fix>

### Next Steps
**If APPROVED**: Run `@product-owner` — accept the feature at Step 5.
**If REJECTED**: Run `@software-engineer` — apply the fixes, re-run Quality Gate B, update Completion Declaration, then signal Step 4B again.
```

---

## Step 4 Report Template (Design Review)

```markdown
## Step 4 Design Verification Report — <feature-stem>

### pyproject.toml Gate
| Check | Result | Notes |
|---|---|---|
| No changes from main | PASS / FAIL | |

### Branch Gate
| Check | Result | Notes |
|---|---|---|
| On feat/<stem> or fix/<stem> | PASS / FAIL | |
| Commits ahead of main | PASS / FAIL | |
| No merge conflicts with main | PASS / FAIL | |

### Feature Verification
| Feature Type | Result | Notes |
|---|---|---|
| (CLI/Library/Mixed) | PASS / FAIL | |

### Self-Declaration Audit
Completeness: PASS / FAIL
(See [[software-craft/self-declaration]] for the full checklist)

### Design Review
(Report each sub-check: 7a through 7g)

### Architect Review Stance Declaration

As a system-architect I declare:
* Adversarial: I actively tried to find a failure mode — AGREE/DISAGREE | note:
* Architecture preservation: stubs, Protocols, and ADR decisions respected — AGREE/DISAGREE | violations:
* Manual trace: I traced at least one execution path manually — AGREE/DISAGREE | path:
* Boundary check: I checked edge cases of every Rule — AGREE/DISAGREE | gaps:
* Semantic read: tests match their ACs — AGREE/DISAGREE | mismatches:
* Independence: verdict not influenced by effort spent — AGREE/DISAGREE

### Decision
**APPROVED** — all design checks passed, signal `step-3b-ready`
OR
**REJECTED** — fix the following:
1. `<file>:<line>` — <specific, actionable fix>

### Next Steps
**If APPROVED**: Signal `step-3b-ready`. SE proceeds to Step 3B (Completion).
**If REJECTED**: SE returns to Step 3A TDD loop to address failures.
```