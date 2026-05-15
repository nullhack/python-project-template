---
domain: requirements
tags: [feature-discovery, story-mapping, backlog-creation, gap-analysis]
last-updated: 2026-05-14
---

# Feature Discovery

## Key Takeaways

- Feature discovery synthesizes analysis artifacts (domain spec, simulation results, domain spec, product definition, glossary) into coherent feature boundaries with scoped business rules. It is a genuine analysis step, not mechanical transcription.
- Each feature captures coarse business rules: one-line statements of behavior that the feature must enforce or enable. These are simulation-validated behavioral statements, not hypotheses.
- Feature boundaries respect bounded context borders, aggregate transactional boundaries, and module dependency order per [[requirements/feature-boundaries]]. Features that span boundaries are flagged for splitting.
- Rules are written directly to .feature files during simulation. Planning refines: splitting, renaming, adding behavior hints.
- Gaps discovered during feature discovery (a bounded context with no feature, a quality attribute with no enforcing feature) are flagged, not silently filled.
- Features progress through a lifecycle of increasing specificity: Rule blocks from simulation → behavior hints → Example blocks and Scenario Outlines.

## Concepts

**Feature Boundary Identification**: Deciding where one feature ends and another begins is a design judgment using the delivery order (from product_definition.md) validated against the context map as backbone (Patton, 2014), cross-checked against bounded context and aggregate boundaries from the domain spec. Each delivery step becomes a feature candidate; candidates spanning multiple contexts or aggregates are split per [[requirements/feature-boundaries]].

**Rule Organization from .feature Files**: Rules are written directly to .feature files during simulation, grouped by bounded context. Feature discovery redistributes Rule blocks when feature files are split or renamed. IF a rule spans multiple features → flag for cross-cutting handling.

**Targeted Clarification During Discovery**: When artifacts are ambiguous, contradictory, or incomplete, ask targeted clarification questions using the same interview techniques (CIT, laddering) as discovery interviews, but scoped to the specific feature boundary or rule under consideration. Record answers in the relevant interview notes.

**Gap Analysis**: Systematically verify coverage across three dimensions: (1) every bounded context from the domain spec is covered by at least one feature, (2) every quality attribute from the product definition is enforced by at least one feature's constraints, (3) every discovered rule is mapped to at least one feature. Uncovered areas indicate missing features or gaps in the spec itself. Flag both.

**Feature Lifecycle**: Features follow a lifecycle of increasing specificity across phases:
1. **Discovery**: Feature boundaries identified from simulation-created .feature files. Features are split/renamed based on Delivery Order and context map. Rule blocks are redistributed (content unchanged). Quality attributes mapped to # Constraints:.
2. **Breakdown**: Rules validated against INVEST, behavior hints added.
3. **Example Writing and Baseline**: Behavior hints converted to Gherkin Example/Scenario Outline blocks.

## Content

### Discovery Sequence

Feature discovery is two sequential activities:

1. **Boundary identification** (discover-features skill): Use the delivery order from product_definition.md as backbone. Map each step to bounded contexts and aggregates from the domain spec. Split candidates that span contexts or aggregates. Name features and write descriptions per [[requirements/feature-boundaries]].

2. **Rule organization** (discover-rules skill): For each feature, organize the Rule blocks already written to .feature files during simulation. Split/rename Rules per context boundaries. Map quality attributes to constraints. Write `# Constraints:` into each .feature file.

### Gap Analysis Procedure

After distributing rules for all features, verify:

1. **Context coverage**: List every bounded context from the domain spec. Check that each has at least one feature. If a context has no feature, flag it as a gap.
2. **Quality attribute enforcement**: List every quality attribute from product_definition.md. Check that each is enforced by at least one feature's Constraints. If a quality attribute has no enforcing feature, flag it as a gap.
3. **Discovered rule coverage**: List every discovered rule from .feature files. Check that each is assigned to at least one feature. If a rule has no feature, flag it as a gap.


Gaps are recorded in the relevant interview notes. Do NOT silently fill gaps with assumed rules.

## Related

- [[requirements/feature-boundaries]]: deriving feature boundaries from delivery order and domain spec
- [[requirements/spec-simulation]]: how rules are discovered during simulation
- [[requirements/invest]]: INVEST criteria applied to Rule blocks
- [[requirements/wsjf]]: feature prioritization applied to BASELINED features
- [[requirements/gherkin]]: writing Examples from rules
- [[requirements/interview-techniques]]: interview methods for clarification
- [[requirements/decomposition]]: splitting Rules
- [[requirements/pre-mortem]]: adversarial analysis applied to rules
