---
name: simulate-spec
description: "Walk through all domain spec contexts mentally, create I/O evidence in /tmp, discover rules and pain points"
---

# Simulate Spec

Available knowledge: [[requirements/spec-simulation]], [[requirements/gherkin#key-takeaways]]. `in` artifacts: read all before starting work. `out` artifacts: `features/*.feature` (one per bounded context, created from template with Feature title and Rule blocks), `simulation_results.md`.

1. Read `domain_spec.md` (all bounded contexts). Read `product_definition.md` for quality attributes that must be tested. Read `glossary.md` for term definitions.
2. If `simulation_results.md` exists from a prior iteration, read it for previously discovered rules and unresolved pain points — this iteration must walk walkthroughs that address those pain points.
3. For each bounded context (`## <Context Name>` section) in domain_spec.md, identify simulation walkthroughs per [[requirements/spec-simulation#concepts]]:
   - **Happy paths**: primary use cases from interview data, one per user persona.
   - **Edge cases**: boundary conditions (empty inputs, maximum values, concurrent operations, out-of-order events).
   - **Error paths**: invalid inputs, precondition failures, integration point failures, timeout scenarios.
   - **Quality attribute tests**: walkthroughs that stress each quality attribute from product_definition.md.
4. For each walkthrough, mentally walk through the system as described in the domain spec:
   - What inputs arrive? What state is the system in?
   - What should happen according to the spec?
   - What is the resulting state and output?
   - Does the spec cover this walkthrough? If not, that is a pain point.
5. Create I/O evidence in `/tmp/sim/<context>/` per [[requirements/spec-simulation#concepts]]: `walkthrough_<N>_in.json` and `walkthrough_<N>_out.json` pairs. These files prove the simulation was walked and provide concrete examples for later test writing.
6. Classify and record pain points per [[requirements/spec-simulation#concepts]]:
   - **Ambiguous**: spec can be read multiple ways.
   - **Contradictory**: spec says two things that conflict.
    - **Missing**: walkthrough not covered by spec at all.
   - **Edge-case**: spec covers the happy path but not this boundary condition.
7. Write each discovered rule as a Rule block in the appropriate .feature file. Use the template at `.templates/docs/features/<feature_name>.feature.template` to create the file for each bounded context. The Rule block format: `Rule: <2-6 word title>` followed by a behavioral description paragraph. Each rule must cite the walkthrough that discovered it.
7a. Verify all titles meet constraints per [[requirements/gherkin#key-takeaways]]: every Feature title is 2–6 words and unique across all .feature files; every Rule title is 2–6 words and unique within its .feature file. Count words by splitting on whitespace. If a title fails, rephrase and re-check.
8. For each bounded context, read the `### Technology Requirements` table in domain_spec.md. Write each technology requirement as a `# Constraints:` entry in the context's .feature file. Use the Verification column's instruction as the constraint text. Technology constraints carry implementation mandates forward from the domain spec to the artifacts the SE reads.
9. Record walkthrough→rule provenance in `simulation_results.md`: each walkthrough's `Discovered Rule` column references the Rule title written to the .feature file.
10. **E2E completeness walk**: string all discovered rules together into an end-to-end user journey per bounded context. Read rules from the .feature files, not simulation_results.md. For each context, verify:
   - The rules cover a complete happy-path flow from input to observable output. No "imagined" steps — every transition between rules has a defined trigger and output in the domain spec.
   - External Contract rules have enough detail to generate real fixtures: response shape, status codes, error shapes, field types.
   - The composed rules would produce a working application if implemented exactly as described. If any step in the E2E flow is undefined, record it as a pain point (type: `missing-e2e`).
   - Cross-context flows are complete: where one context's output feeds another context's input, both sides are specified with matching data shapes.
11. Write `simulation_results.md` from the template at `.templates/docs/spec/simulation_results.md.template`. One file covering all contexts. Record pain points and walkthrough→rule provenance only — discovered rules live in .feature files. Template sections: Walkthroughs Performed (with Discovered Rule column referencing .feature Rule titles), Pain Points, Resolution Status, Summary.
