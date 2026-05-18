---
name: review-architecture
description: "Adversarial architecture review: verify alignment with domain spec, ADR compliance, quality attributes, and cross-document consistency"
---

# Review Architecture

Available knowledge: [[software-craft/code-review#key-takeaways]], [[architecture/reconciliation#concepts]]. `in` artifacts: read all before starting work.

**Adversarial stance**: Actively seek inconsistencies and gaps. Use accountability to an unknown audience (Tetlock, 1985) to produce more rigorous decisions.

1. Read all `in` artifacts: ADRs (if any), product_definition.md, domain_spec.md, glossary.md.
2. Verify cross-document consistency per [[architecture/reconciliation#concepts]]:
   - ADR ↔ domain_spec: every ADR aligns with spec requirements; each ADR references specific Example criteria.
   - domain_spec ↔ product_definition: every bounded context in the spec maps to a quality attribute or delivery step.
   - domain_spec ↔ glossary: every term in the spec is defined in the glossary with consistent meaning.
   - ADR ↔ product_definition: technology choices in ADRs match the technology stack in product_definition.
3. Verify quality attribute coverage: for each quality attribute in product_definition.md, check that the domain spec and ADRs address it with measurable thresholds.
4. Verify integration point consistency: for each bilateral integration between contexts in the domain spec, verify payload shapes match on both sides.
5. Verify ADR completeness per [[architecture/adr#concepts]]: each ADR has context, decision, consequences. No orphan ADRs without a corresponding requirement.
6. IF all checks pass → set evidence `alignment: ==domain-spec-verified` and `adr-compliance: ==adrs-respected`.
7. IF any inconsistencies found → exit `inconsistent` with specific citations (file:line). Do NOT fix issues — flag them.
