---
name: write-bdd-features
description: "Write concrete Given/When/Then Example blocks for each Rule in the feature file"
---

# Write BDD Features

Available knowledge: [[requirements/gherkin]], [[requirements/moscow]], [[requirements/pre-mortem]], [[requirements/decomposition]]. `in` artifacts: read all before starting work.

1. Discover and read the feature file, product definition, domain spec, and glossary from `in`.
2. Run a pre-mortem per [[requirements/pre-mortem]] for each Rule before writing any Examples. All Rules must have their pre-mortems completed before any Examples are written.
3. IF hidden failure modes surface from the pre-mortem → plan Examples to cover them per [[requirements/gherkin#key-takeaways]].
4. For each Rule, write Example or Scenario Outline blocks directly from the Rule description and domain spec knowledge per [[requirements/gherkin#concepts]]. Do NOT use behavior hints — they have been removed from the flow. Derive Example behavior directly from:
   - The Rule's behavioral description paragraph
   - The domain spec's External Contracts, Data Shapes, and Invariants
   - The feature's `# Constraints:` comments
   - Quality attributes from product_definition.md
   Write Examples per format rules in [[requirements/gherkin#concepts]].
5. For each Rule, verify Examples cover distinct behaviours per [[requirements/gherkin#concepts]]:
   a) Group Examples by `Then` outcome. Same outcome = same behaviour. Keep one representative per outcome. Discard duplicates. Exception: Scenario Outline rows are parameterized variants of the same behaviour — they are NOT duplicates.
   b) For each distinct outcome, run the behavior-level pre-mortem per [[requirements/pre-mortem#concepts]].
   c) Add Examples targeting the failure modes surfaced.
   d) Structural (invariant) rules: one representative Example suffices. Defer full coverage to a Hypothesis property test per [[software-craft/test-design#concepts]].
6. Classify each Example per [[requirements/moscow#concepts]]; MoSCoW classification is for internal triage only: do NOT add Must/Should/Could tags to Examples in the .feature file.
7. IF a Rule has more than 8 Must behaviors (after grouping by Then-outcome and collapsing Scenario Outlines) → this is a soft flag for PO review. Do NOT split or modify the Rule — Rule structure is frozen after define-flow. Decomposition was applied during refine-features; this check catches edge cases that slipped through. A Rule with 9+ Must behaviors is acceptable if the behaviour genuinely requires that many distinct cases.
8. Evaluate each Rule's Examples for quality, checking every criterion per [[requirements/gherkin#concepts]]:
   Evaluate Example quality per criteria in [[requirements/gherkin#concepts]]. Every criterion that fails is a hard blocker: fix before advancing.