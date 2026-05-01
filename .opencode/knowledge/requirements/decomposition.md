---
domain: requirements
tags: [decomposition, splitting, features, stories]
last-updated: 2026-04-29
---

# Feature Decomposition Rules

## Key Takeaways

- If a feature spans more than 2 distinct concerns during discovery, split it immediately into separate features.
- If a feature has more than 8 candidate Examples during specification, split the Rule immediately.
- If Musts alone exceed 8 Examples after MoSCoW triage, split the Rule.
- A completed feature whose description or Rules changed during discovery must move back to backlog.
- Stories containing "and" must be split into two separate Rules.

## Concepts

**Real-Time Split During Discovery**: When the PO detects >2 distinct concerns OR >8 candidate Examples during feature questions, split immediately. Record the split in the session notes, create feature files for both parts, and continue feature questions for both in sequence within the same session.

**Decomposition Check During Baselining**: A feature may only be baselined when it does not span >2 concerns AND does not have >8 candidate Examples. The `invest_passed` condition gate enforces INVEST-S (Small) and INVEST-I (Independent), which subsume the decomposition check.

**Story-Level Splits**: If a story contains "and" → break it into two Rules. If a story duplicates another Rule → merge or differentiate. If a story spans multiple unrelated concerns → split immediately. "As the system, I want..." → no business value, must reframe.

**Completed Feature Regression**: If a completed feature was touched during discovery and its description or Rules changed, move it back to backlog. Description changes always imply behaviour changes.

## Related

- [[requirements/invest]] — INVEST criteria that enforce decomposition
- [[requirements/moscow]] — MoSCoW triage thresholds that trigger splits
- [[requirements/gherkin]] — writing Examples for decomposed Rules