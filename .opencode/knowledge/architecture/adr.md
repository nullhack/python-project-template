---
domain: architecture
tags: [adr, decision-record, interview, stakeholder-validation]
last-updated: 2026-04-26
---

# Architecture Decision Records (ADR)

## Key Takeaways

- Only create ADRs for non-obvious decisions with meaningful trade-offs; routine YAGNI choices don't need records.
- Frame each decision as a clear question with known alternatives; evaluate consequences and draft ADRs before stakeholder validation.
- ADRs follow a specific document format: Context, Interview, Decision, Reason, Alternatives Considered, and Consequences.
- ADRs are append-only and require stakeholder validation: never edit a committed ADR; if a decision changes, write a new ADR that supersedes the old one; commit only after stakeholder approval.

## Concepts

**Only non-obvious decisions need ADRs**: Create ADRs only for decisions with meaningful trade-offs. Routine choices following YAGNI do not need records. ADRs require stakeholder validation before commit.

**ADR Interview Pattern**: For each group of related unresolved decisions identified during domain analysis: frame the questions, state constraints from the feature file and existing ADRs, evaluate alternatives with consequences, draft the ADRs, then present a validation table to the stakeholder.

**ADR Document Format**: File `docs/adr/ADR-YYYY-MM-DD-<slug>.md` with sections: Context (the situation that triggered these questions), Interview (Q&A table with final accepted answers), Decision (one sentence), Reason (one sentence), Alternatives Considered (rejected options with reasons), and Consequences (+/- outcomes).

**ADR Rules**: ADRs are append-only — never edit a committed ADR. If a decision changes, write a new ADR that supersedes the old one. ADRs require stakeholder validation before commit; do not commit ADRs that have not been validated.

## Content

### ADR Interview Pattern

For each group of related unresolved decisions identified during domain analysis:

1. **Frame the questions**: state each decision as a clear question with known alternatives.
   Example: "Should `FrameworkAdapter` be a `typing.Protocol` or an ABC?"

2. **State constraints**: list what is known from the feature file, glossary, and existing ADRs that constrains the answer.

3. **Evaluate alternatives**: for each option, state the consequence. Apply laddering to surface hidden consequences.

4. **Draft the ADR**: group related questions into one ADR using the document format below. Do not commit yet — ADRs require stakeholder validation first.

5. **Stakeholder validation**: after all ADRs are drafted, present a validation table to the stakeholder:

   | ADR | Summary | Decision | Reason | Alternatives |
   |---|---|---|---|---|
   | ADR-YYYY-MM-DD-<slug> | <one-line summary> | <chosen option> | <one-line reason> | <option names only> |

6. **If stakeholder approves**: commit each approved ADR. `feat(<feature-stem>): add ADR-<slug>`

7. **If stakeholder rejects an ADR**: expand that ADR with deeper considerations and consequences, then present the specific ADR as a targeted question with options. Iterate until the stakeholder approves, then commit.

Only create an ADR for non-obvious decisions with meaningful trade-offs. Routine YAGNI choices do not need a record.

### ADR Document Format

File: `docs/adr/ADR-YYYY-MM-DD-<slug>.md`

Sections:

- **Context** — the situation that triggered these questions
- **Interview** — Q&A table with final accepted answers (one row per question)
- **Decision** — one sentence
- **Reason** — one sentence
- **Alternatives Considered** — rejected options with reasons
- **Consequences** — (+) and (-) outcomes

### Rules

- ADRs are append-only: never edit a committed ADR. If a decision changes, write a new ADR that supersedes the old one.
- ADRs require stakeholder validation before commit. Do not commit ADRs that have not been validated.
- Only non-obvious decisions with trade-offs need ADRs. Routine choices (e.g., "use dataclass for a value object") do not.

## Related

- [[architecture/smell-check]] — the gate that ADRs must satisfy
- [[architecture/domain-stubs]] — stubs that implement ADR decisions
- [[requirements/discovery-techniques]] — laddering technique used during ADR interviews