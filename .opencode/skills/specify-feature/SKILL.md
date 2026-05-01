---
name: specify-feature
description: "Conduct a targeted conversation with stakeholders to capture feature-specific behavioral rules and scenarios"
---

# Specify Feature

Load [[requirements/interview-techniques#key-takeaways]] before starting. 

1. Conduct a feature-specific interview per [[requirements/interview-techniques#concepts]],
   focusing on behavioral rules and scenarios.
2. If the stakeholder describes a past failure related to this feature, probe for the
   specific incident per [[requirements/interview-techniques#concepts]].
3. If a stated requirement lacks a clear scenario, ladder to the real constraint per
   [[requirements/interview-techniques#concepts]].
4. If hidden failure modes are suspected, apply a pre-mortem per [[requirements/pre-mortem]].
5. Write confirmation gate before any file writes.
6. Write results to artifacts listed in the current state's `out` attrs. If findings affect artifacts outside the `out` contract, flag them in output notes for the appropriate step.
7. Advance the flow with necessary evidence, choosing the appropriate next state based on the work completed.
