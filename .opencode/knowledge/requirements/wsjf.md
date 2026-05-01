---
domain: requirements
tags: [wsjf, prioritization, scoring, backlog, feature-selection]
last-updated: 2026-04-29
---

# Weighted Shortest Job First — Reinertsen, 2009

## Key Takeaways

- Calculate WSJF as Value divided by Effort; select features with higher scores first.
- Value (1-5) maps to Kano categories: 5=Must-have (core workflow blocked), 4=High, 3=Medium (performance), 2=Low (delighter), 1=Minimal (cosmetic).
- Effort (1-5) maps to complexity: 1=Trivial (no new domain concepts), 2=Small (one new entity), 3=Medium (cross-cutting), 4=Large (multiple entities), 5=Very large (spans modules).
- Dependency=1 features are ineligible regardless of WSJF score; ties broken by Value; if all features have Dependency=1, resolve the blocking dependency first.
- Only features with `Status: BASELINED` are eligible for scoring; WIP limit is 1.

## Concepts

**WSJF Formula** (Reinertsen, 2009): `WSJF = Cost of Delay / Duration = Value / Effort`. Higher WSJF score means higher priority for selection. Value and Effort are each scored 1-5 using defined scales.

**Value Scale**: Value maps to Kano model categories (Kano et al., 1984). Must-have (5) means core workflow is blocked without it. High (4) significantly improves the primary use case. Medium (3) is useful but not blocking. Low (2) is a nice-to-have. Minimal (1) is cosmetic or out-of-scope.

**Effort Scale**: Effort maps to complexity. Trivial (1) has no new domain concepts. Small (2) introduces one new domain entity. Medium (3) is a cross-cutting concern. Large (4) involves multiple interacting domain entities. Very large (5) spans multiple modules or has unknown complexity.

**Selection Rules**: Dependency=1 features are ineligible regardless of WSJF score. Pick the highest WSJF score among Dependency=0 candidates. Ties broken by Value. If all BASELINED features have Dependency=1, resolve the blocking dependency first.

## Content

### Formula

```
WSJF = Cost of Delay / Duration = Value / Effort
```

Higher WSJF score = higher priority for selection.

### Value Scale (1-5)

Estimate user/business impact, mapped to Kano model categories:

| Score | Label | Kano Category | Description |
|---|---|---|---|
| 5 | Must-have | Basic need | Core workflow blocked without it |
| 4 | High | — | Significantly improves the primary use case |
| 3 | Medium | Performance | Useful but not blocking |
| 2 | Low | Delighter | Nice-to-have |
| 1 | Minimal | — | Cosmetic or out-of-scope edge case |

Tiebreaker: use the number of Must Examples in the feature's Rule blocks. More Musts = higher value.

### Effort Scale (1-5)

Estimate implementation complexity:

| Score | Label | Description |
|---|---|---|
| 1 | Trivial | No new domain concepts |
| 2 | Small | One new domain entity |
| 3 | Medium | Cross-cutting concern |
| 4 | Large | Multiple interacting domain entities |
| 5 | Very large | Spans multiple modules or has unknown complexity |

### Dependency Scoring (0/1)

| Score | Meaning |
|---|---|
| 0 | Independent — no hard prerequisite |
| 1 | Blocked — requires another backlog feature to be completed first |

### Selection Rules

1. Only features with Dependency=0 are eligible — features that depend on other uncompleted features cannot be selected, regardless of WSJF score.
2. Among eligible features, select the one with the highest WSJF score.
3. Ties broken by Value — user impact matters more than effort optimization.
4. If no features are eligible (all have Dependency=1): resolve the blocking dependency first, then re-score.

### Prerequisites

- Only features with `Status: BASELINED` are eligible for scoring
- WIP limit of 1 — only one feature in progress at a time
- The PO selects and moves the feature; no other agent moves feature files

## Related

- [[requirements/invest]] — story quality criteria applied before scoring
- [[requirements/moscow]] — prioritizing Examples within a Rule