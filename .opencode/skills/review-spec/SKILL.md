---
name: review-spec
description: "Independently verify the feature spec for cross-document consistency, domain alignment, BDD quality, and pre-mortem coverage"
---

# Review Spec

Available knowledge: [[architecture/reconciliation]], [[requirements/gherkin#concepts]], [[requirements/pre-mortem#concepts]]. `in` artifacts: read all before starting work.

1. Declare adversarial stance per [[architecture/reconciliation#concepts]]: actively search for inconsistencies, not confirm alignment.
2. Run the four applicable cross-document consistency checks per [[architecture/reconciliation]] (skip ADR check — ADRs are not in the `in` list for this review):
   - domain_model ↔ glossary
   - domain_model ↔ feature
   - glossary ↔ feature
   - product_definition ↔ scope
3. Verify BDD quality per [[requirements/gherkin#concepts]]: every Example is declarative, each `Then` has a single observable outcome, no two Examples duplicate the same `Then` outcome.
4. Verify pre-mortem coverage per [[requirements/pre-mortem#concepts]]: each Rule has undergone specification pre-mortem; each distinct `Then` outcome has undergone behavior pre-mortem with Examples added for surfaced failure modes.
5. If any inconsistency or quality gap is found, flag with file:line references (e.g., "domain_model.md:23 conflicts with <feature>.feature:15"). Vague findings create rework.
