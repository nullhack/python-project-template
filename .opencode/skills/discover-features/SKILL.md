---
name: discover-features
description: "Synthesize analysis artifacts into .feature files with coherent boundaries, business rules, and constraints"
---

# Discover Features

Available knowledge: [[requirements/feature-discovery#concepts]]. `in` artifacts: discover and read on demand as needed.

1. Read the product definition, domain model, technical design, and interview notes.
2. Map delivery order steps to bounded contexts and aggregate boundaries. IF a delivery step spans multiple aggregates → flag for potential split. IF multiple delivery steps share one aggregate → they may belong together.
3. For each feature boundary, cross-reference domain events, entity invariants, and interview findings to identify business rules.
4. IF artifacts are ambiguous, contradictory, or incomplete for a feature boundary or business rule → ask the stakeholder targeted questions using CIT and laddering per [[requirements/interview-techniques#concepts]]. Record answers in the feature's Questions table.
5. Derive coarse `Rules (Business)` bullets from the synthesized understanding — one per behavioral hypothesis.
6. For each feature, identify applicable Constraints from the product definition's quality attributes.
7. Run gap analysis per [[requirements/feature-discovery#concepts]]:
   - Every bounded context covered by at least one feature?
   - Every quality attribute enforced by at least one feature?
   - Every critical domain event traceable to a rule?
   IF any gap is found → flag it. Do NOT silently fill gaps with assumed rules.
8. Create a `.feature` file from the template at `.templates/docs/features/feature.feature.template` for each feature with title, description, Status: ELICITING, Rules (Business), and Constraints.
9. Do NOT write full `Rule:` blocks (As a/I want/So that) or `Example:` blocks — those require the adversarial analysis of breakdown.
10. Write results to artifacts listed in the current state's `out` attrs. If findings affect artifacts outside the `out` contract, flag them in output notes for the appropriate step.
11. Advance the flow with necessary evidence, choosing the appropriate next state based on the work completed.
