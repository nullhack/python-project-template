---
domain: requirements
tags: [prioritization, MoSCoW, examples, classification]
last-updated: 2026-04-29
---

# MoSCoW Prioritization (Clegg & Barker, 1994)

## Key Takeaways

- Classify each candidate Example as Must (required for correctness), Should (high value but deferrable), or Could (nice-to-have edge case). This classification is for internal triage only — it must NOT appear as Gherkin tags or in the .feature file.
- If Musts alone exceed 8 Examples or the Rule spans more than 2 concerns, split the Rule immediately.
- Musts cannot exceed 60% of total effort at the story level (DSDM); if a story has 12 Examples and only 3 are Musts, the remaining 9 can be deferred.
- MoSCoW triage is applied during criteria writing (planning-flow `bdd-features` state), not during discovery.

## Concepts

**Must**: Required for the Rule to be correct. Without it, the feature is wrong. Must Examples define the minimum viable behaviour that must be present for the Rule to be considered implemented.

**Should**: High value but deferrable. The feature works without it but is diminished. Should Examples enhance the core behaviour but are not required for correctness.

**Could**: Nice-to-have edge case. Low risk if deferred. Could Examples cover unusual conditions or minor enhancements that improve robustness.

**Split Rule**: If Musts alone exceed 8 Examples or the Rule spans more than 2 concerns, split the Rule immediately. This prevents Rules from becoming unwieldy and ensures each Rule is independently testable and deliverable.

## Content

### Priority Definitions

| Priority | Definition | Consequence if omitted |
|---|---|---|
| **Must** | Required for the Rule to be correct | The feature is wrong |
| **Should** | High value but deferrable | The feature works but is diminished |
| **Could** | Nice-to-have edge case | Low risk if deferred |

### Split Rules

Two conditions trigger an immediate split:

1. **Musts alone exceed 8 Examples** — the Rule is too large and should be decomposed into smaller Rules, each with its own set of Examples.
2. **The Rule spans more than 2 concerns** — distinct concerns should be expressed in separate Rules to maintain INVEST-I (Independence) and INVEST-S (Small).

### Effort Allocation

At the story level, Musts should not exceed 60% of total effort (DSDM). If a story has 12 Examples and only 3 are Musts, the remaining 9 can be deferred. This prevents gold-plating and keeps stories small and focused.

### When to Apply

MoSCoW triage is applied during criteria writing in the `bdd-features` state of the planning flow, after INVEST qualification in `feature-breakdown` and pre-mortem analysis. Each candidate Example receives a Must/Should/Could classification for internal triage — to decide which Examples to include and which to defer. MoSCoW labels must NOT appear as Gherkin tags, in `@id` tags, or anywhere in the .feature file.

## Related

- [[requirements/invest]] — story quality criteria applied before MoSCoW triage
- [[requirements/decomposition]] — splitting Rules that fail MoSCoW thresholds
- [[requirements/gherkin]] — writing Examples with MoSCoW classification