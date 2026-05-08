---
name: discover-rules
description: "Derive business rules and constraints from domain model artifacts (events, invariants, commands) and map them to feature files"
---

# Discover Rules

Available knowledge: [[requirements/rule-derivation]], [[requirements/feature-discovery#concepts]]. `in` artifacts: read all before starting work.

1. Read product_definition.md, domain_model.md, glossary.md, and all `.feature` files (created by discover-features in this same state) from `in` artifacts.
2. Assign domain model artifacts to features per [[requirements/rule-derivation#content]]: using the bounded context column in the domain model's entity table, assign each entity, event, and command to the feature corresponding to its context.
3. For each feature, derive behavioral rules from domain events per [[requirements/rule-derivation#key-takeaways]]: "When [event], then [consequence]." Write each as a coarse bullet under `Rules (Business)`.
4. For each feature, derive structural rules from aggregate invariants per [[requirements/rule-derivation#key-takeaways]]: "[Entity] must always [condition]." Write each as a coarse bullet under `Rules (Business)`.
5. For each feature, derive action rules from commands per [[requirements/rule-derivation#key-takeaways]]: "[Actor] can [action] when [precondition]." Write each as a coarse bullet under `Rules (Business)`.
6. For each quality attribute in product_definition.md, map it to the feature(s) that enforce it per [[requirements/rule-derivation#key-takeaways]]. Write each as a Constraint with a measurable threshold.
7. Run traceability verification per [[requirements/rule-derivation#content]]: every event → at least one rule, every invariant → at least one rule, every command → at least one rule, every quality attribute → at least one constraint. IF any gap → flag it in the feature's Questions table. Do NOT silently fill gaps with assumed rules.
8. Write all Rules (Business) bullets and Constraints into each `.feature` file. Do NOT write full `Rule:` blocks (As a/I want/So that) or `Example:` blocks — those require the adversarial analysis of breakdown.