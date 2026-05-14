---
name: write-bdd-features
description: "Write concrete Given/When/Then Example blocks for each Rule in the feature file"
---

# Write BDD Features

Available knowledge: [[requirements/gherkin]], [[requirements/moscow]], [[requirements/pre-mortem]], [[requirements/decomposition]]. `in` artifacts: read all before starting work.

1. Discover and read the feature file, product definition, behavioral spec, and glossary from `in`.
2. Run a pre-mortem per [[requirements/pre-mortem]] for each Rule before writing any Examples. All Rules must have their pre-mortems completed before any Examples are written.
3. IF hidden failure modes surface from the pre-mortem → add Examples to cover them per [[requirements/gherkin#key-takeaways]].
4. Write Example blocks per [[requirements/gherkin#concepts]]: declarative, single observable outcome per Then, using `Example:` keyword not `Scenario:`. Examples go under their parent `Rule:` block.
5. For each Rule, verify Examples cover distinct behaviours per [[requirements/gherkin#concepts]]:
   a) Group Examples by `Then` outcome. Same outcome = same behaviour. Keep one representative per outcome. Discard duplicates.
   b) For each distinct outcome, run the behavior-level pre-mortem per [[requirements/pre-mortem#concepts]].
   c) Add Examples targeting the failure modes surfaced.
   d) Structural (invariant) rules: one representative Example suffices. Defer full coverage to a Hypothesis property test per [[software-craft/test-design#concepts]].
6. Classify each Example per [[requirements/moscow#concepts]]; MoSCoW classification is for internal triage only: do NOT add Must/Should/Could tags to Examples in the .feature file.
7. IF a Rule has more than 8 Must Examples → split the Rule per [[requirements/decomposition#key-takeaways]].
8. IF a Rule spans more than 2 concerns → split per [[requirements/decomposition#key-takeaways]].
9. Ensure every Example has a unique, descriptive title. pytest-beehave maps Examples to test functions by title: the function name is `test_<scenario_title_slug>`. Titles must be unique within the feature file and descriptive enough to serve as the test function identifier. No `@id` tags are used — the title is the traceability link.
10. Evaluate each Rule's Examples for quality: observable (single outcome per Then), declarative (behaviour not steps), distinct (no duplicate coverage), and pre-mortem coverage. Every criterion that fails is a hard blocker: fix before advancing.
