---
name: write-bdd-features
description: "Write concrete Given/When/Then BDD scenarios for each user story using ubiquitous language"
---

# Write BDD Features

Available knowledge: [[requirements/gherkin]], [[requirements/moscow]], [[requirements/pre-mortem]], [[requirements/decomposition]]. `in` artifacts: discover and read on demand as needed. 

1. Discover and read the feature file, product definition, domain model, and glossary from `in`.
2. Run a pre-mortem per [[requirements/pre-mortem]] for each Rule before writing any Examples. All Rules must have their pre-mortems completed before any Examples are written.
3. IF hidden failure modes surface from the pre-mortem → add Examples to cover them per [[requirements/gherkin#key-takeaways]].
4. Write Example blocks per [[requirements/gherkin#concepts]] — declarative, single observable outcome per Then, using `Example:` keyword not `Scenario:`.
5. Classify each Example per [[requirements/moscow#concepts]]; MoSCoW classification is for internal triage only — do NOT add Must/Should/Could tags to Examples in the .feature file.
6. IF a Rule has more than 8 Must Examples → split the Rule per [[requirements/decomposition#key-takeaways]].
7. IF a Rule spans more than 2 concerns → split per [[requirements/decomposition#key-takeaways]].
8. Assign `@id` tags to all Examples. After a feature is BASELINED, all Example blocks are immutable — changes require `@deprecated` on the old Example (preserving the original @id) and a new Example with a new @id. `@id` tags are for traceability only; do NOT add priority tags (e.g. @must, @should) to Examples.
9. Evaluate each Rule's Examples for quality: observable (single outcome per Then), declarative (behaviour not steps), distinct (no duplicate coverage), and pre-mortem coverage. Every criterion that fails is a hard blocker — fix before advancing.
10. Write results to artifacts listed in the current state's `out` attrs. If findings affect artifacts outside the `out` contract, flag them in output notes for the appropriate step.
11. Advance the flow with necessary evidence, choosing the appropriate next state based on the work completed.