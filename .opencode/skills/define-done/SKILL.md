---
name: define-done
description: "Define the quality gates that must pass before the feature is considered complete"
---

# Define Done

Load [[software-craft/code-review#key-takeaways]] before starting. 

1. Define quality gates per [[software-craft/code-review#key-takeaways]] — design correctness, test quality, and conventions.
2. Incorporate quality attributes from the product definition into the gates.
3. Verify spec compliance — for each interface element documented in the technical design (command flags, configuration keys, API parameters), verify it exists in the implementation. Interface elements specified in the design but not implemented indicate an incomplete feature.
4. Write results to artifacts listed in the current state's `out` attrs. If findings affect artifacts outside the `out` contract, flag them in output notes for the appropriate step.
5. Advance the flow with necessary evidence, choosing the appropriate next state based on the work completed.