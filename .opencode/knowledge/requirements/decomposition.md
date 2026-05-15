---
domain: requirements
tags: [decomposition, splitting, features, rules]
last-updated: 2026-04-29
---

# Feature Decomposition Rules

## Key Takeaways

- If a feature spans more than 2 distinct concerns, split it immediately into separate features.
- If a feature has more than 8 candidate Examples, split the Rule immediately.
- If Musts alone exceed 8 Examples after MoSCoW triage, split the Rule.
- A completed feature whose description or Rules changed must move back to backlog.
- Rules containing "and" must be split into two separate Rules.

## Concepts

**Immediate Split on Threshold**: When the PO detects >2 distinct concerns OR >8 candidate Examples, split immediately. Record the split in the session notes, create feature files for both parts, and continue.

**Decomposition Check During Baselining**: A feature may only be baselined when it does not span >2 concerns AND does not have >8 candidate Examples. The flow enforces INVEST-S (Small) and INVEST-I (Independent), which subsume the decomposition check.

**Rule-Level Splits**: If a Rule contains "and" → break it into two Rules. If a Rule duplicates another Rule → merge or differentiate. If a Rule spans multiple unrelated concerns → split immediately. "As the system, I want..." → no business value, must reframe.

**Completed Feature Regression**: If a completed feature's description or Rules changed, move it back to backlog. Description changes always imply behaviour changes.

## Related

- [[requirements/invest]]: INVEST criteria that enforce decomposition
- [[requirements/moscow]]: MoSCoW triage thresholds that trigger splits
- [[requirements/gherkin]]: writing Examples for decomposed Rules