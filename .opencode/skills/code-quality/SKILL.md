---
name: code-quality
description: Enforce code quality using ruff, pytest coverage, and static type checking
version: "2.0"
author: developer
audience: developer, reviewer
workflow: feature-lifecycle
---

# Code Quality

Run these four commands before handing off to the reviewer (Step 5). All must pass.

## Developer Self-Check

Before handing off to reviewer:

```bash
uv run task lint                # ruff check + ruff format — must exit 0
uv run task static-check        # pyright — must exit 0, 0 errors
uv run task test                # pytest with coverage — must exit 0, 100% coverage
timeout 10s uv run task run     # app starts — must exit non-124
```

All four must pass. Do not hand off broken work.

**Golden rule: never use `noqa` or `type: ignore`.** Fix the underlying issue instead.
