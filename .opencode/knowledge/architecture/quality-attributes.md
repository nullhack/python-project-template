---
domain: architecture
tags: [quality-attributes, architectural-styles, trade-offs, ATAM]
last-updated: 2026-04-29
---

# Quality Attributes

## Key Takeaways

- Quality attributes — not functional requirements — drive architectural decisions (Bass, Clements & Kazman, 2021).
- Six architecturally significant quality attribute categories: Performance, Availability, Security, Modifiability, Reliability, and Usability (Bass et al., 2021).
- Architectural style selection must be justified against quality attribute priorities, not personal preference — each style optimises for different attributes.
- Quality attributes often conflict — optimising for Performance may harm Modifiability; the utility tree method (ATAM) forces explicit prioritisation with business value justification.

## Concepts

**Quality Attributes as Architectural Drivers** (Bass et al., 2021) — Quality attributes are measurable properties of a system's architecture, distinct from functional requirements (what the system does). Performance, Availability, and Security constrain the architecture; Modifiability, Reliability, and Usability shape its flexibility. Each quality attribute produces concrete architectural tactics that directly affect module structure, dependency direction, and communication patterns.

**Quality Attribute Conflicts** — Performance (fast response, low latency) often conflicts with Modifiability (abstraction layers, indirection). Security (encryption, validation) often conflicts with Performance (overhead). Availability (redundancy, failover) often conflicts with cost constraints. The architect must prioritise which attributes matter most for the business and make trade-offs explicitly, documented as ADRs.

**ATAM Utility Tree** — The Architecture Tradeoff Analysis Method provides a structured way to prioritise quality attributes: stakeholders rank attribute scenarios by business value (High/Medium/Low) and by architectural difficulty (High/Medium/Low). The intersection produces a prioritised set of scenarios that the architecture must address first. This prevents architects from over-engineering for low-value attributes or under-engineering for high-value ones.

**Architectural Tactics** — Each quality attribute has a set of design tactics that directly address it: Performance uses resource arbitration, concurrency, and caching; Availability uses redundancy, fault detection, and recovery; Modifiability uses encapsulation, substitution, and binding time. Tactics are the building blocks that architects combine into architectural styles.

## Content

### Quality Attribute Taxonomy

| Category | Definition | Key Tactics |
|---|---|---|
| Performance | Response time and throughput under load | Caching, concurrency, resource pooling, load balancing |
| Availability | System uptime and fault tolerance | Redundancy, failover, circuit breaker, health checks |
| Security | Protection against unauthorised access and data breaches | Authentication, authorisation, encryption, audit logging |
| Modifiability | Ease of changing the system without side effects | Encapsulation, substitution, dependency inversion, binding time |
| Reliability | Correct operation over time under stated conditions | Input validation, checksums, transaction boundaries, retry |
| Usability | Ease of use for end users | Consistent UI patterns, clear error messages, progressive disclosure |

### Architectural Styles and Quality Attributes

| Style | Optimises For | Trades Off |
|---|---|---|
| Monolith | Simplicity, fast time-to-market, low-latency intra-module calls | Independent deployment, team autonomy |
| Microservices | Independent deployment, team autonomy, fault isolation | Operational complexity, inter-service latency |
| Event-driven | Loose coupling, async processing, scalability | Eventual consistency, debugging complexity |
| Serverless | Cost optimisation (pay-per-use), auto-scaling | Cold starts, vendor lock-in, debugging difficulty |
| Hexagonal | Testability, domain isolation, delivery-mechanism independence | Indirection overhead, architectural discipline required |

### Quality Attributes in Architecture Documents

When documenting quality attributes in `technical_design.md`:
- Each attribute must link to an architectural decision that addresses it
- Each architectural decision must link to an ADR
- Priority order must be explicit (which attribute wins when they conflict)

## Related

- [[architecture/technical-design]]
- [[architecture/adr]]
- [[architecture/assessment]]