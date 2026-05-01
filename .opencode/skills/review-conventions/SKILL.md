---
name: review-conventions
description: "Verify formatting, docstrings, type hints, and lint rules"
---

# Review Conventions

Load [[requirements/ubiquitous-language]] and [[software-craft/code-review]] before starting. 

1. Declare fail-fast stance per [[software-craft/code-review#concepts]] — stop at the first failure.
2. Run `ruff check .` and `task static-check` to verify formatting and lint rules pass.
3. Verify docstrings, type hints, and naming follow domain language per [[requirements/ubiquitous-language#key-takeaways]].
4. The reviewer MUST NOT modify any files per [[software-craft/code-review#key-takeaways]] — lint and type errors are findings to report, not to fix during review.
5. Write results to artifacts listed in the current state's `out` attrs. If findings affect artifacts outside the `out` contract, flag them in output notes for the appropriate step.
6. Advance the flow with necessary evidence, choosing the appropriate next state based on the work completed.