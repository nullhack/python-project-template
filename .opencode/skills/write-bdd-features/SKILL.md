---
name: write-bdd-features
description: "Write concrete Given/When/Then Example blocks for each Rule in the feature file"
---

# Write BDD Features

Available knowledge: [[requirements/gherkin]], [[requirements/moscow]], [[requirements/pre-mortem]], [[requirements/decomposition]], [[requirements/property-patterns]]. `in` artifacts: read all before starting work.

1. Discover and read the feature file, product definition, domain spec, and glossary from `in`.
2. Run a pre-mortem per [[requirements/pre-mortem]] for each Rule before writing any Examples. All Rules must have their pre-mortems completed before any Examples are written.
3. IF hidden failure modes surface from the pre-mortem → plan Examples to cover them per [[requirements/gherkin#key-takeaways]].
4. For each Rule, apply property patterns per [[requirements/property-patterns#concepts]] to determine Example structure:
    a) Check each of the seven patterns against the Rule's behaviour.
    b) If no pattern applies → write a simple `Example:` with fixed inputs.
    c) If a pattern applies and reveals 3+ input combinations with the same step structure → write a `Scenario Outline:` with an `Examples:` table covering the significant combinations surfaced by the pattern.
    d) If a pattern applies but only reveals 1-2 combinations → write simple `Example:` per combination.
    Write Examples per format rules in [[requirements/gherkin#concepts]], deriving behavior from the Rule's description, domain spec External Contracts/Data Shapes/Invariants, the feature's `# Constraints:` comments, and quality attributes from product_definition.md.
5. For each Rule, verify Examples cover distinct behaviours per [[requirements/gherkin#concepts]]:
   a) Group Examples by `Then` outcome. Same outcome = same behaviour. Keep one representative per outcome. Discard duplicates. Exception: Scenario Outline rows are parameterized variants of the same behaviour — they are NOT duplicates.
   b) For each distinct outcome, run the behavior-level pre-mortem per [[requirements/pre-mortem#concepts]].
   c) Add Examples targeting the failure modes surfaced.
    d) Structural (invariant) rules: one representative Example suffices. Defer full coverage to a Hypothesis property test per [[software-craft/test-design#concepts]], using the pattern-to-strategy mapping in [[requirements/property-patterns#content]].
6. Classify each Example per [[requirements/moscow#concepts]]; MoSCoW classification is for internal triage only: do NOT add Must/Should/Could tags to Examples in the .feature file.
7. IF a Rule has more than 8 Must behaviors (after grouping by Then-outcome and collapsing Scenario Outlines) → this is a soft flag for PO review. Do NOT split or modify the Rule — Rule structure is frozen after define-flow. Decomposition was applied during refine-features; this check catches edge cases that slipped through. A Rule with 9+ Must behaviors is acceptable if the behaviour genuinely requires that many distinct cases.
8. Evaluate each Rule's Examples for quality, checking every criterion per [[requirements/gherkin#concepts]]:
    Evaluate Example quality per criteria in [[requirements/gherkin#concepts]]. Every criterion that fails is a hard blocker: fix before advancing.
9. Run `beehave check <feature_id>` to verify structural traceability catches issues at write time — title character violations, placeholder name problems, literal format issues. Fix any errors before committing. This prevents downstream rework when the SE generates stubs.