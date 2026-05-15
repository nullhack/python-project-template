---
domain: requirements
tags: [prioritization, MoSCoW, examples, classification]
last-updated: 2026-04-29
---

# MoSCoW Prioritization (Clegg & Barker, 1994)

## Key Takeaways

- Classify each candidate Example as Must (required for correctness), Should (high value but deferrable), or Could (nice-to-have edge case). This classification is for internal triage only: it must NOT appear as Gherkin tags or in the .feature file.
- If MoSCoW triage reveals that Musts alone exceed 8 Examples or the Rule spans more than 2 concerns, split per [[requirements/decomposition]].
- Musts cannot exceed 60% of total effort at the Rule level (DSDM); if a Rule has 12 Examples and only 3 are Musts, the remaining 9 can be deferred.
- MoSCoW triage classifies Examples for internal prioritization only: it must NOT appear as Gherkin tags or in the .feature file.

## Concepts

**Must**: Required for the Rule to be correct. Without it, the feature is wrong. Must Examples define the minimum viable behaviour that must be present for the Rule to be considered implemented.

**Should**: High value but deferrable. The feature works without it but is diminished. Should Examples enhance the core behaviour but are not required for correctness.

**Could**: Nice-to-have edge case. Low risk if deferred. Could Examples cover unusual conditions or minor enhancements that improve robustness.

**Split Trigger**: If Musts alone exceed 8 Examples or the Rule spans more than 2 concerns, the decomposition rules in [[requirements/decomposition]] apply. MoSCoW triage surfaces the signal; decomposition handles the split.

## Content

### Priority Definitions

| Priority | Definition | Consequence if omitted |
|---|---|---|
| **Must** | Required for the Rule to be correct | The feature is wrong |
| **Should** | High value but deferrable | The feature works but is diminished |
| **Could** | Nice-to-have edge case | Low risk if deferred |

### Effort Allocation

At the Rule level, Musts should not exceed 60% of total effort (DSDM). If a Rule has 12 Examples and only 3 are Musts, the remaining 9 can be deferred. This prevents gold-plating and keeps Rules small and focused.

### When to Apply

MoSCoW triage classifies each candidate Example as Must/Should/Could for internal prioritization, to decide which Examples to include and which to defer. MoSCoW labels must NOT appear as Gherkin tags, as Example titles, or anywhere in the .feature file.

## Related

- [[requirements/invest]]: INVEST criteria
- [[requirements/decomposition]]: splitting Rules that fail MoSCoW thresholds
- [[requirements/gherkin]]: writing Examples with MoSCoW classification