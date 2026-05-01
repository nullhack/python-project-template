---
domain: domain-modeling
tags: [ddd, event-storming, bounded-contexts, aggregates, domain-events]
last-updated: 2026-04-29
---

# Event Storming & Domain Modeling

## Key Takeaways

- Event storming surfaces domain events (past-tense verbs), commands (imperative verbs), and aggregates (transactional consistency boundaries) from stakeholder interviews (Brandolini, 2012).
- Bounded contexts group related events, commands, and entities — a context boundary is where a term changes meaning (Evans, 2003).
- Aggregates define transactional consistency boundaries (Evans, 2003) — everything within an aggregate must be consistent after a transaction; everything between aggregates is eventually consistent.
- Domain events are expressed in past tense (OrderPlaced, PaymentReceived); commands in imperative (PlaceOrder, ReceivePayment).

## Concepts

**Event Storming** (Brandolini, 2012) — A collaborative workshop technique where domain experts place domain events on a timeline. The process: identify events (what happens), identify commands (what triggers them), group into bounded contexts (areas of related meaning), and identify aggregates (consistency boundaries). Event storming produces: an event map, candidate bounded contexts, and candidate aggregates.

**Bounded Contexts** (Evans, 2003) — A bounded context is a linguistic boundary — within it, every term has exactly one meaning. When the same word means different things in different parts of the domain, that's a context boundary. For example, "Product" might mean a catalog item in the Sales context and a physical item in the Warehouse context.

**Aggregates** (Evans, 2003) — An aggregate is a cluster of domain objects treated as a single unit for data changes. Every aggregate has a root entity and a consistency boundary: all invariants must be satisfied within a single transaction. References from outside the aggregate point only to the root. Aggregates are the unit of transactional consistency.

**Domain Events** — Something that happened in the domain, expressed in past tense. Events are facts — they cannot be undone, only compensated. Events capture the vocabulary of the domain: OrderPlaced, PaymentReceived, InventoryDepleted.

**Commands** — An intent to make something happen, expressed in imperative. Commands may be rejected (insufficient funds, out of stock). When a command succeeds, it produces a domain event: PlaceOrder → OrderPlaced.

## Content

### Event Storming Steps

1. Brainstorm domain events from interview notes — past-tense, business-relevant
2. Place events on a chronological timeline
3. For each event, identify the command that triggers it
4. Group related events and commands into candidate bounded contexts
5. Within each context, identify aggregate boundaries — which entities must be transactionally consistent
6. Flag contradictions (same term, different meaning) as context boundaries
7. Flag gaps (events without commands, or commands without events) for follow-up

### Aggregate Design Rules

- An aggregate must fit in memory — if it's too large, split it
- An aggregate must be consistent after every transaction — if invariants span two aggregates, merge them or accept eventual consistency
- References between aggregates use identity (ID), not object references
- One aggregate per transaction — if you need to update two aggregates atomically, reconsider your boundaries

### Context Mapping (Evans, 2003)

- Upstream/Downstream: one context provides data/services, the other consumes
- Anti-corruption layer: a translation boundary that prevents upstream concepts from leaking into downstream
- Conformist: downstream accepts upstream's model as-is
- Open-host service: upstream publishes a standardized protocol

## Related

- [[domain-modeling/context-mapping]]
- [[requirements/ubiquitous-language]]
- [[architecture/technical-design]]