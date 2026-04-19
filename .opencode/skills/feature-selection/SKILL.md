---
name: feature-selection
description: Score and select the next backlog feature by value, effort, and dependencies
version: "1.0"
author: product-owner
audience: product-owner
workflow: feature-lifecycle
---

# Feature Selection

Select the next most valuable, unblocked feature from the backlog using a lightweight scoring model grounded in flow economics and dependency analysis.

**Research basis**: Weighted Shortest Job First (WSJF) — Reinertsen *Principles of Product Development Flow* (2009); INVEST criteria — Wake (2003); Kano model — Kano (1984); Dependency analysis — PMBOK Critical Path Method. See `docs/scientific-research/requirements-elicitation.md`.

**Core principle**: Cost of Delay ÷ Duration. Features with high user value and low implementation effort should start first. Features blocked by unfinished work should wait regardless of value.

## When to Use

Load this skill when `TODO.md` says "No feature in progress" — before moving any feature to `in-progress/`.

## Step-by-Step

### 1. Verify WIP is Zero

```bash
ls docs/features/in-progress/
```

- 0 files → proceed
- 1 file → a feature is already in progress; do not start another; exit this skill
- >1 files → WIP violation; stop and resolve before proceeding

### 2. List BASELINED Candidates

Read each `.feature` file in `docs/features/backlog/`. Check its discovery section for `Status: BASELINED`.

- Non-BASELINED features are not eligible — they need Step 1 (scope) first
- If no BASELINED features exist: inform the stakeholder; run `@product-owner` with `skill scope` to baseline the most promising backlog item first

**IMPORTANT**

**NEVER move a feature to `in-progress/` unless its discovery section has `Status: BASELINED`**

### 3. Score Each Candidate

For each BASELINED feature, fill this table:

| Feature | Value (1–5) | Effort (1–5) | Dependency (0/1) | WSJF |
|---|---|---|---|---|
| `<name>` | | | | Value ÷ Effort |

**Value (1–5)** — estimate user/business impact:
- 5: Must-have — core workflow blocked without it (Kano: basic need)
- 4: High — significantly improves the primary use case
- 3: Medium — useful but not blocking (Kano: performance)
- 2: Low — nice-to-have (Kano: delighter)
- 1: Minimal — cosmetic or out-of-scope edge case

Use the number of `Must` Examples in the feature's `Rule:` blocks as a tiebreaker: more Musts → higher value.

**Effort (1–5)** — estimate implementation complexity:
- 1: Trivial — 1–2 `@id` Examples, no new domain concepts
- 2: Small — 3–5 `@id` Examples, one new domain entity
- 3: Medium — 6–8 `@id` Examples or cross-cutting concern
- 4: Large — >8 Examples or multiple interacting domain entities
- 5: Very large — spans multiple modules or has unknown complexity

**Dependency (0/1)** — does this feature assume another backlog feature is already built?
- 0: Independent — no hard prerequisite
- 1: Blocked — requires another backlog feature to be completed first

A Dependency=1 feature is **ineligible for selection** regardless of WSJF score. Apply WSJF only to Dependency=0 features.

### 4. Select

Pick the BASELINED, Dependency=0 feature with the highest WSJF score.

Ties: prefer higher Value (user impact matters more than effort optimization).

If all BASELINED features have Dependency=1: stop and resolve the blocking dependency first — select and complete the depended-upon feature.

### 5. Move and Update TODO.md

```bash
mv docs/features/backlog/<name>.feature docs/features/in-progress/<name>.feature
```

Update `TODO.md`:

```markdown
# Current Work

Feature: <name>
Step: 1 (SCOPE) or 2 (ARCH) — whichever is next
Source: docs/features/in-progress/<name>.feature

## Next
Run @<agent-name> — <first concrete action for this feature>
```

- If the feature has no `Rule:` blocks yet → Step 1 (SCOPE): `Run @product-owner — load skill scope and write stories`
- If the feature has `Rule:` blocks but no `@id` Examples → Step 1 Phase 4 (Criteria): `Run @product-owner — load skill scope and write acceptance criteria`
- If the feature has `@id` Examples → Step 2 (ARCH): `Run @software-engineer — load skill implementation and write architecture stubs`

### 6. Commit

```bash
git add docs/features/in-progress/<name>.feature TODO.md
git commit -m "chore: select <name> as next feature"
```

## Checklist

- [ ] `in-progress/` confirmed empty before selection
- [ ] Only BASELINED features considered
- [ ] Dependency=1 features excluded from scoring
- [ ] WSJF scores filled for all candidates
- [ ] Selected feature has highest WSJF among Dependency=0 candidates
- [ ] Feature moved to `in-progress/`
- [ ] `TODO.md` updated with correct Step and `Next` line
- [ ] Changes committed
