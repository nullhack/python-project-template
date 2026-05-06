---
domain: requirements
tags: [feature-discovery, story-mapping, backlog-creation, gap-analysis]
last-updated: 2026-05-04
---

# Feature Discovery

## Key Takeaways

- Feature discovery synthesizes multiple analysis artifacts (domain model, event map, interview notes, delivery order, technical design) into coherent feature boundaries with scoped business rules. It is a genuine analysis step, not mechanical transcription.
- Each feature captures coarse business rules: one-line statements of behavior that the feature must enforce or enable. These are behavioral hypotheses to be validated and refined.
- The PO must identify feature boundaries that respect bounded context borders, aggregate transactional boundaries, and module dependency order. Features that span aggregate boundaries or cross dependency lines are flagged for splitting.
- Gaps discovered during feature discovery (a bounded context with no feature, a quality attribute with no enforcing feature, a domain event with no corresponding rule) are flagged, not silently filled.
- When artifacts are ambiguous, contradictory, or incomplete, the PO asks targeted clarification questions using the same interview techniques (CIT, laddering) as discovery interviews, but scoped to the specific feature boundary or rule under consideration.
- Features have a lifecycle of increasing specificity: `Status: ELICITING` through discovery and breakdown, advancing to `BASELINED` after baseline confirmation.

## Concepts

**Feature Boundary Identification**: Deciding where one feature ends and another begins is a design judgment, not a mechanical step. Bounded contexts provide coarse boundaries, but the PO must decide granularity: too coarse and the feature is unmanageable; too fine and you lose cohesion. Patton (2014) recommends mapping the user's narrative flow as a backbone, then slicing vertically into releasable increments. Each slice should be independently deliverable and testable. Cross-reference the domain model's aggregate boundaries and the delivery order's dependency graph to validate that each feature is self-contained.

**Rule Discovery as Hypothesis**: Coarse rules are hypotheses about what the system must do, derived by cross-referencing three sources: domain events ("what must happen when X occurs"), entity invariants ("what must always be true about Y"), and stakeholder goals ("what the user needs to accomplish"). These hypotheses are validated and refined across phases (coarse hypotheses first, validated rules later) preventing premature commitment to story-level detail while ensuring comprehensive coverage across the whole product (Cohn, 2004; Patton, 2014).

**Targeted Clarification During Discovery**: When synthesizing analysis artifacts into feature boundaries, gaps and contradictions naturally emerge. A delivery step may map to multiple aggregates with unclear ownership. An entity invariant may contradict what the interview notes say. A quality attribute may have no obvious enforcing mechanism. These are not failures of earlier interviews. They are expected consequences of zooming from domain-level understanding to feature-level specificity. Targeted questions use the same techniques as discovery interviews (CIT for specific failure incidents, laddering for "why does this matter?") but are narrower, focused on resolving a specific boundary question rather than exploring the whole domain.

**Gap Analysis**: Systematically verify coverage across three dimensions: (1) every bounded context from the domain model is covered by at least one feature, (2) every quality attribute from the product definition is enforced by at least one feature's constraints, and (3) every critical domain event is traceable to at least one business rule. Uncovered areas indicate missing features or gaps in the domain model itself. Flag both.

**Feature Lifecycle**: Features follow a lifecycle of increasing specificity across phases:
1. **Discovery**: Feature boundaries identified, coarse business rules written, constraints scoped. Status: ELICITING.
2. **Breakdown**: Coarse rules expanded into full Rule blocks with As a/I want/So that format. INVEST validation applied. Targeted clarification may refine rules. Status remains ELICITING.
3. **Example Writing and Baseline**: Given/When/Then Examples written, pre-mortems applied, baseline confirmed. Status advances to BASELINED.

## Related

- [[requirements/invest]]: story quality criteria applied to rules
- [[requirements/wsjf]]: feature prioritization applied to BASELINED features
- [[requirements/gherkin]]: writing Examples from rules
- [[requirements/interview-techniques]]: interview methods for clarification
- [[requirements/decomposition]]: splitting Rules
- [[requirements/pre-mortem]]: adversarial analysis applied to rules
