---
domain: requirements
tags: [rule-derivation, business-rules, invariants, simulation-rules]
last-updated: 2026-05-14
---

# Rule Derivation

## Key Takeaways

- Rules come from two sources: simulation-discovered rules (behavioral, from walking scenarios) and structural rules from the domain model (invariants, relationships, aggregate boundaries).
- Simulation rules are descriptive statements discovered by walking External Contracts through happy/edge/error scenarios. Each rule cites the scenario and External Contract that produced it.
- Structural rules come from aggregate invariants: "[Entity] must always [condition]." These are non-negotiable consistency boundaries.
- Quality attributes from product_definition.md constrain rules: each attribute produces at least one Constraint that bounds the feature's behavior with a measurable threshold.

## Concepts

**Simulation-Discovered Rules**: The primary source of behavioral rules. As the SA walks through External Contracts in the behavioral spec with happy/edge/error scenarios, rules emerge about what the system must do, must not do, and what happens when things go wrong. These rules are recorded in simulation_results.md and distributed to features during discovery.

**Structural Rules from Domain Model**: Aggregate invariants from the domain model produce structural rules — non-negotiable consistency boundaries. These rules are already present in the domain model and are distributed to features alongside simulation rules during discovery.

**Quality Attribute -> Constraint Mapping**: Each quality attribute in product_definition.md (latency, reliability, safety) constrains feature behavior. Map each attribute to the feature(s) responsible for enforcing it. If no feature enforces a quality attribute, it is a gap. Constraints include measurable thresholds: "Latency: tick-to-order under 100ms", "Reliability: no orphaned orders after crash."

**Rule Distribution**: Rules are distributed to features based on the bounded context and entities they involve. IF a rule spans multiple features → flag for cross-cutting handling. Every rule must be assigned to at least one feature. Gaps indicate missing features or incomplete simulation.

## Content

### Distribution Procedure

For each feature, starting with the feature that has the most entities from the behavioral spec:

**Step 1: Assign simulation rules to features.** Using the bounded context and entity information in simulation_results.md, assign each rule to the feature that corresponds to its context and entities.

**Step 2: Assign structural rules from domain model.** For each aggregate invariant in the domain model, assign it to the feature that contains the aggregate root. These are non-negotiable consistency boundaries.

**Step 3: Map quality attributes to constraints.** For each quality attribute in product_definition.md:
- Which feature(s) enforce this attribute? → Add Constraint to those features
- Include measurable threshold from the quality attribute
- If no feature enforces it → flag in interview notes as a gap

**Step 4: Write to .feature files.** Write each assigned rule as a coarse bullet under `# Business rules:` in the relevant .feature file. Write each constraint under `# Constraints:`.

### Traceability Verification

After distributing rules for all features, verify:

1. **Every simulation rule → at least one feature.** If a rule has no feature, either it's out of scope or a feature is missing.
2. **Every aggregate invariant → at least one feature.** If an invariant has no feature, flag it as a gap.
3. **Every quality attribute → at least one constraint.** If a quality attribute has no enforcing feature, flag it as a gap.
4. **Every feature → at least one business rule.** If a feature has no rules, flag it as potentially unnecessary.

## Related

- [[requirements/spec-simulation]]: how rules are discovered during simulation
- [[requirements/feature-discovery]]
- [[requirements/feature-boundaries]]
- [[domain-modeling/behavioral-contracts]]: External Contracts that simulation walks
