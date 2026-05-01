---
domain: architecture
tags: [adr, architecture-decision-records, decision-making]
last-updated: 2026-04-29
---

# Architecture Decision Records

## Key Takeaways

- ADRs document architecturally significant decisions — decisions that are hard to change and affect multiple components (Nygard, 2011).
- Each ADR follows a fixed structure: Status, Context, Decision, Reason, Alternatives, Consequences (Nygard, 2011).
- ADRs are append-only — once written, they are never edited. Superseded ADRs get a new "Superseded by" reference, not a revision.
- ADRs must be consistent with feature requirements — every ADR should reference the `@id` criteria it addresses.
- ADR risk assessment uses Probability × Impact classification (Boehm, 1991) to prioritise mitigation effort on the highest-exposure risks.

## Concepts

**Architecturally Significant** — A decision is architecturally significant if it affects multiple components, is hard to reverse, or constrains future choices (Nygard, 2011; Fowler, 2003). Choosing a database is architecturally significant. Choosing a variable name is not. When in doubt, write the ADR.

**ADR Structure** — Every ADR contains (Nygard, 2011): Status (Proposed, Accepted, Deprecated, Superseded), Context (the forces at play, the problem being solved), Decision (the choice made), Reason (why this choice over alternatives), Alternatives (other options considered and why they were rejected), Consequences (what changes because of this decision, both positive and negative).

**Append-Only Discipline** — ADRs capture the decision as it was made at the time. If understanding changes, write a new ADR that supersedes the old one. This preserves the history of architectural reasoning and prevents retroactive justification.

**ADR Consistency** — Every ADR must be consistent with the feature requirements it addresses. During review, check that each ADR aligns with the `@id` criteria in the feature file. An ADR that contradicts a requirement is a signal that either the ADR or the requirement needs updating. Architecture review is adversarial — the reviewer actively seeks inconsistencies and gaps, leveraging accountability to an unknown audience (Tetlock, 1985) to produce more rigorous decisions.

**Risk Assessment** (Boehm, 1991) — Each ADR's Risk Assessment table uses Probability × Impact to classify and prioritise risks. Probability (Low/Medium/High) estimates how likely the risk is to materialise. Impact (Low/Medium/High) estimates how severe the consequence would be. Risks with High Probability and High Impact demand explicit mitigations or rejection of the decision. Risks with Low Probability and Low Impact may be accepted without mitigation. Risk leverage — the ratio of risk reduction to mitigation cost — helps prioritise which mitigations to invest in first.

## Content

### ADR Template Fields

| Field | Content |
|---|---|
| Status | Proposed, Accepted, Deprecated, or Superseded |
| Context | What is the issue that we're seeing that is motivating this decision? |
| Decision | What is the change that we're proposing/making? |
| Reason | Why is this the best choice given the alternatives? |
| Alternatives | What other choices were considered and why were they rejected? |
| Consequences | What becomes easier or harder to do because of this change? |

### When to Write an ADR

- Choosing a framework, library, or database
- Choosing an architectural style (monolith, microservices, event-driven)
- Choosing a communication pattern (sync HTTP, async events, gRPC)
- Choosing a data storage strategy (SQL, NoSQL, event sourcing)
- Choosing a deployment strategy (container, serverless, bare metal)
- Introducing a new bounded context boundary
- Changing a cross-cutting concern (authentication, logging, error handling)

### Risk Assessment Classification

| Probability \ Impact | Low | Medium | High |
|---|---|---|---|
| **High** | Monitor | Mitigate | Mitigate or Reject |
| **Medium** | Accept | Monitor | Mitigate |
| **Low** | Accept | Accept | Monitor |

- **Mitigate**: Explicit mitigation strategy required before accepting the ADR
- **Monitor**: Flag for future review; no immediate action needed
- **Accept**: Risk is acceptable; document in ADR
- **Reject**: Risk is too high; reconsider the decision or choose an alternative

Risk leverage prioritises mitigations with the highest ratio of risk reduction to mitigation cost (Boehm, 1991).

### When NOT to Write an ADR

- Choosing a variable name
- Choosing a code style (use project conventions)
- Choosing a test framework (use project conventions)
- Any decision that is easily reversible and affects only one component

## Related

- [[architecture/assessment]]
- [[architecture/technical-design]]
- [[architecture/reconciliation]]
- [[architecture/quality-attributes]]