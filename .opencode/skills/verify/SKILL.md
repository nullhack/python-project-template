---
name: verify
description: Step 4 — run all verification commands, review code quality, and produce a written report
version: "6.0"
author: system-architect
audience: system-architect
workflow: feature-lifecycle
---

# Verify

This skill guides the system-architect through Step 4: adversarial verification that the feature works correctly and respects the architecture designed in Step 2. The output is a written report with a clear APPROVED or REJECTED decision.

**Your default hypothesis is that the code is broken despite passing automated checks. You designed the architecture; you know what should have been preserved. Your job is to find the failure mode. If you cannot find one after thorough investigation, APPROVE. If you find one, REJECTED.**

**Every PASS/FAIL cell must have evidence.** Empty evidence = UNCHECKED = REJECTED.

**You never move, create, or edit `.feature` files.** After producing an APPROVED report: update the session file in `.flowception/` `state` to `step-5-ready` then stop. The PO accepts the feature and moves the file.

The system-architect produces one written report (see template below) that includes: all gate results, the SE Self-Declaration Audit, the **Architect Review Stance Declaration**, and the final APPROVED/REJECTED verdict. Do not start until the software-engineer has committed all work and communicated the Self-Declaration verbally in the handoff message.

## When to Use

Load this skill when the software-engineer signals Step 3 complete and hands off for review (Step 4). Do not load it earlier.

## Step-by-Step

### 1. Read the Feature Docs

**Required reads**:

| Read | Why |
|---|---|
| In-progress `.feature` file | All `@id` tags, Example titles, interaction model |
| `docs/system.md` | Current-state overview and Domain Model — verify naming consistency |
| `docs/glossary.md` | Verify domain terms are used correctly |
| SE Self-Declaration | Communicated verbally in the handoff message |

Read specific ADR files on demand only — reference Key Decisions in `system.md` first, then read individual ADRs when a decision needs deeper scrutiny.

### 2. pyproject.toml Gate

```bash
git diff main -- pyproject.toml
```

Any change → REJECT immediately. The software-engineer must revert and get stakeholder approval.

### 3. Branch Gate

```bash
git branch --show-current
```

- Must output `feat/<stem>` or `fix/<stem>`. If `main` → REJECT immediately — the SE is working on the wrong branch.

```bash
git log main..HEAD --oneline
```

- Must show 1+ commits. If empty → REJECT — nothing was committed on this branch.

```bash
git merge-tree $(git merge-base HEAD main) HEAD main
```

- Empty output = clean merge possible. Non-empty output = conflicts exist → REJECT — the SE must resolve conflicts on the feature branch before handoff.

### 4. Check Commit History

```bash
git log --oneline -20
git status
```

Verify:
- Commits follow conventional commit format
- No "fix tests", "wip", "temp" commits
- No uncommitted changes: `git status` should be clean

### 5. Production-Grade Gate

Run before semantic review. If any row is FAIL, stop immediately with REJECTED.

| Check | How to check | PASS | FAIL | Fix |
|---|---|---|---|---|
| App exits cleanly | `timeout 10s uv run task run` | Exit 0 or non-124 | Exit 124 (timeout/hang) | Fix the hang |
| Output changes when input changes | Run app, change an input or condition, observe output | Output changes accordingly | Output is static | Implement real logic |

### 6. Self-Declaration Audit

**Completeness check (hard gate — REJECT if failed)**: Verify that every claim in the SE's Self-Declaration is present and numbered. If any claim is missing, or the declaration is empty, REJECT immediately — do not proceed to item-level audit.

Read the software-engineer's Self-Declaration from the handoff message.

For every **AGREE** claim:
- Find the `file:line` — does it hold?

For every **DISAGREE** claim:
- Read the justification carefully.
- If the constraint genuinely falls outside the SE's control (e.g. external library forces method chaining, dataclass/Pydantic/TypedDict exemption for ≤2 ivars): accept with a note in the report and suggest the closest compliant alternative if one exists.
- If the justification is weak, incomplete, or a best-practice alternative exists that the SE did not consider: REJECT with the specific alternative stated.
- If there is no justification: REJECT.

