---
name: map-contexts
description: "Map bounded context relationships, Vernon patterns, and anti-corruption layers into behavioral_spec.md integration points"
---

# Map Contexts

Available knowledge: [[domain-modeling/context-mapping#key-takeaways]]. `in` artifacts: read all before starting work.

1. For each pair of interacting bounded contexts, select a relationship pattern per [[domain-modeling/context-mapping#concepts]].
2. Draw a context map diagram showing all relationships.
3. If a downstream context needs isolation from an upstream model, design an anti-corruption layer per [[domain-modeling/context-mapping#concepts]].
4. Write the context map section into domain_model.md (relationships table, diagram, ACL table).
5. Update the Integration Points section in behavioral_spec.md with the context-to-context communication details (purpose, trigger, payload, response).
