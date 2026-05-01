---
domain: architecture
tags: [reconciliation, cross-document-consistency, adversarial-review, verification]
last-updated: 2026-04-29
---

# Reconciliation

## Key Takeaways

- Reconciliation is an adversarial cross-document consistency check — the reviewer actively seeks inconsistencies, not confirms consistency (Tetlock, 1985).
- Five cross-document consistency checks verify alignment: system↔glossary, system↔feature, ADRs↔feature, glossary↔feature, product_definition↔scope.
- Every inconsistency is a signal that either the architecture or the requirements need updating — the reviewer does not decide which side changes, only that a mismatch exists.
- Reconciliation gates prevent forward progress until all five checks pass; this is the last chance to catch misalignment before implementation begins.

## Concepts

**Adversarial Reconciliation** — The reviewer's default hypothesis is that inconsistencies exist. Leveraging accountability to an unknown audience (Tetlock, 1985), the reviewer actively searches for mismatches rather than confirming alignment. This adversarial stance produces more rigorous verification than cooperative review because it prevents confirmation bias — the tendency to see what we expect rather than what is actually there.

**Five Cross-Document Consistency Checks** — Each check compares two documents and verifies that their models, terms, and requirements align. A mismatch in any check is a hard blocker: the architecture must be corrected, or the requirements must be revised, before implementation can proceed.

**Reconciliation Gate** — The reconciliation gate sits between architecture review and implementation. It is the last point where misalignment can be caught cheaply. After this gate, code is written against the architecture, and fixing misalignment becomes exponentially more expensive.

## Content

### The Five Checks

| # | Check | Verify | Mismatch Signal |
|---|---|---|---|
| 1 | system ↔ glossary | Every glossary term matches how it is used in system.md Domain Model | A term defined in the glossary is used with a different meaning in the domain model |
| 2 | system ↔ feature | Every entity, action, and relationship in system.md Domain Model matches feature requirements | An entity appears in the domain model but not in any feature, or vice versa |
| 3 | ADRs ↔ feature | Every ADR aligns with feature requirements; each ADR references specific `@id` criteria | An ADR contradicts a feature requirement, or a feature requirement has no ADR addressing it |
| 4 | glossary ↔ feature | Every domain term in the feature file matches its glossary definition | A term used in the feature has no glossary entry, or the glossary definition contradicts the feature's usage |
| 5 | product_definition ↔ scope | Scope in the product definition stays within the stated boundaries (what_is, what_is_not, out_of_scope) | A feature requirement exceeds the product definition's stated scope |

### Mismatch Resolution

When a mismatch is found:

1. **Record the mismatch**: Which two documents, which specific items, and how they disagree.
2. **Determine which side changes**: If the architecture is wrong, update system.md, technical_design.md, or the ADR. If the requirements are wrong, update the feature file or product definition.
3. **Update both documents**: Ensure the correction is reflected in all affected documents.
4. **Re-run the affected check**: Verify the mismatch is resolved.

### Reviewer Stance Declaration

Before performing reconciliation, the reviewer declares:

- Adversarial stance: "I will actively search for inconsistencies, not confirm consistency."
- Boundary check: "I will verify every cross-document relationship, not just the ones that seem obvious."
- Semantic read: "I will read for meaning, not just surface-level keyword matching."

## Related

- [[architecture/adr]]
- [[architecture/assessment]]
- [[requirements/pre-mortem]]