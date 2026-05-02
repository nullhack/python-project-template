---
name: map-contexts
description: "Map bounded context relationships, integration points, and anti-corruption layers"
---

# Map Contexts

Available knowledge: [[domain-modeling/context-mapping#key-takeaways]]. `in` artifacts: discover and read on demand as needed.

1. For each pair of interacting bounded contexts, select a relationship pattern
   per [[domain-modeling/context-mapping#concepts]].
2. Draw a context map diagram showing all relationships.
3. For each cross-context interaction, define an integration point per
   [[domain-modeling/context-mapping#concepts]].
4. If a downstream context needs isolation from an upstream model, design an
   anti-corruption layer per [[domain-modeling/context-mapping#concepts]].
5. Write results to artifacts listed in the current state's `out` attrs. If findings affect artifacts outside the `out` contract, flag them in output notes for the appropriate step.
6. Advance the flow with necessary evidence, choosing the appropriate next state based on the work completed.
