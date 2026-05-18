---
domain: requirements
tags: [decomposition, splitting, features, rules]
last-updated: 2026-05-17
---

# Feature Decomposition Rules

## Key Takeaways

- Split triggers apply after grouping Examples by behavioral outcome and collapsing parameterized variants into Scenario Outlines, not on raw Example counts.
- If a Rule has >8 Must behaviors after MoSCoW triage and Scenario Outline collapse, split the Rule.
- If a Rule spans >1 bounded context, split immediately — bounded contexts are the decomposition unit, not "concerns."
- If a Rule behavioral paragraph contains "and" joining two independently testable outcomes, split into two Rules.
- Scenario Outlines count as one behavioral test for decomposition, regardless of Examples table row count.
- A completed feature whose description or Rules changed must move back to backlog.

## Concepts

**Behavioral Counting Before Threshold**: Raw Example count is meaningless for decomposition. Examples that share the same `Then` outcome test the same behavior (Wynne, 2015; Adzic, 2011). Group by `Then` outcome first, then collapse groups of 3+ value variants into Scenario Outlines per [[requirements/gherkin#concepts]]. Only the resulting behavioral group count feeds the decomposition threshold.

**Split Threshold**: After MoSCoW triage and Scenario Outline collapse, if a Rule's Must behaviors exceed 8, the Rule is too broad. Split it. This threshold fires at refine-features time (define-flow), when Rule structure can still be changed. During write-bdd-features (develop-flow), Rule structure is frozen and >8 Must Examples is a soft flag for PO review, not a split trigger.

**Context-Based Decomposition**: "Concern" is ambiguous — bounded context is not. Every bounded context is explicitly defined in `domain_spec.md`. If a Rule touches entities from two or more bounded contexts, split along context boundaries per [[requirements/feature-boundaries#concepts]]. Exceptions are documented there.

**Rule-Level Splits**: Three structural triggers apply regardless of Example count:
1. "and" joining two independently testable outcomes → split. "Create offline AND sync later" is one sequential workflow (keep). "Plant must have a name AND a care profile" is two independent validations (split).
2. Duplicate Rule → merge or differentiate.
3. Rule with no beneficiary → every Rule must name who benefits; system-only rules lack business value.

**Scenario Outline Collapse**: A Scenario Outline with 10 Examples table rows is one behavioral test, not 10. The decomposition threshold counts Scenario Outlines as one unit each. This prevents false splits when a Rule correctly uses parameterization to verify the same outcome across many inputs.

**Completed Feature Regression**: If a completed feature's description or Rules changed, move it back to backlog. Description changes always imply behaviour changes.

## Content

### Decomposition Decision Tree

```
When evaluating a Rule for decomposition:

1. GROUP candidate Examples by Then-outcome.
   Same Then = same behavior per [[requirements/gherkin#concepts]].

2. COLLAPSE groups with 3+ value variants into Scenario Outlines.
   Each Scenario Outline = 1 behavioral test.

3. COUNT distinct behavioral groups (plain Examples + Scenario Outlines).

4. TRIAGE via MoSCoW per [[requirements/moscow#concepts]].
   Count only Must behaviors.

5. CHECK structural triggers (apply regardless of count):
   - Rule spans >1 bounded context → split along context boundaries
   - "and" joins independently testable outcomes → split
   - Rule has no beneficiary → reframe to name who benefits
   - Duplicate Rule → merge or differentiate

6. CHECK Must-behavior threshold:
   - >8 Must behaviors → split Rule
   - ≤8 → Rule is well-sized, no split needed
```

### Split Decision Examples

| Rule | Raw Examples | After Group + Collapse | Must Behaviors | Split? | Why |
|------|-------------|----------------------|----------------|--------|-----|
| "Order rejected for invalid input" | 15 | 1 Scenario Outline | 1 | No | 15 variants of same Then-outcome → 1 Scenario Outline |
| "Plant must have name and care profile" | 6 | 2 Examples | 2 | Yes | "and" joins two independent validations → 2 Rules |
| "User registration" | 12 | 8 Examples + 1 Scenario Outline | 6 | No | 9 behavioral groups, 6 Musts → under threshold |
| "Care event lifecycle" (spans Plant Catalog + Care Logging) | 5 | 5 Examples | 4 | Yes | >1 bounded context → split along context lines |

### When Decomposition Fires

| Phase | Action | Trigger |
|-------|--------|---------|
| refine-features (define-flow) | Hard split | >8 Must behaviors, >1 context, "and" joins independent outcomes |
| write-bdd-features (develop-flow) | Soft flag for PO | >8 Must Examples — Rule structure is frozen |
| create-py-stubs (develop-flow) | Verify only | Confirm decomposition was applied during define-flow |

## Related

- [[requirements/invest]]: INVEST criteria that enforce decomposition
- [[requirements/moscow]]: MoSCoW triage thresholds that feed the Must count
- [[requirements/gherkin]]: Scenario Outline format and behavioral distinctness
- [[requirements/feature-boundaries]]: feature-level split along context and aggregate lines
