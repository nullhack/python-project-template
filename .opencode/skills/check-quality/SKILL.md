---
name: check-quality
description: Enforce code quality using ruff, pytest coverage, and static type checking
version: "2.1"
author: software-engineer
audience: software-engineer, system-architect
workflow: feature-lifecycle
---

# Check Quality

Quick reference for the software-engineer quality gate before handing off to the system-architect (Step 4).

**For the full verification protocol used by the system-architect, load `skill verify`.**

## When to Use

Load this skill when completing Step 3 and preparing to hand off to the system-architect. Run all four commands; all must pass before signalling handoff.

## Step-by-Step

```bash
uv run task lint                # ruff check + ruff format — must exit 0
uv run task static-check        # pyright — must exit 0, 0 errors
uv run task test                # pytest with coverage — must exit 0, 100% coverage
timeout 10s uv run task run     # app starts — must exit non-124
```

All four must pass. Do not hand off broken work.

## Checklist

- [ ] `lint` exits 0 (ruff check + ruff format)
- [ ] `static-check` exits 0, 0 pyright errors
- [ ] `test` exits 0, 100% coverage
- [ ] `run` exits non-124 (not hung)
- [ ] No `noqa` or `type: ignore` — fix the underlying issue
