---
domain: requirements
tags: [feature-discovery, story-mapping, backlog-creation, gap-analysis]
last-updated: 2026-05-14
---

# Feature Discovery

## Key Takeaways

- Feature discovery synthesizes analysis artifacts (behavioral spec, simulation results, domain model, product definition, glossary) into coherent feature boundaries with scoped business rules. It is a genuine analysis step, not mechanical transcription.
- Each feature captures coarse business rules: one-line statements of behavior that the feature must enforce or enable. These are simulation-validated behavioral statements, not hypotheses.
- Feature boundaries respect bounded context borders, aggregate transactional boundaries, and module dependency order per [[requirements/feature-boundaries]]. Features that span boundaries are flagged for splitting.
- Rules come from two sources: simulation-discovered rules in simulation_results.md and structural rules from the domain model (invariants, relationships, aggregate boundaries).
- Gaps discovered during feature discovery (a bounded context with no feature, a quality attribute with no enforcing feature) are flagged, not silently filled.
- Features progress through a lifecycle of increasing specificity: an empty file with a description → coarse `# Business rules:` and `# Constraints:` comments → full Rule blocks with Examples.

## Concepts

**Feature Boundary Identification**: Deciding where one feature ends and another begins is a design judgment using the delivery order as backbone (Patton, 2014), validated against bounded context and aggregate boundaries from the domain model and behavioral spec. Each delivery step becomes a feature candidate; candidates spanning multiple contexts or aggregates are split per [[requirements/feature-boundaries]].

**Rule Distribution from Simulation**: Rules are discovered during spec simulation and recorded in simulation_results.md. Feature discovery distributes these rules to features based on the bounded context and entities each rule involves. IF a rule spans multiple features → flag for cross-cutting handling.

**Targeted Clarification During Discovery**: When artifacts are ambiguous, contradictory, or incomplete, ask targeted clarification questions using the same interview techniques (CIT, laddering) as discovery interviews, but scoped to the specific feature boundary or rule under consideration. Record answers in the relevant interview notes.

**Gap Analysis**: Systematically verify coverage across three dimensions: (1) every bounded context from the behavioral spec is covered by at least one feature, (2) every quality attribute from the product definition is enforced by at least one feature's constraints, (3) every simulation rule is distributed to at least one feature. Uncovered areas indicate missing features or gaps in the spec itself. Flag both.

**Feature Lifecycle**: Features follow a lifecycle of increasing specificity across phases:
1. **Discovery**: Feature boundaries identified, coarse business rules distributed from simulation results, constraints scoped.
2. **Breakdown**: Coarse rules verified for specificity, written as Rule blocks (descriptive statements, no user stories). INVEST validation applied.
3. **Example Writing and Baseline**: Given/When/Then Examples written, pre-mortems applied, baseline confirmed (feature now has Examples with unique titles).

## Content

### Discovery Sequence

Feature discovery is two sequential activities:

1. **Boundary identification** (discover-features skill): Use the delivery order as backbone. Map each step to bounded contexts and aggregates from the behavioral spec and domain model. Split candidates that span contexts or aggregates. Name features and write descriptions per [[requirements/feature-boundaries]]. Create .feature files with title and description.

2. **Rule distribution** (discover-rules skill): For each feature, assign simulation-discovered rules from simulation_results.md based on bounded context and entity membership. Map quality attributes to constraints. Write coarse `# Business rules:` bullets and `# Constraints:` into each .feature file.

### Gap Analysis Procedure

After distributing rules for all features, verify:

1. **Context coverage**: List every bounded context from the behavioral spec. Check that each has at least one feature. If a context has no feature, flag it as a gap.
2. **Quality attribute enforcement**: List every quality attribute from product_definition.md. Check that each is enforced by at least one feature's Constraints. If a quality attribute has no enforcing feature, flag it as a gap.
3. **Simulation rule distribution**: List every rule from simulation_results.md. Check that each is assigned to at least one feature. If a rule has no feature, flag it as a gap.
4. **E2E test candidate distribution**: List every E2E test candidate from simulation_results.md. Check that each maps to at least one feature's Examples. If a candidate has no feature, flag it as a gap.

Gaps are recorded in the relevant interview notes. Do NOT silently fill gaps with assumed rules.

## Related

- [[requirements/feature-boundaries]]: deriving feature boundaries from delivery order and domain model
- [[requirements/spec-simulation]]: how rules are discovered during simulation
- [[requirements/invest]]: story quality criteria applied to rules
- [[requirements/wsjf]]: feature prioritization applied to BASELINED features
- [[requirements/gherkin]]: writing Examples from rules
- [[requirements/interview-techniques]]: interview methods for clarification
- [[requirements/decomposition]]: splitting Rules
- [[requirements/pre-mortem]]: adversarial analysis applied to rules
