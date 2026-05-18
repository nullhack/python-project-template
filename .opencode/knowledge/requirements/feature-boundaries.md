---
domain: requirements
tags: [feature-boundaries, story-mapping, delivery-order, bounded-contexts, feature-naming]
last-updated: 2026-05-08
---

# Feature Boundaries

## Key Takeaways

- Feature boundaries are derived from simulation-created .feature files, validated against the delivery order in product_definition.md, the context map, and aggregate boundaries from the domain spec. Each .feature file from simulation is a feature candidate; candidates may be split, renamed, or merged.
- A feature should belong to primarily one bounded context. If a delivery step spans two or more contexts, split it along context boundaries.
- A feature should not span multiple aggregate transactional consistency boundaries. If it does, split along aggregate lines.
- Feature names follow the `[Capability]` pattern from the delivery step. Descriptions answer: what it provides, which context it serves, why it exists, and key entities.
- Cross-cutting concerns (risk management, error handling, observability) are not separate features — they appear as Constraints in the features that implement them.

## Concepts

**Delivery Order as Backbone**: Patton (2014) recommends mapping the user's narrative flow as a backbone, then slicing vertically into releasable increments. The .feature files created during simulation capture the discovered behavior — the delivery order in product_definition.md validates the dependency graph. .feature files are refined into independently deliverable features that follow the validated delivery order.

**Context Alignment Validation**: Each feature candidate must be checked against the domain spec's bounded context table. A feature that touches entities from two or more contexts has a boundary problem. Split it: each context gets its own feature. The domain spec's "Why Separate" column explains why the contexts were split — the feature split must respect the same reasoning.

**Aggregate Boundary Validation**: Aggregates define transactional consistency boundaries. A feature that modifies data across two aggregates in one transaction violates aggregate design. If a delivery step spans multiple aggregates, split the feature so each aggregate's invariants are tested within one feature.

**Naming and Description Convention**: Feature names come from the delivery step name, validated for clarity. Good names are specific enough that a developer knows what to build and a tester knows what to verify. Descriptions follow a four-part pattern: (1) what the feature provides, (2) which bounded context it serves, (3) why it exists — the business need, (4) key entities from the domain spec that belong to this feature.

**Cross-Cutting Concerns**: Risk management, error handling, logging, and observability span multiple contexts. These are not separate features. Instead, they appear as Constraints in the features where they are implemented. The domain spec's context map shows which contexts have safety or error-handling responsibilities. Map those responsibilities to Constraints, not to separate features.

**Exceptions to Context Splitting**: Three patterns justify a feature spanning multiple bounded contexts: (1) Foundational shared types (e.g., "Domain value objects") that all contexts depend on — these belong to a separate shared-kernel feature whose entities have `Domain (shared)` as their context. (2) Orchestrator contexts (e.g., "Execution engine") that coordinate multiple contexts but own no business logic — these are a single feature because splitting the orchestrator would create circular dependencies. (3) Tightly coupled co-deployed contexts (e.g., "Strategy framework" spanning Pricing + Strategy) that share a ubiquitous language and deployment boundary — these are one feature when their integration point is a single protocol call.

## Content

### Feature Boundary Derivation Process

1. **List delivery steps as feature candidates**: Read product_definition.md delivery order. Each numbered step is a feature candidate. Record: step number, name, module, and summary.

2. **Map each candidate to bounded contexts**: For each candidate, identify which bounded contexts its entities belong to using the domain spec's entity table. If a candidate spans multiple contexts, split it.

3. **Map each candidate to aggregates**: For each candidate, identify which aggregate boundaries its entities belong to using the domain spec's aggregate boundary table. If a candidate spans multiple aggregates, validate that the feature does not require cross-aggregate transactions. If it does, split it.

4. **Validate naming**: Each feature name should be a noun phrase that names a cohesive capability. Avoid vague names ("Core", "Utils", "Infrastructure" without qualification). Prefer specific names ("Domain value objects", "Data infrastructure", "Payment adapter").

5. **Write descriptions**: Each description answers four questions: What does this feature provide? Which bounded context does it serve? Why does it exist? Which key entities from the domain spec belong to it?

### Splitting Criteria

When a delivery step spans multiple contexts or aggregates:

| Signal | Split | Keep together |
|--------|-------|---------------|
| Spans 2+ bounded contexts | Split along context boundaries | Shared-kernel types (Domain shared), Orchestrator, Tightly coupled co-deployed |
| Spans 2+ aggregates | Split along aggregate boundaries | If aggregates must be transactionally consistent |
| Delivery step name contains "and" | Likely two features | If "and" joins inseparable aspects |

### Cross-Cutting Concern Mapping

For quality attributes that span contexts (risk, error handling, observability):

1. Check the domain spec context map for which contexts participate in the cross-cutting concern
2. For each participating context, add a Constraint to that context's feature
3. Do NOT create a separate "Risk Management" feature — distribute the constraints

Example: Kill switch behavior appears in Engine (lifecycle control) and Order Execution (cancel all). Both features get a Constraint referencing the kill switch quality attribute.

## Related

- [[requirements/feature-discovery]]
- [[requirements/decomposition]]
- [[domain-modeling/event-storming]]
