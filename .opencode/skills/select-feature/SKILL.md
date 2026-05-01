---
name: select-feature
description: "Pick the next feature to develop based on business priority and delivery order"
---

# Select Feature

Load [[requirements/wsjf]] before starting. 

1. IF more than one feature directory exists in `docs/features/` → stop; WIP limit is 1.
2. Verify that architecture covers the candidate features.
3. Score BASELINED features per [[requirements/wsjf]].
4. IF no features have `Status: BASELINED` → exit; features need scoping first.
5. Filter to features with Dependency=0 (no prerequisite features). Only these are eligible for selection — features blocked by other uncompleted features are ineligible regardless of WSJF score.
6. Among eligible features, select the one with the highest WSJF score. Ties broken by Value.
7. IF no eligible features exist (all have Dependency=1) → resolve the blocking dependency first, then re-score.
8. Write results to artifacts listed in the current state's `out` attrs. If findings affect artifacts outside the `out` contract, flag them in output notes for the appropriate step.
9. Advance the flow with necessary evidence, choosing the appropriate next state based on the work completed.