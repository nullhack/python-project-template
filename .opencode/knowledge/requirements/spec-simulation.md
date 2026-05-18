---
domain: requirements
tags: [spec-simulation, behavioral-validation, pain-points, rules-discovery]
last-updated: 2026-05-14
---

# Spec Simulation

## Key Takeaways

- Spec simulation walks through domain spec walkthroughs mentally before any code is written, discovering rules, pain points, and E2E test candidates. The domain spec is monolithic: one file containing all bounded contexts as `## <Context Name>` sections.
- Simulation iterates over all bounded contexts in the single domain_spec.md file. I/O evidence is per-context in .cache/sim/<context>/. These files are NOT committed — they are ephemeral evidence of the simulation process.
- Pain points are classified as: ambiguous (multiple readings), contradictory (conflicting specs), missing (not covered at all), or edge-case (happy path covered but not this boundary).
- Discovered rules are surfaced as plain-language behavioral statements — no numbered prefixes. Each discovered rule traces to the walkthrough that produced it.
- The simulation loop (simulate → review → fix → re-simulate) caps at 5 iterations. If unresolved pain points remain, the flow escalates to needs-reinterview.

## Concepts

**Walkthrough Types**: Three categories ensure comprehensive coverage across all bounded contexts in the monolithic domain_spec.md:
- **Happy paths**: primary use cases from interview data, one per user persona. These prove the spec works for the common case.
- **Edge cases**: boundary conditions — empty inputs, maximum values, concurrent operations, out-of-order events. These prove the spec handles realistic variation.
- **Error paths**: invalid inputs, precondition failures, integration point failures, timeout scenarios. These prove the spec handles failure gracefully.

**Pain Point Classification**: Each pain point gets a classification that determines how fix-spec addresses it:
- **Ambiguous**: the spec text can be read multiple ways. Fix: clarify to a single reading.
- **Contradictory**: two spec sections say different things. Fix: resolve the contradiction, documenting why one interpretation was chosen.
- **Missing**: the walkthrough is not covered by the spec at all. Fix: add the missing content (new entity fields, integration contracts, error paths).
- **Edge-case**: the spec covers the happy path but not this boundary condition. Fix: add explicit handling (constraints, guards) or state out-of-scope.

**I/O Evidence**: Each simulated walkthrough produces a pair of JSON files in .cache/sim/<context>/:
- `walkthrough_<N>_in.json`: the input state and stimulus.
- `walkthrough_<N>_out.json`: the expected output state and response.
These files provide concrete examples for later test writing and prove the simulation was thorough.

**Iteration Cap**: The simulation loop caps at 5 iterations to prevent infinite refinement. If pain points remain after 5 iterations, the flow escalates to needs-reinterview — the stakeholder must clarify before simulation can continue.

## Content

### Simulation Walkthrough Procedure

For each walkthrough, the SA mentally executes:

1. **Setup**: What is the initial state? Which entities exist? What are their field values?
2. **Stimulus**: What input arrives? From which External Contract? What are the exact field values?
3. **Processing**: What should the system do according to the spec? Walk through each entity, state machine, and rule that applies.
4. **Output**: What is the resulting state? What output is produced? What side effects occur?
5. **Verification**: Does the spec cover this walkthrough completely? If any step has a ?, a conflict, or a gap → record as a pain point.

### Reviewer Decision Criteria

The reviewer decides PASS or FAIL based on:

1. **Zero unresolved pain points**: Every pain point across all contexts from simulation must be resolved in the spec.
2. **Entity coverage**: Every entity across all contexts has at least one happy path, one edge case, one error path.
3. **Integration point coverage**: Every integration point (including bilateral cross-context pairs) has at least one success and one failure walkthrough.
4. **Quality attribute coverage**: Every quality attribute from product_definition.md has at least one walkthrough stressing it.
5. **Rule quality**: Every discovered rule is specific, testable, traceable, and non-contradictory.
6. **Cross-context consistency**: Bilateral integration points between contexts are consistent (Context A's payload matches Context B's expectation).

## Related

- [[domain-modeling/behavioral-contracts]]: the External Contracts that simulation targets
- [[requirements/pre-mortem]]: adversarial analysis technique used during simulation
