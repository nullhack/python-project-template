# Post-Mortem: ping-pong-cli — Package Directory and Design Review Gaps

## Context

| Field | Value |
|-------|-------|
| Date | April 16, 2026 |
| Feature | ping-pong-cli (follow-up run after v3.1 workflow fixes) |
| Branch | feat/po-workflow-redesign-v4 |

This post-mortem was conducted after a second ping-pong-cli test run on the updated v3.1 workflow. Two systemic failures were identified that the v3.1 fixes did not address.

---

## Failure 1: Code Created in Wrong Package Directory

### What Happened

The developer created production code under `python_project_template/` (the template's own package) instead of `ping_pong_cli/` (the feature's package). The correct package name was visible in `pyproject.toml` under `[tool.setuptools] packages`, but no step in the workflow required the developer to read it before writing code.

### Why It Happened

The `implementation` skill's Step 2 (Architecture) listed prerequisites and module structure instructions, but contained no explicit step to:
1. Read `pyproject.toml` to determine the correct package name
2. Confirm the package directory exists on disk
3. Record the package name as a hard constraint before writing any files

Without this verification, the developer defaulted to a plausible-looking name rather than the actual configured name.

### Impact

All production code was placed in the wrong directory. The feature appeared to work during development (imports resolved within the wrong package) but would have failed on any fresh install or CI run.

### Fix Applied

Added a **Package Verification** block at the top of Step 2 in `implementation/SKILL.md` (before prerequisites):

```
1. Read pyproject.toml → [tool.setuptools] → record packages = ["<name>"]
2. Confirm that directory exists on disk: ls <name>/
3. Write the correct package name at the top of working notes
4. All new source files go under <name>/ — never under a template placeholder
```

Added a corresponding check row to `verify/SKILL.md` section 4g:

> `Imports use correct package name` — confirm all imports match `[tool.setuptools] packages`, not a template placeholder

---

## Failure 2: Design Principle Violations Not Caught in Review

### What Happened

The reviewer approved code containing getters and setters (`get_x()` / `set_x()` pairs), violating Object Calisthenics Rule 9. The violation was visible in the code but was not caught because the review process had no structured mechanism for the developer to declare their own compliance before asking for review.

### Why It Happened

The per-test reviewer check asked the reviewer to verify YAGNI > KISS > DRY > SOLID > ObjCal, but provided no structured checklist or required evidence format. The reviewer was scanning for violations rather than verifying explicit claims. When a reviewer is reading unfamiliar code for the first time, getter/setter patterns can be overlooked if they are not explicitly flagged.

Additionally, the reviewer had no "audit target" — there was nothing the developer had committed to that the reviewer could directly compare against the code.

### Impact

OC Rule 9 (tell-don't-ask) was violated. The design choice propagated into the committed codebase, requiring a later refactor.

### Fix Applied

Added a **Design Self-Declaration** step between REFACTOR and REVIEWER CHECK in `implementation/SKILL.md`:

- Developer fills a checklist covering YAGNI, KISS, DRY, SOLID (all 5 principles), and OC Rules 1–9
- Each item requires `file:line` evidence or an explicit "does not apply" note
- The filled checklist is sent to the reviewer as the audit target

Updated the **REVIEWER CHECK** response template from a 3-line compact format to an 11-row structured comparison table (YAGNI, KISS, DRY, SOLID-S/O/L/I/D, OC-1-9, Design patterns, Semantic alignment):

- Developer Claims column (what the developer declared)
- Reviewer Verdict column (independent verification)
- Evidence column (`file:line` required for every FAIL)
- Any FAIL row = rejection

Updated the Cycle State phases to include `SELF-DECLARE` between REFACTOR and REVIEWER:

```
RED → GREEN → REFACTOR → SELF-DECLARE → REVIEWER(code-design) → COMMITTED
```

Updated `session-workflow/SKILL.md` Cycle State phase list and Rule 6 to include `SELF-DECLARE`.

Updated `reviewer.md` per-test Step 4 section to reference the structured table and load `skill implementation` for the full protocol.

---

## Summary

| Failure | Root Cause | Fix |
|---------|-----------|-----|
| Code in wrong package | No package verification step before writing code | Package Verification block added to Step 2 |
| OC Rule 9 violation approved | No structured self-declaration; reviewer had no audit target | Design Self-Declaration checklist per test; 11-row verification table |

---

## Systemic Pattern

Both failures share the same root cause: **the workflow relied on agents noticing problems rather than proving compliance**. The fixes shift the burden:

- Package verification: developer must prove the package name is correct before writing the first line
- Design self-declaration: developer must prove each principle is satisfied before asking for review; reviewer verifies claims rather than scanning from scratch
