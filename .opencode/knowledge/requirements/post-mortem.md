---
domain: requirements
tags: [post-mortem, root-cause-analysis, blameless, failure-analysis]
last-updated: 2026-04-29
---

# Post-Mortem

## Key Takeaways

- Post-mortems are process-level root cause analysis, not person-level blame — every failure is a process failure, not a people failure (Beyer et al., 2016).
- Keep post-mortems compact (max 15 lines) — focus on what failed, which gate was missed, and the fix.
- Post-mortems are append-only — never edit an existing post-mortem; if understanding evolves, write a new one.
- The restart check answers: "Can we safely re-enter the pipeline from the identified point, or is there a deeper issue?"

## Concepts

**Process Root Cause, Not People** — Post-mortems identify which process gate failed, not who made the mistake. "The design review didn't catch the missing validation" is correct; "Bob forgot to add validation" is incorrect. People operate within processes — if a person can make the mistake, the process should have caught it (Beyer et al., 2016).

**Compact Format** — Every post-mortem must fit in 15 lines or fewer. The constraint forces discipline: state the failure, the missed gate, and the fix. Anything longer indicates the root cause hasn't been identified clearly enough. The template fields are: what failed, why, and which gate was missed.

**Append-Only** — Once a post-mortem is written, it's immutable. If understanding deepens later, write a new post-mortem referencing the original. This preserves the history of understanding and prevents retroactively modifying the record.

**Restart Check** — After identifying the fix, the post-mortem must answer the restart check: "Can we safely re-enter the pipeline from this point, or do we need to go further back?" This prevents the same failure from recurring because the re-entry point was too shallow.

## Content

### Post-Mortem Template Fields

| Field | Content |
|---|---|
| What failed | The observable failure (e.g., "acceptance test rejected: feature doesn't handle edge case X") |
| Why | The process root cause (e.g., "pre-mortem during discovery didn't surface edge case X") |
| Missed gate | Which quality gate should have caught this (e.g., "design review didn't verify boundary conditions") |
| Fix | The corrective action (e.g., "add boundary condition check to design review checklist") |
| Restart check | Where to re-enter the pipeline (e.g., "re-enter at design review — the architecture is sound, only the design needs updating") |

### Routing After Post-Mortem

| Root cause location | Re-entry point |
|---|---|
| Discovery gap (missing requirement) | Back to discovery |
| Architecture gap (wrong design) | Back to architecture |
| Planning gap (wrong specification) | Back to planning |
| Implementation gap (correct spec, wrong code) | Back to development |
| Fundamentally flawed product | Abandon |

### What Post-Mortems Are Not

- Not a place for suggestions or wish-list items
- Not a place for blame or finger-pointing
- Not a detailed timeline of everything that happened
- Not a design document for the fix (the fix is a single sentence, the design happens when re-entering the pipeline)

## Related

- [[requirements/pre-mortem]]
- [[workflow/flowr-spec]]