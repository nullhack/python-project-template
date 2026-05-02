---
name: conduct-interview
description: "Interview stakeholders to elicit pain points, business goals, domain terms, and quality attributes"
---

# Conduct Stakeholder Interview

Available knowledge: [[requirements/interview-techniques#key-takeaways]]. `in` artifacts: discover and read on demand as needed.

1. Start with general questions per [[requirements/interview-techniques#concepts]].
2. If general questions reveal multiple behaviour groups, probe each as a
   cross-cutting group per [[requirements/interview-techniques#concepts]].
3. If specific features are identified, drill into feature-level questions to
   define feature names and rough boundaries per [[requirements/interview-techniques#concepts]].
4. If >2 concerns emerge for a single feature, split per [[requirements/decomposition]].
5. Write confirmation gate before any file writes.
6. Write results to artifacts listed in the current state's `out` attrs. If findings affect artifacts outside the `out` contract, flag them in interview notes for the appropriate step.
7. Advance the flow with necessary evidence, choosing the appropriate next state based on the work completed.
