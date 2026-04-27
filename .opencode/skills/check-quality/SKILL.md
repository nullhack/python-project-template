---
name: check-quality
description: Pre-handoff quality checklists for the two-phase TDD process
version: "3.0"
author: software-engineer
audience: software-engineer, system-architect
workflow: feature-lifecycle
---

# Check Quality

Two checklists for the two-phase TDD process. Use the appropriate checklist before handing off to the system-architect.

**For the full verification protocol used by the system-architect, load `skill verify`.**

## When to Use

- **Pre-Design-Review Checklist**: Load before Step 3A handoff (design review)
- **Pre-Completion-Review Checklist**: Load before Step 3B handoff (completion verification)

---

## Pre-Design-Review Checklist (Step 3A handoff)

Run before handing off for Step 4 (Design Verification).

```bash
uv run task test-fast
```

Feature-type verification (choose one):

| Feature Type | Command |
|---|---|
| CLI | `timeout 10s uv run task run` |
| Library | `uv run python -c "import <package>; <public_api_call>"` |
| Mixed | Both commands above |

- [ ] `test-fast` exits 0 (all tests pass)
- [ ] Feature-type verification passes (CLI/Library/Mixed)
- [ ] Design Self-Declaration completed (25 items, verbally communicated)

**Do NOT run**: lint, static-check, test-coverage, ruff format. Those are Step 3B concerns.

---

## Pre-Completion-Review Checklist (Step 3B handoff)

Run before handing off for Step 4B (Completion Verification).

```bash
uv run task test-coverage
uv run task lint
uv run task static-check
uv run task test-fast
```

Feature-type verification (choose one):

| Feature Type | Command |
|---|---|
| CLI | `timeout 10s uv run task run` |
| Library | `uv run python -c "import <package>; <public_api_call>"` |
| Mixed | Both commands above |

- [ ] `test-coverage` exits 0, coverage meets threshold
- [ ] `lint` exits 0 (ruff check + ruff format)
- [ ] `static-check` exits 0, 0 pyright errors
- [ ] `test-fast` exits 0 (all tests pass)
- [ ] Feature-type verification passes
- [ ] No `noqa` or `type: ignore` — fix the underlying issue
- [ ] Completion Declaration completed (4 items, verbally communicated)