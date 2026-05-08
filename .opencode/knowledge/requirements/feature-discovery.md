---
domain: requirements
tags: [feature-discovery, story-mapping, backlog-creation, gap-analysis]
last-updated: 2026-05-08
---

# Feature Discovery

## Key Takeaways

- Feature discovery synthesizes analysis artifacts (domain model, delivery order, product definition, glossary) into coherent feature boundaries with scoped business rules. It is a genuine analysis step, not mechanical transcription.
- Each feature captures coarse business rules: one-line statements of behavior that the feature must enforce or enable. These are behavioral hypotheses to be validated and refined.
- Feature boundaries respect bounded context borders, aggregate transactional boundaries, and module dependency order per [[requirements/feature-boundaries]]. Features that span boundaries are flagged for splitting.
- Rules are derived systematically from three sources: domain events, aggregate invariants, and commands per [[requirements/rule-derivation]]. Every rule traces to at least one domain model artifact.
- Gaps discovered during feature discovery (a bounded context with no feature, a quality attribute with no enforcing feature, a domain event with no corresponding rule) are flagged, not silently filled.
- Features progress through a lifecycle of increasing specificity: an empty file with a description → coarse Rules (Business) and Constraints → full Rule blocks with @id-tagged Examples.

## Concepts

**Feature Boundary Identification**: Deciding where one feature ends and another begins is a design judgment using the delivery order as backbone (Patton, 2014), validated against bounded context and aggregate boundaries from the domain model. Each delivery step becomes a feature candidate; candidates spanning multiple contexts or aggregates are split per [[requirements/feature-boundaries]].

**Rule Discovery as Hypothesis**: Coarse rules are hypotheses about what the system must do, derived from three sources: domain events (behavioral rules), entity invariants (structural rules), and commands (action rules) per [[requirements/rule-derivation]]. These hypotheses are validated and refined across phases — coarse bullets first, formal user stories later — preventing premature commitment to story-level detail while ensuring comprehensive coverage (Cohn, 2004; Patton, 2014).

**Targeted Clarification During Discovery**: When artifacts are ambiguous, contradictory, or incomplete, ask targeted clarification questions using the same interview techniques (CIT, laddering) as discovery interviews, but scoped to the specific feature boundary or rule under consideration. Record answers in the relevant interview notes.

**Gap Analysis**: Systematically verify coverage across three dimensions: (1) every bounded context from the domain model is covered by at least one feature, (2) every quality attribute from the product definition is enforced by at least one feature's constraints, (3) every critical domain event is traceable to at least one business rule. Uncovered areas indicate missing features or gaps in the domain model itself. Flag both.

**Feature Lifecycle**: Features follow a lifecycle of increasing specificity across phases:
1. **Discovery**: Feature boundaries identified, coarse business rules written, constraints scoped.
2. **Breakdown**: Coarse rules expanded into full Rule blocks with As a/I want/So that format. INVEST validation applied.
3. **Example Writing and Baseline**: Given/When/Then Examples written, pre-mortems applied, baseline confirmed (feature now has @id-tagged Examples).

## Content

### Discovery Sequence

Feature discovery is two sequential activities:

1. **Boundary identification** (discover-features skill): Use the delivery order as backbone. Map each step to bounded contexts and aggregates from the domain model. Split candidates that span contexts or aggregates. Name features and write descriptions per [[requirements/feature-boundaries]]. Create .feature files with title and description.

2. **Rule derivation** (discover-rules skill): For each feature, assign domain model artifacts (entities, events, invariants, commands) based on bounded context membership. Derive behavioral rules from events, structural rules from invariants, and action rules from commands per [[requirements/rule-derivation]]. Map quality attributes to constraints. Write coarse Rules (Business) bullets and Constraints into each .feature file.

### Gap Analysis Procedure

After deriving rules for all features, verify:

1. **Context coverage**: List every bounded context from the domain model. Check that each has at least one feature. If a context has no feature, flag it as a gap.
2. **Quality attribute enforcement**: List every quality attribute from product_definition.md. Check that each is enforced by at least one feature's Constraints. If a quality attribute has no enforcing feature, flag it as a gap.
3. **Event traceability**: List every critical domain event. Check that each is traceable to at least one business rule. If an event has no rule, flag it as a gap.
4. **Invariant traceability**: List every aggregate invariant. Check that each has at least one rule. If an invariant has no rule, add it.
5. **Command traceability**: List every command. Check that each has at least one rule. If a command has no rule, flag it as out of scope or missing.

Gaps are recorded in the relevant interview notes. Do NOT silently fill gaps with assumed rules.

## Related

- [[requirements/feature-boundaries]]: deriving feature boundaries from delivery order and domain model
- [[requirements/rule-derivation]]: deriving business rules from events, invariants, and commands
- [[requirements/invest]]: story quality criteria applied to rules
- [[requirements/wsjf]]: feature prioritization applied to BASELINED features
- [[requirements/gherkin]]: writing Examples from rules
- [[requirements/interview-techniques]]: interview methods for clarification
- [[requirements/decomposition]]: splitting Rules
- [[requirements/pre-mortem]]: adversarial analysis applied to rules