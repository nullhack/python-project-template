---
name: break-down-feature
description: "Decompose a selected feature into user stories that pass INVEST criteria"
---

# Break Down Feature

Available knowledge: [[requirements/invest]], [[requirements/decomposition]]. `in` artifacts: discover and read on demand as needed.

1. Discover and read the feature file, product definition, technical design, and interview notes from `in`.
2. Derive Rule blocks from the feature description — one Rule per user story.
3. Validate each Rule per [[requirements/invest#concepts]].
4. IF a story contains "and" → split into two Rules per [[requirements/decomposition#key-takeaways]].
5. IF a story lacks a named user role or business value → reframe per [[requirements/invest#concepts]].
6. IF a Rule spans more than 2 concerns or has more than 8 candidate Examples → split per [[requirements/decomposition#key-takeaways]].
7. Self-declare INVEST for each Rule per [[requirements/invest#concepts]]:
   - INVEST-I: each Rule is Independent — AGREE/DISAGREE
   - INVEST-V: each Rule delivers Value to a named user — AGREE/DISAGREE
   - INVEST-S: each Rule is Small enough for one cycle — AGREE/DISAGREE
   - INVEST-T: each Rule is Testable — AGREE/DISAGREE
   Every DISAGREE is a hard blocker — fix before advancing.
8. IF the feature cannot pass INVEST as a single story → propose the split to the stakeholder with rationale per [[requirements/decomposition#key-takeaways]]. Stakeholder decides what's core vs. deferred. Document their decision in the feature file.
9. Write results to artifacts listed in the current state's `out` attrs. If findings affect artifacts outside the `out` contract, flag them in output notes for the appropriate step.
10. Advance the flow with necessary evidence, choosing the appropriate next state based on the work completed.