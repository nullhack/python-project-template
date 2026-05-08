---
name: select-feature
description: "Select the next feature to develop: by delivery order for the first feature, by WSJF for subsequent features"
---

# Select Feature

Available knowledge: [[requirements/wsjf]]. `in` artifacts: read all before starting work.

1. Discover available features by listing `docs/features/` (or the project's feature directory).
2. IF no feature files exist → exit via `no_features`; features need discovery first.
3. IF more than one feature has `Status: BASELINED` → stop; WIP limit is 1.
4. Verify that architecture covers the candidate features by checking `domain_model.md` for relevant bounded contexts and `product_definition.md` for technology stack.
5. IF features have `Status: ELICITING` (no BASELINED features yet) → this is a first-run selection:
   - Select the first feature by delivery order from `product_definition.md`. The delivery order was established during discovery and already reflects business priority and technical dependencies.
   - Skip WSJF scoring: there's nothing to compare against.
6. IF features have `Status: BASELINED` (subsequent runs) → score per [[requirements/wsjf]] and select the highest WSJF score among Dependency=0 candidates.
7. Set the `feature_name` session param to the selected feature's filename stem (without `.feature` extension).
