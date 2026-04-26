---
domain: requirements
tags: [wsjf, prioritization, scoring, backlog]
last-updated: 2026-04-26
---

# Weighted Shortest Job First (WSJF)

## Key Takeaways

- WSJF = Value / Effort; higher score means higher priority for selection.
- Value (1-5) maps to Kano categories: 5=Must-have (core workflow blocked), 4=High, 3=Medium (performance), 2=Low (delighter), 1=Minimal (cosmetic).
- Effort (1-5) maps to @id count: 1=Trivial (1-2), 2=Small (3-5), 3=Medium (6-8), 4=Large (>8), 5=Very large (spans modules).
- Dependency=1 features are ineligible regardless of WSJF score; ties broken by Value; if all features have Dependency=1, resolve the blocking dependency first.

## Concepts

**WSJF Formula**: `WSJF = Cost of Delay / Duration = Value / Effort`. Higher WSJF score means higher priority for selection. Value and Effort are each scored 1-5 using defined scales.

**Value Scale**: Value maps to Kano model categories — 5 (Must-have, core workflow blocked without it), 4 (High, significantly improves primary use case), 3 (Medium, useful but not blocking), 2 (Low, nice-to-have), 1 (Minimal, cosmetic or out-of-scope edge case).

**Effort Scale**: Effort maps to @id count — 1 (Trivial, 1-2 @ids), 2 (Small, 3-5), 3 (Medium, 6-8), 4 (Large, >8), 5 (Very large, spans multiple modules).

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

Tiebreaker: use the number of `Must` Examples in the feature's `Rule:` blocks. More Musts = higher value.

### Effort Scale (1-5)

Estimate implementation complexity, mapped to @id count:

| Score | Label | @id Count | Description |
|---|---|---|---|
| 1 | Trivial | 1-2 | No new domain concepts |
| 2 | Small | 3-5 | One new domain entity |
| 3 | Medium | 6-8 | Cross-cutting concern |
| 4 | Large | >8 | Multiple interacting domain entities |
| 5 | Very large | — | Spans multiple modules or has unknown complexity |

### Dependency Scoring (0/1)

| Score | Meaning |
|---|---|
| 0 | Independent — no hard prerequisite |
| 1 | Blocked — requires another backlog feature to be completed first |

### Selection Rules

1. **Dependency=1 features are ineligible** regardless of WSJF score. They cannot start until their prerequisite is completed.
2. **Pick the highest WSJF score** among Dependency=0 candidates.
3. **Ties broken by Value** — user impact matters more than effort optimization.
4. **If all BASELINED features have Dependency=1**: stop and resolve the blocking dependency first — select and complete the depended-upon feature.

### Scoring Table Template

| Feature | Value (1-5) | Effort (1-5) | Dependency (0/1) | WSJF |
|---|---|---|---|---|
| `<name>` | | | | Value / Effort |

### Prerequisites

- Only features with `Status: BASELINED` are eligible for scoring
- `docs/features/in-progress/` must be empty (WIP limit of 1)
- The PO moves the selected feature to `in-progress/` — no other agent moves `.feature` files

## Related

- [[requirements/invest-moscow]] — story quality criteria applied before scoring
- [[workflow/state-machine]] — workflow states governing feature lifecycle