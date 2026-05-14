---
name: simulate-spec
description: "Walk through all domain spec contexts mentally, create I/O evidence in /tmp, discover rules and pain points"
---

# Simulate Spec

Available knowledge: [[requirements/spec-simulation]]. `in` artifacts: read all before starting work.

1. Read `domain_spec.md` (all bounded contexts). Read `product_definition.md` for quality attributes that must be tested. Read `glossary.md` for term definitions.
2. If `simulation_results.md` exists from a prior iteration, read it for previously discovered rules and unresolved pain points — this iteration must walk scenarios that address those pain points.
3. For each bounded context (`## <Context Name>` section) in domain_spec.md, identify simulation scenarios per [[requirements/spec-simulation#concepts]]:
   - **Happy paths**: primary use cases from interview data, one per user persona.
   - **Edge cases**: boundary conditions (empty inputs, maximum values, concurrent operations, out-of-order events).
   - **Error paths**: invalid inputs, precondition failures, integration point failures, timeout scenarios.
   - **Quality attribute tests**: scenarios that stress each quality attribute from product_definition.md.
4. For each scenario, mentally walk through the system as described in the domain spec:
   - What inputs arrive? What state is the system in?
   - What should happen according to the spec?
   - What is the resulting state and output?
   - Does the spec cover this scenario? If not, that is a pain point.
5. Create I/O evidence in `/tmp/sim/<context>/` per [[requirements/spec-simulation#concepts]]: one `_in.json` and `_out.json` pair per scenario. These files prove the simulation was walked and provide concrete examples for later test writing.
6. Classify and record pain points per [[requirements/spec-simulation#concepts]]:
   - **Ambiguous**: spec can be read multiple ways.
   - **Contradictory**: spec says two things that conflict.
   - **Missing**: scenario not covered by spec at all.
   - **Edge-case**: spec covers the happy path but not this boundary condition.
7. Record discovered rules as descriptive statements in plain language. Each rule must cite the scenario that discovered it. Rules map directly to Example titles in .feature files later — write them as clear, unique descriptions without special characters.
8. Identify E2E test candidates: scenarios that should become acceptance tests after validation. Each candidate gets a descriptive title suitable for use as an Example: title.
9. **E2E completeness walk**: string all discovered rules together into an end-to-end user journey per bounded context. For each context, verify:
   - The rules cover a complete happy-path flow from input to observable output. No "imagined" steps — every transition between rules has a defined trigger and output in the domain spec.
   - External Contract rules have enough detail to generate real fixtures: response shape, status codes, error shapes, field types.
   - The composed rules would produce a working application if implemented exactly as described. If any step in the E2E flow is undefined, record it as a pain point (type: `missing-e2e`).
   - Cross-context flows are complete: where one context's output feeds another context's input, both sides are specified with matching data shapes.
10. Write `simulation_results.md` from the template at `.templates/docs/spec/simulation_results.md.template` with all findings. One file covering all contexts, with a `## <Context Name>` section per bounded context.
