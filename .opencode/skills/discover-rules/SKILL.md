---
name: discover-rules
description: "Map structural rules from domain spec aggregate invariants and quality attribute constraints into feature files"
---

# Discover Rules

Available knowledge: [[requirements/feature-discovery#concepts]], [[requirements/gherkin#concepts]]. `in` artifacts: read all before starting work.

1. Read product_definition.md, domain_spec.md, and all `.feature` files (created by simulation) from `in` artifacts.
2. For each aggregate invariant in domain_spec.md, verify the corresponding feature already has a Rule block covering it (written by simulation). Use [[requirements/gherkin#concepts]] for Rule block structure.
3. If an invariant has no corresponding Rule, add it as a Rule block with a behavioral description derived from the invariant. Format: `Rule: <2-6 word title>` followed by a behavioral description paragraph.
4. Run gap analysis: every aggregate invariant → at least one Rule; every quality attribute → at least one Constraint (constraints are written by discover-features). IF any gap → flag it. Do NOT silently fill gaps with assumed rules.
