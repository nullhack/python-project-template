---
name: review-conventions
description: "Verify formatting, docstrings, type hints, and lint rules"
---

# Review Conventions

Available knowledge: [[requirements/ubiquitous-language]], [[software-craft/code-review]]. `in` artifacts: discover and read on demand as needed. 

1. This review tier runs after design and structure review have passed. The SE addresses convention findings only at this stage — the SE does not proactively run lint, format, or type checks during the TDD cycle.
2. Declare fail-fast stance per [[software-craft/code-review#concepts]] — stop at the first failure.
3. Run `ruff check .` and `task static-check` to verify formatting and lint rules pass.
4. Verify docstrings, type hints, and naming follow domain language per [[requirements/ubiquitous-language#key-takeaways]].
5. The reviewer MUST NOT modify any files per [[software-craft/code-review#key-takeaways]] — lint and type errors are findings to report, not to fix during review.
6. When flagging issues, include file:line references — e.g., "auth/handler.py:12 uses 'userName' instead of 'user_name'". Vague findings create rework.
7. Write results to artifacts listed in the current state's `out` attrs. If findings affect artifacts outside the `out` contract, flag them in output notes for the appropriate step.
8. Advance the flow with necessary evidence, choosing the appropriate next state based on the work completed.