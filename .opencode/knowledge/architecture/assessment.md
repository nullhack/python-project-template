---
domain: architecture
tags: [architecture, delivery-mechanism, bounded-contexts, hexagonal-architecture]
last-updated: 2026-04-29
---

# Architecture Assessment

## Key Takeaways

- Delivery mechanism is the boundary between the domain and the outside world (Cockburn, 2005) — HTTP, CLI, message queue, etc. — it must be verified against the product definition before designing anything.
- Architecture exists when system.md, technical_design.md, and context_map.md all contain meaningful content aligned with the current domain.
- If architecture exists but delivery mechanism mismatches, record it as an ADR before proceeding.
- Hexagonal architecture (Ports & Adapters — Cockburn, 2005) keeps the domain independent of delivery mechanism — verify this is followed.
- SA conducts an assessment interview to verify and correct quality attributes, deployment constraints, and hidden requirements before routing.

## Concepts

**Delivery Mechanism Verification** — Before designing a feature, the architect must verify that the delivery mechanism stated in the product definition (e.g., "web application", "CLI tool", "API service") matches the actual codebase implementation. A mismatch (e.g., product says "web" but codebase is CLI) must be recorded as an ADR and resolved before proceeding. This checkpoint prevents building on a foundation that doesn't match the product's intent.

**Architecture Existence Check** — Architecture is considered to exist when three documents contain meaningful, aligned content: system.md (current state snapshot), technical_design.md (technical decisions), and context_map.md (bounded context relationships). Empty or placeholder content does not count. If all three exist and are coherent, the architect evaluates whether the existing architecture covers the new feature or needs updating.

**Hexagonal Architecture (Ports & Adapters — Cockburn, 2005)** — The domain core must not depend on infrastructure. Ports define what the domain needs; adapters provide concrete implementations. When reviewing architecture, verify that external dependencies (databases, frameworks, APIs) are behind Protocol interfaces, not directly referenced in domain code.

**Assessment Interview** — The SA interviews the stakeholder to surface information not captured in the artifacts. Topics: quality attribute priorities (are the documented priorities accurate and complete?), deployment constraints (does the deployment section match reality?), hidden requirements (constraints not captured in the artifacts), and architecture gaps (does the current system fail to cover anything needed?). Apply gap-finding techniques from [[requirements/interview-techniques]]: use CIT to probe for specific past failures, use Laddering to climb from surface preferences to real constraints. Apply a pre-mortem from [[requirements/pre-mortem]]: "Imagine this architecture is built exactly as designed, all tests pass, but it fails in production — what would be missing?" Corrections are written into existing artifacts (product_definition.md), not into separate interview notes.

## Content

### Delivery Mechanism Checkpoint

The delivery mechanism is the outermost layer — how users or systems interact with the product. Common delivery mechanisms:

- Web application (HTTP server, browser-based)
- CLI tool (terminal interface)
- API service (REST, GraphQL, gRPC)
- Desktop application (GUI)
- Library/SDK (programmatic interface)

When assessing architecture for a new feature:

1. Read the product definition's deployment section
2. Verify the codebase's actual entry points match
3. If mismatched, create an ADR documenting the discrepancy and the resolution path
4. Only proceed with technical design after the delivery mechanism is verified

### Architecture Existence Decision Tree

| Condition | Routing |
|---|---|
| No architecture documents exist | Needs full architecture (technical-design) |
| Architecture exists, covers the feature | No architecture needed (proceed to planning) |
| Architecture exists, needs updating for this feature | Needs context update (context-map then technical-design) |
| Architecture exists, fundamental gap discovered | Needs discovery (back to discovery flow) |

### Hexagonal Architecture Verification

When reviewing existing architecture:

- Every external dependency must have a Protocol (interface) in the domain layer
- The domain layer must have zero imports from infrastructure packages
- Adapters must implement domain-defined Ports, not the other way around
- If the domain references a concrete technology, it's a violation

## Related

- [[architecture/quality-attributes]]
- [[architecture/reconciliation]]
- [[requirements/pre-mortem]]
- [[workflow/flowr-spec]]