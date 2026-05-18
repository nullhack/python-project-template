---
name: fix-spec
description: "Rewrite domain spec addressing all pain points from simulation, full rewrite for coherence"
---

# Fix Spec

Available knowledge: [[requirements/spec-simulation#concepts]], [[requirements/gherkin#concepts]]. `in` artifacts: read all before starting work.

1. Read `.cache/sim/simulation_results_*.md` (all iterations, focus on the latest) and `domain_spec.md` (all contexts). Prior iterations provide cumulative context for previously discovered pain points.
2. List all unresolved pain points from the latest simulation results across all contexts. These are the fix targets.
3. Rewrite `domain_spec.md` addressing every pain point per its classification in [[requirements/spec-simulation#concepts]].
4. Fill in any `?` constraints in Data Shapes that were resolved by this iteration.
5. Update **State Machines** section within each context (derived summaries referencing .feature rules): state transitions emerge from accumulated rules. If rules imply a lifecycle, formalize it as a state machine table.
6. Update **Error Handling** section within each context (derived summaries referencing .feature rules): error paths discovered during simulation get explicit entries.
7. Update **Invariants** section within each context (derived summaries referencing .feature rules): any "must always" conditions discovered get added.
8. Update the latest `.cache/sim/simulation_results_<timestamp>.md` Resolution Status table: mark each pain point as Resolved with a brief description of how. This is the authoritative pain-point tracker — domain_spec does not duplicate them.
9. Update .feature files: correct Rule blocks that were based on resolved pain points. If a Rule description was ambiguous (pain point classified as ambiguous), rewrite it for clarity. If a Rule title was changed during correction, verify the new title is 2–6 words and unique within the feature file per [[requirements/gherkin#key-takeaways]]. Count words by splitting on whitespace.
10. This is a FULL REWRITE of domain_spec.md, not a patch. Read the entire existing spec (all contexts), then write the updated version from top to bottom. This ensures coherence — no context contradicts another because the whole document was written in one pass with full context.
