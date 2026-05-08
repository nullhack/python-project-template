---
domain: domain-modeling
tags: [ddd, bounded-contexts, entities, relationships, aggregates, domain-model]
last-updated: 2026-05-08
---

# Domain Modeling

## Key Takeaways

- Domain modeling formalizes event storming candidates into bounded contexts, entities, relationships, aggregate boundaries, and a context map — the convergent synthesis after divergent exploration.
- Bounded contexts are linguistic boundaries where every term has one meaning. Formalize by clustering aggregates that share a ubiquitous language and separating where terms change meaning (Evans, 2003).
- Entities have identity and lifecycle (Slot, TrackedOrder, Position). Value objects have no identity — defined by attributes (Token, Pair, Orderbook). Only entities can be aggregate roots.
- Relationships capture composition (Orderbook composed of PriceLevels), dependency (Strategy uses MarketSnapshot), and domain flow (Strategy produces OrderAction). Cardinality (1:1, 1:N, M:N) constrains design.
- Aggregate boundaries define transactional consistency. Every invariant within an aggregate must hold after each transaction. Invariants spanning entities indicate they belong to the same aggregate.

## Concepts

**Formalization Process**: Event storming produces candidates (events, commands, aggregates, contexts). Domain modeling formalizes these into a structural specification. For each candidate context: identify entities from event/command payloads, classify as entities (have identity) or value objects (defined by attributes), determine relationships, and define aggregate boundaries from transactional consistency requirements.

**Bounded Context Identification**: Contexts emerge from linguistic boundaries. A boundary exists when: the same term changes meaning, different consistency requirements apply, or independent deployment is needed. Each context documents: name, responsibility, key entities, business capability, why separate, and integration points.

**Entity vs Value Object**: An entity has identity persisting across state changes (a Slot is the same Slot regardless of state). A value object has no identity — defined entirely by attribute values (PriceLevel at price=100, qty=5 equals any other with same values). Only entities can be aggregate roots. Value objects are always owned by an entity.

**Relationship Extraction**: Relationships derive from: event flow (entity A produces an event entity B consumes), data flow (entity A composed from entity B's data), and domain constraints (a rule involves both entities). Three types: composition, dependency, domain flow. Cardinality constrains design: 1:1 enables direct reference, 1:N enables collection, M:N requires indirection.

**Aggregate Boundary Determination**: An aggregate is the unit of transactional consistency. Group entities sharing invariants (business rules that must hold atomically). Split when: the aggregate exceeds memory, transactions span multiple aggregates, or different parts have different consistency requirements. One aggregate per transaction; cross-aggregate references use identity only.

## Content

### Formalization Steps

1. **List entity candidates from events and commands**: Each event's subject is an entity candidate. Each command's target is an entity candidate. Each read model references entity candidates. Deduplicate across events.

2. **Classify each candidate**: Entity if it has identity (ID or natural key) and lifecycle. Value object if defined by attributes and immutable.

3. **Determine relationships**: For each pair, classify: composition (A contains B), dependency (A uses B), or domain flow (A produces output for B). Determine cardinality: 1:1, 1:N, M:N.

4. **Define aggregate boundaries**: Group entities sharing invariants. Document root entity, invariants, and business reason for grouping per [[domain-modeling/event-storming#key-takeaways]].

5. **Identify context boundaries**: Group aggregates sharing a ubiquitous language. Document: name, responsibility, key entities, capability, why separate, integration points.

6. **Map context relationships**: Classify each inter-context relationship per [[domain-modeling/context-mapping#key-takeaways]]. Document upstream, downstream, pattern, and any anti-corruption layer.

### Entity Table Format

| Field | Purpose |
|---|---|
| Name | PascalCase entity name |
| Type | Entity or Value Object |
| Description | What it represents |
| Bounded Context | Owning context |
| Aggregate Root? | Yes if root, — if value object |

### Aggregate Boundary Table Format

| Field | Purpose |
|---|---|
| Aggregate | PascalCase name |
| Root Entity | Identity root |
| Invariants | Business rules enforced |
| Why Grouped | Business reason for boundary |
| Bounded Context | Owning context |

### Boundary Decision Heuristics

- If an invariant references two entities, they share an aggregate
- If an aggregate exceeds memory, split and accept eventual consistency
- If two contexts use the same term with different definitions, they are separate contexts
- If removing one aggregate doesn't change term meanings in another, they are separate contexts
- If a rule can be checked eventually (not immediately), entities may be in different aggregates

## Related

- [[domain-modeling/event-storming]]
- [[domain-modeling/context-mapping]]
- [[requirements/ubiquitous-language]]
