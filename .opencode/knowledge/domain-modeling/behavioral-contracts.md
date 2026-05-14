---
domain: domain-modeling
tags: [behavioral-contracts, external-contracts, simulation-target, io-specification]
last-updated: 2026-05-14
---

# Behavioral Contracts

## Key Takeaways

- External Contracts define how users and external systems interact with a bounded context. They are the primary simulation target: "given this input, the system produces this output." All contracts for all contexts live in a single monolithic domain_spec.md file.
- Each contract has seven fields: Actor, Trigger, Input, Output, Errors, Side Effects, Preconditions. Contracts are `#### <Contract Name>` headings within each context's `### External Contracts` section.
- Contracts start with ? for unknowns at iteration 0. Simulation fills in specifics through scenario walkthrough.
- Contracts are NOT API specifications — they are behavioral descriptions that may map to CLI commands, HTTP endpoints, event handlers, or internal operations.

## Concepts

**External Contract Fields**:
- **Actor**: who or what invokes this — a user persona, an external system, a CLI, a timer, or another bounded context.
- **Trigger**: what initiates the interaction — a command, an HTTP request, a CLI invocation, a domain event, or a scheduled time.
- **Input**: the data shape arriving with the trigger. Fields may be ? at iteration 0, resolved by simulation.
- **Output**: the data shape produced on success. Fields may be ? at iteration 0, resolved by simulation.
- **Errors**: a mapping of error conditions to error responses. Discovered during error-path simulation.
- **Side Effects**: state changes, events emitted, notifications sent, or other context mutations. Discovered during simulation.
- **Preconditions**: what must be true before this contract can succeed. Derived from invariants and state machine guards.

**Contract vs Integration Point**: Integration Points describe context-to-context communication (how bounded contexts talk to each other). External Contracts describe how the outside world talks to THIS context. Both are in the domain spec but serve different purposes.

**Simulation Target**: The SA walks through each External Contract with happy/edge/error scenarios, mentally executing the contract against the spec. The contract's Input/Output fields provide the I/O shape for /tmp/sim/ evidence files. Pain points discovered here drive spec fixes.

## Content

### Contract Definition Template

```
#### <Contract Name: e.g. "Submit Order", "CLI: --version", "GET /orders/{id}">
- **Actor**: <who or what invokes this>
- **Trigger**: <what initiates the interaction>
- **Input**: {<field>: <type>}
- **Output**: {<field>: <type>} on success
- **Errors**:
  - <error condition> -> <error response>
- **Side Effects**: <state changes, events emitted, notifications>
- **Preconditions**: <what must be true>
```

### Contract Naming Convention

Contract names should be descriptive and match the user-facing action:
- CLI commands: `"CLI: <command>"` (e.g. `"CLI: --version"`, `"CLI: submit-order"`)
- HTTP endpoints: `"GET /orders/{id}"`, `"POST /orders"`
- Domain operations: `"<Verb> <Noun>"` (e.g. `"Submit Order"`, `"Cancel Subscription"`)
- Event handlers: `"On <Event>"` (e.g. `"On Payment Received"`, `"On Fill Detected"`)

## Related

- [[requirements/spec-simulation]]: how contracts are walked during simulation
- [[domain-modeling/context-mapping]]: Integration Points (context-to-context communication)
