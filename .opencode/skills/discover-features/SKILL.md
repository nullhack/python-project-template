---
name: discover-features
description: "Create .feature file stubs from the delivery order, domain model, and interview notes"
---

# Discover Features

Available knowledge: [[requirements/feature-discovery#concepts]]. `in` artifacts: discover and read on demand as needed.

1. Read the product definition's delivery order to identify all features.
2. For each delivery order step, create a `.feature` file from the template at `.templates/docs/features/feature.feature.template` with:
   - **Title** — from the delivery order step name.
   - **Description** — 2-4 sentences synthesizing the delivery order description, domain model entities, and interview notes.
   - **Status: ELICITING** — features are discovered, not yet baselined.
   - **Rules (Business)** — coarse one-line bullet points. One bullet per expected user story, derived from domain model entities and domain events.
   - **Constraints** — quality attributes from the product definition that apply to this feature.
3. Do NOT write full `Rule:` blocks (As a/I want/So that) or `Example:` blocks — those belong in planning-flow's `feature-breakdown` and `bdd-features` states respectively.
4. Validate that every bounded context is covered by at least one feature. IF a bounded context has no corresponding feature → flag the gap.
5. Write results to artifacts listed in the current state's `out` attrs. If findings affect artifacts outside the `out` contract, flag them in output notes for the appropriate step.
6. Advance the flow with necessary evidence, choosing the appropriate next state based on the work completed.
