---
name: write-bdd-features
description: "Write concrete Given/When/Then BDD scenarios for each user story using ubiquitous language"
---

# Write BDD Features

Load [[requirements/gherkin]], [[requirements/moscow]], [[requirements/pre-mortem]], and [[requirements/decomposition]] before starting. 

1. Run a pre-mortem per [[requirements/pre-mortem]] for each Rule before writing any Examples.
2. If hidden failure modes surface from the pre-mortem, add Examples to cover them per [[requirements/gherkin]].
3. Write Example blocks per [[requirements/gherkin]].
4. Classify each Example per [[requirements/moscow]]; MoSCoW classification is for internal triage only — do NOT add Must/Should/Could tags to Examples in the .feature file.
5. If a Rule has more than 8 Must Examples, split the Rule per [[requirements/decomposition]].
6. If a Rule spans more than 2 concerns, split per [[requirements/decomposition]].
7. Assign `@id` tags to all Examples.
8. Write results to artifacts listed in the current state's `out` attrs. If findings affect artifacts outside the `out` contract, flag them in output notes for the appropriate step.
9. Advance the flow with necessary evidence, choosing the appropriate next state based on the work completed.