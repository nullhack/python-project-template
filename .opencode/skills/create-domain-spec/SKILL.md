---
name: create-domain-spec
description: "SA and DE collaborate to create a monolithic domain specification from interview notes"
---

# Create Domain Spec

Available knowledge: [[domain-modeling/event-storming#concepts]], [[domain-modeling/context-mapping#key-takeaways]], [[requirements/ubiquitous-language#key-takeaways]]. `in` artifacts: read all before starting work.

1. Read all interview notes from `in` artifacts.
2. Identify bounded contexts from interview data: scan for clusters of related terminology, distinct lifecycles, and independent business capabilities per [[domain-modeling/event-storming#concepts]]. Record each context with a name, responsibility, and rough boundary.
3. Write `product_definition.md` from the trimmed template: What IS/IS NOT, Why, Users, Quality Attributes, Out of Scope. Use the interview data to fill every section.
4. Write `domain_spec.md` from the template at `.templates/docs/spec/domain_spec.md.template`. This is a single monolithic file — one `## <Context Name>` section per bounded context. Fill in iteration-0 content for each context:
   - **Context Map**: leave the top-level section empty — architecture-flow context-mapping state refines it.
   - **Context**: 2-3 sentences about what this context does and why it exists.
   - **Entities**: name, type (Entity/Value Object), purpose, aggregate root designation.
   - **Relationships**: entity relationships with cardinality.
    - **Aggregate Boundaries**: grouping rationale, root entity, and See cross-reference to the Invariants section (not invariant text — invariants are derived during simulation).
   - **Data Shapes**: field names and types from interview data. Constraints may be `?` if unknown.
   - **Integration Points**: direction, trigger, rough payload shape. Details may be `?`.
   - **External Contracts**: actor, trigger, input shape, output shape, known error conditions, side effects, and preconditions. Details may have `?` for unknowns.
   - Leave **State Machines**, **Error Handling**, and **Invariants** empty — simulation discovers these.
5. Write `glossary.md` from the template at `.templates/docs/spec/glossary.md.template`. Extract domain terms from interview notes per [[requirements/ubiquitous-language#key-takeaways]]. Define each in genus-differentia format. Cross-reference against domain spec.
6. Verify: every bounded context has a `## <Context Name>` section in domain_spec.md. Every quality attribute is noted for simulation targeting. Every external contract has at least one input/output pair defined.
