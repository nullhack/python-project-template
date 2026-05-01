---
domain: architecture
tags: [api-contracts, event-contracts, interfaces, rest, hexagonal-architecture]
last-updated: 2026-04-29
---

# Contract Design

## Key Takeaways

- API contracts, event contracts, and interface definitions are the boundaries between modules — design them before implementation (contract-first design).
- REST constraints (Fielding, 2000) define API contracts as resource shapes and media types, not procedure calls — the contract is what data a resource contains and how it can transition, not a method signature.
- Event contracts must specify not just payload schema but also ordering guarantees, delivery semantics, and error handling (Hohpe & Woolf, 2003).
- Interface definitions (Protocol/abstract classes) in the domain layer define what the domain needs; infrastructure implements them — the dependency arrow always points inward (Cockburn, 2005; Evans, 2003).

## Concepts

**Contract-First Design** — Define the boundaries between modules before implementing them. API contracts specify request/response shapes, error codes, authentication, and versioning. Event contracts specify event names, payload schemas, ordering guarantees, and delivery semantics. Interface definitions specify the operations the domain requires without specifying how they are implemented. All three contract types are living documents that evolve with the system but must be versioned to maintain backward compatibility.

**REST and API Contracts** (Fielding, 2000) — REST defines API contracts through resources (identified by URIs), representations (media types like JSON Schema), and standard methods (GET, POST, PUT, DELETE). The Uniform Interface constraint means the client only needs to understand media types and standard methods, not server implementation details. API contracts should specify: resource paths, request/response schemas, error response formats, authentication requirements, and rate limits.

**Event Contracts** (Hohpe & Woolf, 2003) — Asynchronous messaging between systems requires explicit contracts covering: payload schema (event type, aggregate ID, timestamp, data fields), ordering guarantees (per-sender FIFO, causal ordering, or none), delivery semantics (at-most-once, at-least-once, exactly-once), and error handling (dead letter channels, retry policies, circuit breakers). Event contracts decouple time (producer and consumer don't need to be available simultaneously) and schema (each system retains its own model through translation layers).

**Interface Definitions** — In hexagonal architecture (Cockburn, 2005), the domain layer defines Protocol interfaces (ports) that specify what operations the domain needs. Infrastructure adapters implement these ports. The domain never imports from infrastructure — the dependency arrow always points inward (infrastructure → application → domain). Interface definitions must specify: method signatures, parameter types, return types, error types, and preconditions.

## Content

### API Contract Specification

Every API endpoint must document:

| Element | Content |
|---|---|
| Path | `/<resource>/<id>` with path parameters |
| Method | GET, POST, PUT, DELETE |
| Request schema | Fields, types, required/optional, validation rules |
| Response schema | Fields, types, status codes |
| Error responses | Error code, message, retry guidance |
| Authentication | Required auth mechanism |
| Versioning | Header or URL-based version strategy |

### Event Contract Specification

Every event must document:

| Element | Content |
|---|---|
| Event type | Past-tense domain event name (e.g., `OrderPlaced`) |
| Payload schema | Fields, types, required/optional |
| Ordering | None, per-sender FIFO, or causal |
| Delivery | At-most-once, at-least-once, or exactly-once |
| Error handling | Dead letter channel, retry policy, circuit breaker |
| Produced by | Module/context that emits the event |
| Consumed by | Module/context that handles the event |

### Interface Definition Specification

Every domain port must document:

| Element | Content |
|---|---|
| Port name | Domain operation name (e.g., `PaymentGateway`) |
| Methods | Method signatures with parameter and return types |
| Errors | Domain error types the method can raise |
| Preconditions | Conditions that must hold before calling |
| Implementations | Which infrastructure adapter implements this port |

## Related

- [[architecture/technical-design]]
- [[architecture/quality-attributes]]
- [[domain-modeling/context-mapping]]