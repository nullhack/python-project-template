---
domain: domain-modeling
tags: [ddd, context-mapping, bounded-contexts, integration, anti-corruption-layer]
last-updated: 2026-04-29
---

# Context Mapping

## Key Takeaways

- Context mapping defines how bounded contexts relate to each other — each relationship pattern carries specific coordination costs and risk trade-offs (Vernon, 2013).
- Nine relationship patterns describe inter-context dynamics: Partnership, Shared Kernel, Customer-Supplier, Conformist, Anticorruption Layer, Separate Ways, Open Host Service, Published Language, and Big Ball of Mud (Vernon, 2013; Evans, 2003).
- Selecting the correct pattern prevents model pollution and reduces integration friction — use ACL when downstream has limited influence, Customer-Supplier when both teams negotiate, Open Host Service when many consumers need a standardised protocol.
- Integration points are the seams between contexts — each must define its mechanism (sync API, async event, shared DB), its contract, and its error handling.

## Concepts

**Context Relationship Patterns** (Vernon, 2013) — Nine patterns describe the social and technical contracts between bounded contexts. Each pattern carries obligations: Customer-Supplier demands upstream awareness of downstream needs; Conformist accepts upstream dominance; Anticorruption Layer isolates downstream from upstream model drift. Naming the relationship makes both teams' obligations explicit.

**Pattern Selection** — The choice of relationship pattern depends on team influence, model purity needs, and integration complexity. When the downstream team has limited influence over the upstream model, use an Anticorruption Layer. When both teams can negotiate, use Customer-Supplier. When many consumers need access, use Open Host Service with a Published Language. When the cost of integration exceeds the benefit, use Separate Ways.

**Integration Points** — Every seam between bounded contexts is an integration point. Each integration point must specify: the mechanism (synchronous API, asynchronous event, shared database, file exchange), the contract (schema, versioning, backward compatibility), and the error handling (retry, dead letter, circuit breaker). Undefined integration points are the primary source of coupling failures.

**Anti-Corruption Layers** — An ACL is a translation boundary that prevents upstream concepts from leaking into the downstream model. It translates between the upstream's data model and the downstream's domain model, allowing the downstream context to maintain its own ubiquitous language even when consuming services from a differently-modelled context.

## Content

### Context Relationship Patterns

| Pattern | Upstream Role | Downstream Role | When to Use |
|---|---|---|---|
| Partnership | Coordinates with downstream | Coordinates with upstream | Teams in close collaboration; high trust |
| Shared Kernel | Maintains shared subset | Maintains shared subset | Small shared model; both teams commit to changes |
| Customer-Supplier | Considers downstream needs | Influences upstream decisions | Upstream has power but values downstream input |
| Conformist | Provides model as-is | Conforms to upstream model | Downstream has no influence; accept and adapt |
| Anticorruption Layer | N/A (downstream decision) | Translates upstream model to own model | Downstream needs model purity despite external model |
| Separate Ways | N/A | N/A | Integration cost exceeds benefit; each solves independently |
| Open Host Service | Publishes standard protocol | Consumes via standard protocol | Many downstream consumers need access |
| Published Language | Publishes well-documented model | Consumes via published schema | Standard interchange format (e.g., JSON Schema, XML) |
| Big Ball of Mud | N/A | N/A | Legacy or poorly structured context; contain, don't extend |

### Integration Point Specification

Each integration point must document:

1. **Mechanism**: Synchronous API, asynchronous event, shared database, or file exchange
2. **Contract**: Request/response schemas, event payload schemas, versioning strategy
3. **Error handling**: Retry policy, dead letter channel, circuit breaker, timeout behaviour
4. **Ownership**: Which context owns the contract definition (upstream or downstream)

### Anti-Corruption Layer Design

An ACL has three components:
- **Inbound adapter**: Receives data from upstream in the upstream's model
- **Translator**: Maps upstream concepts to downstream domain concepts
- **Domain interface**: Exposes upstream data in the downstream's ubiquitous language

The ACL should be the only place where upstream model concepts appear in downstream code.

## Related

- [[domain-modeling/event-storming]]
- [[architecture/assessment]]
- [[architecture/contract-design]]