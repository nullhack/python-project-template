---
name: select-feature
description: Score and select the next backlog feature by value, effort, and dependencies
version: "1.0"
author: product-owner
audience: product-owner
workflow: feature-lifecycle
---

# Feature Selection

Select the next most valuable, unblocked feature from the backlog using a lightweight scoring model grounded in flow economics and dependency analysis.

**Research basis**: Weighted Shortest Job First (WSJF) — Reinertsen *Principles of Product Development Flow* (2009); INVEST criteria — Wake (2003); Kano model — Kano (1984); Dependency analysis — PMBOK Critical Path Method. See `docs/research/requirements-elicitation.md`.

**Core principle**: Cost of Delay / Duration. Features with high user value and low implementation effort should start first. Features blocked by unfinished work should wait regardless of value.

## When to Use

Load this skill when the session file in `.flowr/sessions/` `state` is `idle` (or no active item) — before moving any feature to `in-progress/`.

## Step-by-Step

### 1. Verify WIP is Zero

```bash
ls docs/features/in-progress/
```

- 0 files -> proceed
- 1 file -> a feature is already in progress; do not start another; exit this skill
- >1 files -> WIP violation; stop and resolve before proceeding

### 2. List BASELINED Candidates

Read each `.feature` file in `docs/features/backlog/`. Check its discovery section for `Status: BASELINED`.

- Non-BASELINED features are not eligible — they need Step 1 (scope) first
- If no BASELINED features exist: inform the stakeholder; run `@product-owner` with `skill define-scope` to baseline the most promising backlog item first

**IMPORTANT**

**NEVER move a feature to `in-progress/` unless its discovery section has `Status: BASELINED`. Only the PO may move `.feature` files — no other agent ever creates, edits, or moves them.**

### 3. Score Each Candidate

For each BASELINED feature, fill this table:

| Feature | Value (1-5) | Effort (1-5) | Dependency (0/1) | WSJF |
|---|---|---|---|---|
| `<name>` | | | | Value / Effort |

See [[requirements/wsjf]] for the Value, Effort, and Dependency scales, the WSJF formula, and selection rules (including tiebreaker and dependency eligibility).

### 4. Select

Pick the BASELINED, Dependency=0 feature with the highest WSJF score.

See [[requirements/wsjf]] for selection rules including tiebreaker logic and handling all-Dependency=1 backlogs.

### 5. Move Feature and Update Session

```bash
mv docs/features/backlog/<name>.feature docs/features/in-progress/<name>.feature
```

Update the session file in `.flowr/sessions/` — add (or replace) the active item block:

```markdown
## Active Items

@id: <name>
@state: [STEP-1-SCOPE] or [STEP-2-ARCH] — whichever is next
@branch: [NONE]
```

- If the feature has no `Rule:` blocks yet -> `@state: STEP-1-SCOPE`; `Run @product-owner — load skill define-scope and write stories`
- If the feature has `Rule:` blocks but no `@id` Examples -> `@state: STEP-1-SCOPE`; `Run @product-owner — load skill define-scope and write acceptance criteria`
- If the feature has `@id` Examples -> `@state: STEP-2-ARCH`; `Run @system-architect — load skill architect`

### 6. Commit

```bash
git add docs/features/in-progress/<name>.feature .flowr/sessions/session.yaml
git commit -m "chore: select <name> as next feature"
```

## Checklist

- [ ] `in-progress/` confirmed empty before selection
- [ ] Only BASELINED features considered
- [ ] Dependency=1 features excluded from scoring
- [ ] WSJF scores filled for all candidates
- [ ] Selected feature has highest WSJF among Dependency=0 candidates
- [ ] Feature moved to `in-progress/`
- [ ] session file updated with correct `state`
- [ ] Changes committed