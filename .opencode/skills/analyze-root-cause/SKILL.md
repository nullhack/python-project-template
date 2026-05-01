---
name: analyze-root-cause
description: "Investigate why the PR was rejected, identifying the failure point and missed gate"
---

# Analyze Root Cause

Load [[requirements/post-mortem#key-takeaways]] before starting. 

1. Identify the failure point — which quality gate was missed per [[requirements/post-mortem#key-takeaways]].
2. Determine whether the root cause is in planning, architecture, or implementation.
3. Write results to artifacts listed in the current state's `out` attrs. If findings affect artifacts outside the `out` contract, flag them in output notes for the appropriate step.
4. Advance the flow with necessary evidence, choosing the appropriate next state based on the work completed.