---
name: extend-criteria
description: Add acceptance criteria discovered after scope is written — gaps found during implementation or review, and post-merge defects
version: "1.0"
author: any
audience: developer, reviewer, product-owner
workflow: feature-lifecycle
---

# Extend Criteria

This skill is loaded when any agent discovers a missing behavior that is not covered by the existing acceptance criteria. It provides the decision rule, UUID assignment, and commit protocol for adding new criteria mid-flight or post-merge.

## When to Use

- **Developer (Step 4)**: implementation reveals an untested behavior
- **Reviewer (Step 5)**: code review reveals an observable behavior with no acceptance criterion
- **Post-merge**: a defect is found in production and a regression criterion must be added

Do not use this skill to scope new features. New observable behaviors that go beyond the current feature's user stories must be escalated to the PO.

## Decision Rule: Is This a Gap or a New Feature?

Ask: "Does this behavior fall within the intent of the current user stories?"

| Situation | Action |
|---|---|
| Edge case or error path within approved scope | Add criterion with `Source: developer` or `Source: reviewer` |
| New observable behavior users did not ask for | Escalate to PO; do not add criterion unilaterally |
| Post-merge regression (the feature was accepted and broke later) | Reopen feature doc; add criterion with `Source: bug` |
| Behavior already present but criterion was never written | Add criterion with appropriate `Source:` |
| **Architecture decision contradicts an acceptance criterion** | **Escalate to PO immediately. Do not proceed with implementation.** |

When in doubt, ask the PO before adding.

## Criterion Format

All criteria use this format (mandatory `Source:` field):

```markdown
- `<uuid>`: <Short description ending with a period>.
  Source: <source>

  Given: <precondition>
  When: <action>
  Then: <single observable outcome>
```

**Source values** (choose exactly one):
- `stakeholder` — an external stakeholder gave this requirement to the PO
- `po` — the PO originated this criterion independently
- `developer` — a gap found during Step 4 implementation
- `reviewer` — a gap found during Step 5 verification
- `bug` — a post-merge regression; the feature doc was reopened

**Rules**:
- UUID must be unique across the entire project
- Generate: `python -c "import uuid; print(uuid.uuid4())"`
- `Then` must be a single observable, measurable outcome — no "and"
- Do not add `Source:` retroactively to criteria that predate this field

## Procedure by Role

### Developer (Step 4)

1. Determine whether this is a gap within scope or a new feature (use the decision table above)
2. If it is within scope:
   a. Add the criterion to the feature doc with `Source: developer`
   b. Write the failing test for it (load `skill tdd`)
   c. Make it green (continue Red-Green-Refactor)
   d. Commit: `test(<feature-name>): add gap criterion <uuid>`
3. If it is out of scope: write a note in TODO.md under `## Next`, flag it for the PO after Step 5

### Reviewer (Step 5)

1. Determine whether this is a gap within scope or a new feature
2. If it is within scope:
   - Add the criterion to the feature doc with `Source: reviewer`
   - Record in the REJECTED report: "Added criterion `<uuid>` — developer must implement before resubmitting"
3. If it is out of scope:
   - Do not add the criterion
   - Note it in the report as a future backlog item

### Post-merge Defect

1. Move the feature doc back to in-progress:
   ```bash
   mv docs/features/completed/<name>.md docs/features/in-progress/<name>.md
   git add -A
   git commit -m "chore(workflow): reopen <name> for bug fix"
   ```
2. Add the new criterion with `Source: bug`
3. Return to Step 3 (write failing test) then Step 4 (implement) then Step 5 (verify) then Step 6 (accept)
4. Update TODO.md to reflect the reopened feature at the correct step

## Checklist

Before committing a new criterion:
- [ ] UUID is unique (search: `grep -r "<uuid>" docs/features/` and `grep -r "<uuid>" tests/`)
- [ ] `Source:` value is one of the five valid values
- [ ] `Then` is a single, observable outcome (no "and")
- [ ] Blank line between `Source:` line and `Given:`
- [ ] A corresponding test will be written (or already exists)
