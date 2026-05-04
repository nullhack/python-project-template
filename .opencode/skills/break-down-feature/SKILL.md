---
name: break-down-feature
description: "Refine coarse Rules into full Rule blocks with adversarial analysis and INVEST validation"
---

# Break Down Feature

Available knowledge: [[requirements/invest]], [[requirements/decomposition]], [[requirements/pre-mortem#key-takeaways]], [[requirements/interview-techniques#concepts]]. `in` artifacts: discover and read on demand as needed.

1. Discover and read the feature file, product definition, technical design, domain model, and interview notes from `in`. The feature file contains coarse `Rules (Business)` bullet points from discovery — these are behavioral hypotheses, not validated stories.
2. For each coarse rule, apply adversarial analysis:
   - Pre-mortem per [[requirements/pre-mortem#key-takeaways]]: "Imagine this rule was built exactly as described, all tests pass, but it fails for the user. What would be missing?"
   - CIT per [[requirements/interview-techniques#concepts]]: "When has this behavior gone wrong in practice?"
   - Laddering per [[requirements/interview-techniques#concepts]]: "Why is this rule important? What breaks without it?"
3. Expand each validated rule into a full `Rule:` block with As a/I want/So that format.
4. IF clarification is needed for a Rule → ask the stakeholder targeted questions. Record answers in the feature's Questions table.
5. Validate each Rule per [[requirements/invest#concepts]].
6. IF a story contains "and" → split into two Rules per [[requirements/decomposition#key-takeaways]].
7. IF a story lacks a named user role or business value → reframe per [[requirements/invest#concepts]].
8. IF a Rule spans more than 2 concerns or has more than 8 candidate Examples → split per [[requirements/decomposition#key-takeaways]].
9. Self-declare INVEST for each Rule per [[requirements/invest#concepts]]:
   - INVEST-I: each Rule is Independent — AGREE/DISAGREE
   - INVEST-V: each Rule delivers Value to a named user — AGREE/DISAGREE
   - INVEST-S: each Rule is Small enough for one cycle — AGREE/DISAGREE
   - INVEST-T: each Rule is Testable — AGREE/DISAGREE
   Every DISAGREE is a hard blocker — fix before advancing.
10. IF the feature cannot pass INVEST as a single story → propose the split to the stakeholder with rationale per [[requirements/decomposition#key-takeaways]]. Stakeholder decides what's core vs. deferred. Document their decision in the feature file.
11. Write results to artifacts listed in the current state's `out` attrs. If findings affect artifacts outside the `out` contract, flag them in output notes for the appropriate step.
12. Advance the flow with necessary evidence, choosing the appropriate next state based on the work completed.
