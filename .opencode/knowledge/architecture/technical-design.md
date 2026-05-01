---
domain: architecture
tags: [technical-design, architectural-styles, c4-diagrams, hexagonal-architecture, module-structure]
last-updated: 2026-04-29
---

# Technical Design

## Key Takeaways

- Architectural style must be selected based on quality attributes and deployment constraints — not personal preference.
- C4 diagrams provide four levels of abstraction (Brown, 2018): Context (system in environment), Container (deployable units), Component (modules within containers), Code (classes and functions).
- Module structure follows separation of concerns — domain logic must not depend on infrastructure (Cockburn, 2005; Evans, 2003).
- API contracts, event contracts, and interface definitions are the boundaries between modules — design them before implementation.

## Concepts

**Architectural Styles** — Common styles and when to choose them: Monolith (single deployment, simple ops, low latency between modules), Microservices (independent deployment, team autonomy, high operational complexity), Event-driven (loose coupling, eventual consistency, async workflows), Serverless (pay-per-use, auto-scaling, cold starts), Hexagonal/Ports & Adapters (testability, domain isolation, delivery-mechanism independence).

**C4 Diagrams** (Brown, 2018) — Four levels of architectural visualization: Context (actors and external systems), Container (deployable units and their tech stacks), Component (internal modules and their responsibilities), Code (individual classes — rarely needed). Always start with Context, then Container. Component diagrams are optional. Code diagrams are rarely necessary.

**Module Structure** — Organize by bounded context first (Evans, 2003), then by layer (domain, application, infrastructure). Domain layer has zero infrastructure imports. Application layer orchestrates use cases. Infrastructure layer implements external concerns. The dependency arrow always points inward: infrastructure → application → domain (Clean Architecture — Martin, 2012; Hexagonal Architecture — Cockburn, 2005).

**Contract-First Design** — Define the boundaries before the implementation: API contracts (request/response shapes, error codes, authentication), Event contracts (event names, payload schemas, ordering guarantees), Interface definitions (Protocol/abstract classes that the domain defines and infrastructure implements).

## Content

### Architectural Style Selection

| Quality Attribute Priority | Recommended Style |
|---|---|
| Simplicity, fast time-to-market | Monolith |
| Team autonomy, independent scaling | Microservices |
| Loose coupling, async workflows | Event-driven |
| Cost optimization, variable load | Serverless |
| Testability, domain isolation | Hexagonal |

Hybrid approaches are valid: a monolith with hexagonal internals, or microservices with event-driven communication between them.

### C4 Diagram Guidelines

- Context diagram: always include — shows the system boundary and external actors
- Container diagram: always include — shows deployable units and tech choices
- Component diagram: include when module structure is non-trivial
- Code diagram: only for complex algorithms or critical paths

### Module Structure Template

```
feature_name/
  domain/        # Business logic, zero infrastructure imports
  application/   # Use case orchestration
  infrastructure/ # External concerns (DB, HTTP, queues)
  api/           # Delivery mechanism (routes, serializers)
```

## Related

- [[architecture/assessment]]
- [[architecture/quality-attributes]]
- [[architecture/contract-design]]