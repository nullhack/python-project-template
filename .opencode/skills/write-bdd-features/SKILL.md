---
name: write-bdd-features
description: "Write concrete Given/When/Then Example blocks for each Rule in the feature file"
---

# Write BDD Features

Available knowledge: [[requirements/gherkin]], [[requirements/moscow]], [[requirements/pre-mortem]], [[requirements/decomposition]]. `in` artifacts: read all before starting work.

1. Discover and read the feature file, product definition, domain spec, and glossary from `in`.
2. Run a pre-mortem per [[requirements/pre-mortem]] for each Rule before writing any Examples. All Rules must have their pre-mortems completed before any Examples are written.
3. IF hidden failure modes surface from the pre-mortem → add Examples to cover them per [[requirements/gherkin#key-takeaways]].
4. Convert behavior hints to Example or Scenario Outline blocks per [[requirements/gherkin#concepts]]:
   a. **Title constraint**: every Example/Scenario Outline title must be 2–6 words and unique within the feature file. Count words by splitting on whitespace. If a title is too short or too long, rephrase before writing the Example.
   b. **Example vs Scenario Outline decision**: if the same behavioural outcome must be verified across 3+ different input/output value combinations → use `Scenario Outline:` with `<placeholder>` syntax and an `Examples:` table. Otherwise use `Example:`. Do NOT use Scenario Outline for single or two-value cases.
   c. **Scenario Outline format**: include all `<placeholder>` names in Given/When/Then steps. Provide at least 3 concrete rows in the Examples table. Placeholder names must be valid Python identifiers (not keywords, not builtins).
   d. **Literals for traceability**: use quoted strings (`"value"`) and bare numbers (`42`) in steps so beehave can extract and verify them in test bodies.
   e. **Declarative style**: describe behaviour, not UI steps. Use `Example:` keyword for single cases (not `Scenario:`).
5. Remove behavior hints section after all hints are converted (cleanup gate — no `Behavior hints:` text should remain in the .feature file).
6. For each Rule, verify Examples cover distinct behaviours per [[requirements/gherkin#concepts]]:
   a) Group Examples by `Then` outcome. Same outcome = same behaviour. Keep one representative per outcome. Discard duplicates. Exception: Scenario Outline rows are parameterized variants of the same behaviour — they are NOT duplicates.
   b) For each distinct outcome, run the behavior-level pre-mortem per [[requirements/pre-mortem#concepts]].
   c) Add Examples targeting the failure modes surfaced.
   d) Structural (invariant) rules: one representative Example suffices. Defer full coverage to a Hypothesis property test per [[software-craft/test-design#concepts]].
7. Classify each Example per [[requirements/moscow#concepts]]; MoSCoW classification is for internal triage only: do NOT add Must/Should/Could tags to Examples in the .feature file.
8. IF a Rule has more than 8 Must Examples → split the Rule per [[requirements/decomposition#key-takeaways]].
9. IF a Rule spans more than 2 concerns → split per [[requirements/decomposition#key-takeaways]].
10. Verify every Rule title is 2–6 words. If any Rule title is too long or too short, rephrase to fit within the constraint while preserving the rule's meaning.
11. Evaluate each Rule's Examples for quality: titles within 2–6 word range, observable (single outcome per Then), declarative (behaviour not steps), distinct (no duplicate coverage), pre-mortem coverage, correct use of Scenario Outline for multi-variant cases. Every criterion that fails is a hard blocker: fix before advancing.
