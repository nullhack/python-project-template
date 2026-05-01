---
name: determine-action-items
description: "Determine whether the feature needs replanning, architecture changes, or should be abandoned"
---

# Determine Action Items

Load [[requirements/post-mortem#concepts]] before starting. 

1. Determine routing per [[requirements/post-mortem#concepts]].
2. Update the post-mortem with the restart check per [[requirements/post-mortem#key-takeaways]].
3. Write results to artifacts listed in the current state's `out` attrs. If findings affect artifacts outside the `out` contract, flag them in output notes for the appropriate step.
4. Advance the flow with necessary evidence, choosing the appropriate next state based on the work completed.