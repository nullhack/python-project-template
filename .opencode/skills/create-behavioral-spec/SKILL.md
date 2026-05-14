---
name: create-behavioral-spec
description: "SA and DE collaborate to create a monolithic behavioral specification from interview notes"
---

# Create Behavioral Spec

Available knowledge: [[domain-modeling/behavioral-contracts#concepts]], [[domain-modeling/context-mapping#key-takeaways]], [[requirements/ubiquitous-language#key-takeaways]]. `in` artifacts: read all before starting work.

1. Read all interview notes from `in` artifacts.
2. Identify bounded contexts from interview data: scan for clusters of related terminology, distinct lifecycles, and independent business capabilities per [[domain-modeling/behavioral-contracts#concepts]]. Record each context with a name, responsibility, and rough boundary.
3. Write `product_definition.md` from the trimmed template: What IS/IS NOT, Why, Users, Quality Attributes, Out of Scope, Delivery Order. Use the interview data to fill every section. The delivery order drives which context gets specified and simulated first.
4. Write `domain_model.md` from the template at `.templates/docs/spec/domain_model.md.template`. Fill in structural domain information:
   - **Summary**: domain overview.
   - **Bounded Contexts**: contexts identified in step 2.
   - **Entities**: entity names, types, descriptions, context membership, aggregate root designation.
   - **Relationships**: entity relationships with cardinality.
   - **Aggregate Boundaries**: grouping rationale and invariants.
   - Context Map is left for the architecture-flow context-mapping state to refine.
5. Write `behavioral_spec.md` from the template at `.templates/docs/spec/behavioral_spec.md.template`. This is a single monolithic file — one `## <Context Name>` section per bounded context. Fill in iteration-0 content for each context:
   - **Context**: 2-3 sentences about what this context does and why it exists.
   - **Entities**: name, purpose, rough lifecycle description. Do NOT define state machines yet.
   - **Data Shapes**: field names and types from interview data. Constraints may be `?` if unknown.
   - **Integration Points**: direction, trigger, rough payload shape. Details may be `?`.
   - Leave **State Machines**, **Error Handling**, **Invariants**, **Rules Discovered**, and **Pain Points** empty — simulation discovers these.
6. For each bounded context, identify external contracts: how users and external systems interact with this context. Write each as an `#### <Contract Name>` entry within the context's **External Contracts** section with actor, trigger, input shape, output shape, known error conditions, side effects, and preconditions. These are the primary simulation targets. Details may have `?` for unknowns.
7. Write `glossary.md` from the template at `.templates/docs/spec/glossary.md.template`. Extract domain terms from interview notes per [[requirements/ubiquitous-language#key-takeaways]]. Define each in genus-differentia format. Cross-reference against behavioral specs.
8. Verify: every bounded context has a `## <Context Name>` section in behavioral_spec.md. Every delivery order entry maps to at least one context. Every quality attribute is noted for simulation targeting. Every external contract has at least one input/output pair defined.