Undeclared violations found during semantic review → REJECT.

See [[software-craft/self-declaration]] for the full Self-Declaration audit checklist.

### 7. Code Review

Read the source files changed in this feature. **Do this before running lint/static-check/test** — if semantic review finds a design problem, commands will need to re-run after the fix anyway.

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

#### 6c. Naming Consistency — any FAIL → REJECTED

| Check | How to check | PASS | FAIL |
|---|---|---|---|
| Classes match domain model | New class names appear in the `## Domain Model` section of `docs/system.md` or are justified | Yes | No |
| Methods match glossary | New method names use terms from `docs/glossary.md` | Yes | No |
| No invented synonyms | Same concept uses same name everywhere | Yes | No |

If a new name is genuinely needed (not in domain model or glossary), the SE should have noted it in the handoff summary or in the `.feature` file's `## Changes` section. If no justification exists, REJECT.

#### 6d. SOLID — any FAIL → REJECTED

See [[software-craft/solid]] for the SOLID review checklist.

#### 6e. Object Calisthenics — any FAIL → REJECTED

Load `skill apply-patterns` and apply the full OC checklist (9 rules). Record a PASS/FAIL with `file:line` evidence for each rule. Rules 1 and 7 (nesting and entity size) share thresholds with 6b above.

See [[software-craft/object-calisthenics]] for the full OC rules.

#### 6f. Design Patterns — any FAIL → REJECTED

See [[software-craft/design-patterns]] for the pattern smell checklist.

#### 6g. Tests — any FAIL → REJECTED

See [[software-craft/test-conventions]] for the test review checklist.

See [[software-craft/test-design]] for refactor-safe test design principles — tests must not be coupled to implementation details.

#### 6h. Code Quality — any FAIL → REJECTED

See [[software-craft/code-quality]] for the code quality checklist.

### 8. Run Verification Commands

```bash
uv run task lint
uv run task static-check
uv run task test
```

Expected for each: exit 0, no errors. Record exact output on failure.

If a command fails, stop and REJECT immediately. Do not run subsequent commands.

### 9. Interactive Verification

If the feature involves user interaction: run the app, provide real input, verify output changes.

Record what input was given and what output was observed.

### 10. Write the Report

```markdown
## Step 4 Verification Report — <feature-stem>

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
| uv run task test-coverage | PASS / FAIL | |

### Naming Consistency
| Check | Result | Notes |
|---|---|---|
| Classes match domain model | PASS / FAIL | |
| Methods match glossary | PASS / FAIL | |
| No invented synonyms | PASS / FAIL | |

### Self-Declaration Audit
See [[software-craft/self-declaration]] for the full checklist. Record each claim with SE verdict and reviewer verdict with evidence.

### Architect Review Stance Declaration

Write this block **before** the Decision. Every `DISAGREE` must include an inline explanation. A `DISAGREE` with no explanation auto-forces `REJECTED`.

As a system-architect I declare:
* Adversarial: I actively tried to find a failure mode, not just confirm passing — AGREE/DISAGREE | note:
* Architecture preservation: I verified that stubs, Protocols, and ADR decisions from Step 2 were respected — AGREE/DISAGREE | violations:
* Manual trace: I traced at least one execution path manually beyond automated output — AGREE/DISAGREE | path:
* Boundary check: I checked the boundary conditions and edge cases of every Rule — AGREE/DISAGREE | gaps:
* Semantic read: I read each test against its AC and confirmed it tests the right observable behaviour — AGREE/DISAGREE | mismatches:
* Independence: my verdict was not influenced by how much effort has already been spent — AGREE/DISAGREE

### Decision
**APPROVED** — all gates passed, no undeclared violations
OR
**REJECTED** — fix the following:
1. `<file>:<line>` — <specific, actionable fix>

### Next Steps
**If APPROVED**: Run `@product-owner` — accept the feature at Step 5.
**If REJECTED**: Run `@software-engineer` — apply the fixes listed above, re-run quality gate, update Self-Declaration, then signal Step 4 again.
```