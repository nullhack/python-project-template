---
name: review-simulation
description: "Adversarial review of simulation results: find missed scenarios, validate pain points, decide PASS or FAIL"
---

# Review Simulation

Available knowledge: [[requirements/spec-simulation#concepts]], [[architecture/reconciliation#key-takeaways]]. `in` artifacts: read all before starting work.

1. Read `simulation_results.md` and `domain_spec.md` (all contexts).
2. Declare adversarial stance per [[architecture/reconciliation#concepts]]: "I will actively search for missed scenarios and invalid pain points, not confirm the simulation's completeness."
3. **Scenario coverage check**: For each context in domain_spec.md, for each entity, verify at least one happy path, one edge case, and one error path was simulated. For each integration point, verify at least one success and one failure scenario. For cross-context integration points, verify both sides of the bilateral relationship were tested. Flag any gaps.
4. **Pain point validation**: For each pain point in simulation_results.md, verify it is real and correctly classified. A pain point is invalid if the spec actually covers the scenario (reviewer misread) or if the scenario is out of scope per product_definition.md. Remove invalid pain points. Add any missed pain points.
5. **Rule quality check**: For each discovered rule, verify it is:
   - Specific enough to be testable (not vague like "the system should handle errors").
   - Traceable to a scenario that discovered it.
   - Not contradicted by another rule or by the spec.
   - Written as a clear, unique descriptive statement suitable for mapping to an Example title.
6. **Quality attribute coverage**: For each quality attribute in product_definition.md, verify at least one scenario stresses it. If not, add a missed scenario.
7. **Cross-context consistency**: Verify integration points are consistent: if Context A says it sends payload X to Context B, verify Context B expects payload X. Bilateral mismatches are hard failures.
8. **Decide PASS or FAIL**:
   - **PASS**: zero unresolved pain points, all entities across all contexts covered by scenarios, all integration points tested, all quality attributes stressed, cross-context integration points consistent.
   - **FAIL**: any unresolved pain point, any untested entity or integration point, any untested quality attribute, any bilateral integration mismatch.
9. Record the decision in simulation_results.md Summary section. If FAIL, specify which pain points must be addressed in the next fix-spec iteration.
