---
name: review-simulation
description: "Adversarial review of simulation results: find missed scenarios, validate pain points, decide PASS or FAIL"
---

# Review Simulation

Available knowledge: [[requirements/spec-simulation#concepts]], [[architecture/reconciliation#key-takeaways]], [[requirements/gherkin#concepts]]. `in` artifacts: read all before starting work.

1. Read `.cache/sim/simulation_results_*.md` (all iterations, focus on the latest) and `domain_spec.md` (all contexts).
2. Declare adversarial stance per [[architecture/reconciliation#concepts]]: "I will actively search for missed scenarios and invalid pain points, not confirm the simulation's completeness."
3. Verify reviewer decision criteria per [[requirements/spec-simulation#content]].
4. **Rule quality check**: For each discovered rule (now in .feature files), verify it is:
    - Specific enough to be testable (not vague like "the system should handle errors").
     - Traceable to a walkthrough that discovered it (via simulation results provenance column).
    - Not contradicted by another rule or by the spec.
    - Written as a Rule block with clear behavioral description, suitable for generating Examples.
5. **Quality attribute coverage**: For each quality attribute in product_definition.md, verify at least one walkthrough stresses it. If not, add a missed walkthrough.
6. **Cross-context consistency**: Verify integration points are consistent: if Context A says it sends payload X to Context B, verify Context B expects payload X. Bilateral mismatches are hard failures.
7. **Decide PASS or FAIL**:
   - **PASS**: zero unresolved pain points, all entities across all contexts covered by walkthroughs, all integration points tested, all quality attributes stressed, cross-context integration points consistent.
   - **FAIL**: any unresolved pain point, any untested entity or integration point, any untested quality attribute, any bilateral integration mismatch.
8. Record the decision in the latest simulation results Summary section. If FAIL, specify which pain points must be addressed in the next fix-spec iteration.
