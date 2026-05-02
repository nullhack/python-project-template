---
name: specify-feature
description: "Conduct a targeted conversation with stakeholders to capture feature-specific behavioral rules and scenarios"
---

# Specify Feature

Available knowledge: [[requirements/interview-techniques#concepts]], [[requirements/pre-mortem#key-takeaways]]. `in` artifacts: discover and read on demand as needed. 

1. Discover and read the feature file and interview notes from `in`.
2. Open the interview with the 7 general questions (Who, What, Why, When/Where, Success, Failure, Out-of-scope) per [[requirements/interview-techniques#concepts]].
3. IF the stakeholder describes a past failure related to this feature → probe for the specific incident per CIT per [[requirements/interview-techniques#concepts]].
4. IF a stated requirement lacks a clear scenario → ladder to the real constraint per [[requirements/interview-techniques#concepts]].
5. IF hidden failure modes are suspected → apply a pre-mortem per [[requirements/pre-mortem#key-takeaways]].
6. Paraphrase each answer before the next question per active listening Level 1 per [[requirements/interview-techniques#concepts]].
7. At transitions between topics, synthesize per active listening Level 2 per [[requirements/interview-techniques#concepts]].
8. At session end, present full synthesis for stakeholder approval per active listening Level 3 per [[requirements/interview-techniques#concepts]].
9. Write results to artifacts listed in the current state's `out` attrs. If findings affect artifacts outside the `out` contract, flag them in output notes for the appropriate step.
10. Advance the flow with necessary evidence, choosing the appropriate next state based on the work completed.