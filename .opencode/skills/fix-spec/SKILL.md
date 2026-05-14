---
name: fix-spec
description: "Rewrite behavioral spec addressing all pain points from simulation, full rewrite for coherence"
---

# Fix Spec

Available knowledge: [[requirements/spec-simulation#concepts]]. `in` artifacts: read all before starting work.

1. Read `simulation_results.md` (current iteration) and `behavioral_spec.md` (all contexts). If prior simulation_results exist, read those too for cumulative context.
2. List all unresolved pain points from simulation_results.md across all contexts. These are the fix targets.
3. Rewrite `behavioral_spec.md` addressing every pain point:
   - **Ambiguous** pain points: clarify the spec text so it can only be read one way.
   - **Contradictory** pain points: resolve the contradiction, choosing one interpretation and documenting why.
   - **Missing** pain points: add the missing content (new entity fields, new integration contracts, new error paths).
   - **Edge-case** pain points: add explicit handling (constraints, guards, or stated out-of-scope).
4. Fill in any `?` constraints in Data Shapes that were resolved by this iteration.
5. Update **State Machines** section within each context: state transitions emerge from accumulated rules. If rules imply a lifecycle, formalize it as a state machine table.
6. Update **Error Handling** section within each context: error paths discovered during simulation get explicit entries.
7. Update **Invariants** section within each context: any "must always" conditions discovered get added.
8. Update `simulation_results.md` Resolution Status table: mark each pain point as Resolved with a brief description of how. This is the authoritative pain-point tracker — behavioral_spec does not duplicate them.
9. This is a FULL REWRITE of behavioral_spec.md, not a patch. Read the entire existing spec (all contexts), then write the updated version from top to bottom. This ensures coherence — no context contradicts another because the whole document was written in one pass with full context.
