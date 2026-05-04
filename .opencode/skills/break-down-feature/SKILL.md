---
name: break-down-feature
description: "Refine coarse Rules from discovery into full Rule blocks with INVEST validation"
---

# Break Down Feature

Available knowledge: [[requirements/invest]], [[requirements/decomposition]], [[requirements/interview-techniques#concepts]]. `in` artifacts: discover and read on demand as needed.

1. Discover and read the feature file, product definition, technical design, and interview notes from `in`. The feature file already contains coarse `Rules (Business)` bullet points from discovery's story mapping.
2. For each `Rules (Business)` bullet point, expand it into a full `Rule:` block with As a/I want/So that format.
3. IF clarification is needed for a Rule → ask the stakeholder targeted questions using CIT and laddering per [[requirements/interview-techniques#concepts]]. Record answers in the feature's Questions table.
4. Validate each Rule per [[requirements/invest#concepts]].
5. IF a story contains "and" → split into two Rules per [[requirements/decomposition#key-takeaways]].
6. IF a story lacks a named user role or business value → reframe per [[requirements/invest#concepts]].
7. IF a Rule spans more than 2 concerns or has more than 8 candidate Examples → split per [[requirements/decomposition#key-takeaways]].
8. Self-declare INVEST for each Rule per [[requirements/invest#concepts]]:
   - INVEST-I: each Rule is Independent — AGREE/DISAGREE
   - INVEST-V: each Rule delivers Value to a named user — AGREE/DISAGREE
   - INVEST-S: each Rule is Small enough for one cycle — AGREE/DISAGREE
   - INVEST-T: each Rule is Testable — AGREE/DISAGREE
   Every DISAGREE is a hard blocker — fix before advancing.
9. IF the feature cannot pass INVEST as a single story → propose the split to the stakeholder with rationale per [[requirements/decomposition#key-takeaways]]. Stakeholder decides what's core vs. deferred. Document their decision in the feature file.
10. Write results to artifacts listed in the current state's `out` attrs. If findings affect artifacts outside the `out` contract, flag them in output notes for the appropriate step.
11. Advance the flow with necessary evidence, choosing the appropriate next state based on the work completed.
