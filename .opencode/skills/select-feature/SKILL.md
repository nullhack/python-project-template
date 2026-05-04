---
name: select-feature
description: "Pick the next feature to develop based on business priority and delivery order"
---

# Select Feature

Available knowledge: [[requirements/wsjf]]. `in` artifacts: discover and read on demand as needed. 

1. Discover available features by listing `docs/features/` (or the project's feature directory).
2. IF no feature files exist → exit via `no_features`; features need discovery first (return to discovery-flow).
3. IF more than one feature has `Status: BASELINED` → stop; WIP limit is 1.
4. Verify that architecture covers the candidate features by checking `technical_design.md` for relevant module structure.
5. IF features have `Status: ELICITING` → select the first one by delivery order from `product_definition.md`. First-run selection uses delivery order, not WSJF.
6. IF features have `Status: BASELINED` (subsequent runs) → score per [[requirements/wsjf]] and select the highest WSJF score among Dependency=0 candidates.
7. Set the `feature_name` session param to the selected feature's filename stem (without `.feature` extension).
8. Write results to artifacts listed in the current state's `out` attrs. If findings affect artifacts outside the `out` contract, flag them in output notes for the appropriate step.
9. Advance the flow with necessary evidence, choosing the appropriate next state based on the work completed.
