---
name: break-down-feature
description: "Decompose a selected feature into user stories that pass INVEST criteria"
---

# Break Down Feature

Load [[requirements/invest]] and [[requirements/decomposition]] before starting. 

1. Derive Rule blocks from the feature description — one Rule per user story.
2. Validate each Rule per [[requirements/invest]].
3. If a story contains "and", split into two Rules per [[requirements/decomposition]].
4. If a story lacks a named user role or business value, reframe per [[requirements/invest]].
5. If a Rule spans more than 2 concerns or has more than 8 candidate Examples, split per [[requirements/decomposition]].
6. Write results to artifacts listed in the current state's `out` attrs. If findings affect artifacts outside the `out` contract, flag them in output notes for the appropriate step.
7. Advance the flow with necessary evidence, choosing the appropriate next state based on the work completed.