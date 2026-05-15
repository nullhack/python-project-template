---
domain: requirements
tags: [rule-derivation, discovered-rules, invariants]
last-updated: 2026-05-14
---

# Rule Derivation

## Key Takeaways

- Rules come from two sources: simulation-discovered rules (now written directly to .feature files) and structural rules from the domain spec (invariants, relationships, aggregate boundaries).
- Simulation rules are descriptive statements discovered by walking External Contracts through happy/edge/error scenarios. Each discovered rule traces to the walkthrough and External Contract that produced it.
- Structural rules come from aggregate invariants: "[Entity] must always [condition]." These are non-negotiable consistency boundaries.
- Quality attributes from product_definition.md constrain rules: each attribute produces at least one Constraint that bounds the feature's behavior with a measurable threshold.

## Concepts

**Simulation-Discovered Rules**: The primary source of behavioral rules. As the SA walks through External Contracts in the domain spec with happy/edge/error walkthroughs, rules emerge about what the system must do, must not do, and what happens when things go wrong. These rules are written as Rule blocks in .feature files during simulation.

**Structural Rules from Domain Spec**: Aggregate invariants from the domain spec produce structural rules — non-negotiable consistency boundaries. These rules are already present in the domain spec and are written to .feature files alongside discovered rules during simulation.

**Quality Attribute -> Constraint Mapping**: Each quality attribute in product_definition.md (latency, reliability, safety) constrains feature behavior. Map each attribute to the feature(s) responsible for enforcing it. If no feature enforces a quality attribute, it is a gap. Constraints include measurable thresholds: "Latency: tick-to-order under 100ms", "Reliability: no orphaned orders after crash."

**Rule Distribution**: Rules are written directly to .feature files during simulation, grouped by bounded context and entities. IF a discovered rule spans multiple features → flag for cross-cutting handling. Every rule must be assigned to at least one feature. Gaps indicate missing features or incomplete simulation.

## Content

### Simulation-to-Feature Flow

During simulation, for each bounded context walked:

**Step 1: Write discovered rules to .feature files.** As the SA walks through each bounded context, discovered rules are written as Rule blocks directly into the .feature file corresponding to that context's entities. No separate distribution step is needed.

**Step 2: Assign structural rules from domain spec.** For each aggregate invariant in the domain spec, assign it to the feature that contains the aggregate root. These are non-negotiable consistency boundaries.

**Step 3: Map quality attributes to constraints.** For each quality attribute in product_definition.md:
- Which feature(s) enforce this attribute? → Add Constraint to those features
- Include measurable threshold from the quality attribute
- If no feature enforces it → flag in interview notes as a gap

**Step 4: Write constraints to .feature files.** Write each constraint under `# Constraints:` in the relevant .feature file.

### Traceability Verification

After distributing rules for all features, verify:

1. **Every discovered rule → at least one feature.** If a rule has no feature, either it's out of scope or a feature is missing. Discovered rules originate in .feature files created during simulation.
2. **Every aggregate invariant → at least one feature.** If an invariant has no feature, flag it as a gap.
3. **Every quality attribute → at least one constraint.** If a quality attribute has no enforcing feature, flag it as a gap.
4. **Every feature → at least one business rule.** If a feature has no rules, flag it as potentially unnecessary.

## Related

- [[requirements/spec-simulation]]: how rules are discovered during simulation
- [[requirements/feature-discovery]]
- [[requirements/feature-boundaries]]
- [[domain-modeling/behavioral-contracts]]: External Contracts that simulation walks
