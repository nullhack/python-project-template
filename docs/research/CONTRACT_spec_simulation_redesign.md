# Contract: Spec Simulation Redesign

> Status: IN PROGRESS — adversarial audit findings being fixed
> Date: 2026-05-14
> Replaces: classical discovery->architecture->feature->TDD flow with simulation-first approach

---

## 1. Problem Statement

Classical discovery->feature->TDD flow produces specs that are never tested before code is written. This causes 3-5 restart cycles when end-to-end integration reveals fundamental spec issues. The root cause: specs describe structure (entities, events) but not behavior (state transitions, error handling, edge cases). By the time code is written against these specs, gaps are expensive to fix.

## 2. Solution: Simulate Before Code

Spec simulation is a tabletop exercise: the agent mentally walks through the system described in the spec, creates I/O pairs as evidence in /tmp, and discovers rules, pain points, and E2E test candidates. The spec is rewritten to address findings. This loop repeats until the spec is clean. Only THEN do features, code, and tests get created.

**Key principles**:
- Rules are DISCOVERED through simulation, not pre-written.
- Given/When/Then is the LAST step (in .feature files), not the first (in spec documents).
- No user stories (As a/I want/So that). Rules are descriptive statements with unique titles that map directly to Example titles.
- No numbered prefixes (R001, SIM-001). Use descriptive text; beehave already provides unique IDs via titles.
- External contracts define how users/systems interact with the solution — these are the primary simulation target.

## 3. Behavioral Spec Evolution

The behavioral spec starts as a minimal structural skeleton and evolves through simulation:

**Iteration 0** (from spec-creation):
- Context description (what this bounded context does)
- Entities and their purpose
- Data shapes (field names, types — constraints may be `?`)
- Integration points (inter-context communication)
- External contracts (how users/systems interact with this context — actor, trigger, input, output, errors)
- No rules, no state machines, no Given/When/Then

**Simulation N** adds:
- Rules discovered (descriptive statements, no numbered prefixes)
- Pain points resolved (descriptive statements, no numbered prefixes)
- Data constraints refined (`?` -> concrete constraints)
- State machines emerge from accumulated rules
- Error handling paths discovered
- External contract details refined (error cases, preconditions, side effects)

**Final spec** (after validation loop):
- Complete state machines
- All rules discovered (descriptive statements)
- All data constraints concrete
- All integration contracts defined
- All external contracts fully specified
- All error paths specified
- Zero unresolved pain points

## 4. New Flow Structure

```
main-flow
  |-- discovery-flow (2 states)
  |     |-- stakeholder-interview (PO: conduct-interview)
  |     '-- spec-creation (SA+DE: create-behavioral-spec + define-ubiquitous-language)
  |
  |-- spec-validation-flow (NEW, 3 states, iterative loop)
  |     |-- simulate-spec (SA: simulate-spec)
  |     |-- review-simulation (R: review-simulation)
  |     '-- fix-spec (SA+DE: fix-spec, loops to simulate-spec or exits)
  |     [cap: 5 iterations -> escalate root causes to stakeholder]
  |
  |-- architecture-flow (4 states, same structure)
  |     |-- architecture-assessment
  |     |-- context-mapping
  |     |-- technical-design
  |     '-- review-signoff
  |
  '-- feature-development-flow (same structure)
        |-- planning-flow
        |     |-- feature-selection (rules from simulation_results)
        |     |-- feature-breakdown (verify rules, write Rule blocks, INVEST validation)
        |     |-- feature-examples (Given/When/Then written HERE)
        |     |-- spec-review
        |     '-- create-py-stubs (beehave generate)
        |-- development-flow (TDD cycle)
        '-- delivery-flow (acceptance, merge, publish)
```

## 5. Git Branch Strategy

**dev branch model**: All project-level commits go to `dev`, not `main`.

- `main`: production-ready, stable. Only receives changes via PR from dev.
- `dev`: integration branch. Discovery, architecture, spec validation commits go here.
- Feature branches: `feat/<stem>` branched from `dev`, merged back to `dev`.
- PRs: created from `dev` -> `main` when stakeholder decides to publish.

Changes from current model:
- All `git: main` in flows -> `git: dev`
- `committed-to-main-locally` condition -> `committed-to-dev-locally`
- `merge-local` skill: squash-merges feature -> `dev` (was feature -> main)
- `create-pr` skill: pushes `dev` to remote, creates PR dev -> main
- `publish-decision`: decides whether to PR dev -> main

## 6. Template Changes

### product_definition.md (TRIM: ~50 lines from 119)

Remove: DoD checklist, Deployment checklist, Scope Changes table. Those belong in AGENTS.md.

Keep: Vision, Why, Users, IS/IS NOT, Quality Attributes, Out of Scope, Delivery Order.

### domain_model.md (KEEP, trimmed)

Keep `domain_model.md.template` for the structural domain model (entities, relationships, bounded contexts, aggregates, context map). This is the project-wide WHAT EXISTS view. Remove events/commands tables (those concepts feed into behavioral_spec). Updated template removes:
- Events and Commands section (behavioral -> behavioral_spec)
- Changes table (use git log)

### behavioral_spec.md (NEW)

Per bounded context. Starts minimal (iteration 0), evolves through simulation. Template sections:

1. **Context**: what this bounded context does (2-3 sentences)
2. **Entities**: name, purpose, rough lifecycle
3. **Data Shapes**: field name, type, constraints (may be `?` initially)
4. **Integration Points**: inter-context communication, trigger, payload/response shape
5. **External Contracts**: how users/external systems interact — actor, trigger, input, output, errors, side effects, preconditions. PRIMARY simulation target.
6. **State Machines**: emerge from simulation (empty at iteration 0)
7. **Error Handling**: discovered during simulation (empty at iteration 0)
8. **Invariants**: discovered during simulation (empty at iteration 0)
9. **Rules Discovered**: descriptive statements from simulation (empty at iteration 0)
10. **Pain Points**: unresolved issues from simulation (empty at iteration 0)

NO Given/When/Then. NO As a/I want/So that. NO numbered prefixes.

### simulation_results.md (NEW)

Per simulation iteration. Contains:
1. Iteration number and context being simulated
2. Scenarios walked (happy path, edge cases, error paths)
3. I/O pairs created in /tmp/sim/<context>/
4. Pain points found (descriptive statements, no prefixes)
5. Rules discovered (descriptive statements, no prefixes)
6. E2E test candidates (descriptive titles suitable for Example: titles)
7. Resolution status per pain point

### glossary.md (UNCHANGED)

### feature.template (UNCHANGED)

## 7. Skill Changes

### NEW Skills (4)

**create-behavioral-spec** (owner: SA+DE):
- Reads interview notes
- Identifies bounded contexts from interview data
- Creates product_definition.md (trimmed template)
- Creates domain_model.md (structural: entities, relationships, aggregates, contexts)
- Creates behavioral_spec.md per bounded context (structural skeleton + external contracts only)
- Creates glossary.md with initial terms
- NO rules, NO state machines, NO Given/When/Then

**simulate-spec** (owner: SA):
- Reads behavioral_spec.md for a bounded context
- Primary simulation against external contracts: walk each contract's input -> output
- Walks through scenarios mentally: happy paths, edge cases, error paths
- Creates I/O pairs in /tmp/sim/<context>/ as evidence
- Discovers rules and pain points
- Writes simulation_results.md

**review-simulation** (owner: R):
- Adversarial review of simulation_results.md
- Adds missed scenarios
- Validates pain points are real
- Decides: PASS (spec clean enough) or FAIL (needs more work)
- Exit criteria: zero unresolved pain points, all external contracts covered, all state transitions covered, all error paths specified

**fix-spec** (owner: SA+DE):
- Rewrites behavioral_spec.md addressing all pain points from simulation
- Full rewrite for coherence, not patches
- Incorporates discovered rules
- Fills in `?` constraints
- State machines emerge from accumulated rules

### MODIFIED Skills (8)

**discover-features**:
- Rules source: simulation_results.md (was domain_model.md)
- Still reads product_definition.md for delivery order and domain_model.md for entity/context mapping
- Still creates .feature files with title + description + # Business rules: + # Constraints:
- Rules come FROM simulation results, not from event-storming derivation

**discover-rules**:
- Rules source: simulation_results.md discovered rules (was domain_model events/invariants/commands)
- Writes `# Business rules:` and `# Constraints:` into .feature files from simulation findings
- Traceability: every simulation rule -> at least one feature rule

**break-down-feature**:
- No user stories (As a/I want/So that removed)
- Rules from simulation are already validated — skill verifies they're specific enough
- Writes Rule: blocks using rule text directly as title
- INVEST validation stays

**write-bdd-features**:
- No user stories reference
- Writes Given/When/Then Examples under Rule: blocks
- Same Example quality criteria (observable, declarative, distinct, pre-mortem coverage)

**conduct-interview**:
- `domain_model.md` references -> `behavioral_spec.md` + `domain_model.md`

**map-contexts** (architecture-flow):
- in: behavioral_spec.md + domain_model.md (was domain_model.md only)

**define-ubiquitous-language**:
- References change from domain_model.md to domain_model.md + behavioral_spec.md

**merge-local**:
- Squash-merges feature -> `dev` (was feature -> main)

**create-pr**:
- Pushes `dev` to remote, creates PR dev -> main (was push main)

### REMOVED Skills (3)

- **facilitate-event-storming**: folded into create-behavioral-spec (event storming concepts absorbed into behavioral-contracts knowledge)
- **domain-discovery**: folded into create-behavioral-spec
- **define-product-scope**: folded into create-behavioral-spec (product_definition written there)

## 8. Knowledge Changes

### NEW Knowledge (2)

**requirements/spec-simulation.md**: Simulation technique, I/O file format (/tmp/sim/<context>/), pain point classification (ambiguous / contradictory / missing / edge-case), rules as descriptive statements (no numbered prefixes), external contract simulation priority, exit criteria (zero unresolved pain points).

**domain-modeling/behavioral-contracts.md**: How to write state machines, data shapes, integration contracts, external contracts. Event storming concepts (events, commands, aggregates) absorbed here as background knowledge for spec creation, not as separate workshop step.

### MODIFIED Knowledge (5)

**requirements/feature-discovery.md**: Rules come from simulation_results.md, not from event-storming derivation. Lifecycle updated: discovery creates structural spec + external contracts -> simulation discovers rules -> planning groups rules into features.

**requirements/rule-derivation.md**: Sources change from domain model events/invariants/commands -> simulation discovered rules. Traceability: simulation rule -> feature rule -> Example.

**architecture/reconciliation.md**: domain_model.md references stay (structural model is kept). Add behavioral_spec.md to cross-document checks. Cross-document checks updated.

**software-craft/git-conventions.md**: main -> dev branch model. Squash-merge to dev. PR from dev -> main. Local dev as staging area (was local main).

**architecture/adr.md**: Example criteria references stay the same (title-based, not @id).

### DEPRECATED Knowledge (1)

**domain-modeling/event-storming.md**: Concepts absorbed into behavioral-contracts.md. File kept for reference but no skills reference it.

## 9. Flow YAML Changes

### discovery-flow.yaml (REWORK: 4 states -> 2) [DONE]

States:
1. stakeholder-interview (PO, conduct-interview) -> git: dev
2. spec-creation (SA, skills: create-behavioral-spec, define-ubiquitous-language) -> git: dev

Exits: complete
Out: product_definition.md, domain_model.md, behavioral_spec.md, glossary.md

### spec-validation-flow.yaml (NEW: 3 states + loop) [DONE]

States:
1. simulate-spec (SA, skill: simulate-spec) -> git: dev
2. review-simulation (R, skill: review-simulation) -> git: dev
3. fix-spec (SA, skill: fix-spec) -> git: dev -> loops to simulate-spec or exits
4. validated (exit state, committed-to-dev-locally)

Exits: validated, needs-reinterview
Conditions: max 5 iterations, escalation to stakeholder at cap

### main-flow.yaml (UPDATE) [DONE]

States: discovery -> spec-validation -> architecture -> feature-development
All git: dev (except feature-development which is git: feature)

### architecture-flow.yaml (UPDATE) [DONE]

All git: dev. domain_model.md references stay. behavioral_spec.md added to in. simulation_results.md added to in. committed-to-dev-locally.

### planning-flow.yaml (UPDATE) [DONE]

All git: dev. domain_model.md -> behavioral_spec.md + simulation_results.md. committed-to-dev-locally.

### feature-development-flow.yaml (UPDATE) [PENDING]

git: main -> git: dev on planning state. flow-version: "^13".

### delivery-flow.yaml (UPDATE) [PENDING]

git: main -> git: dev on local-merge, publish-decision, pr-creation.
committed-to-main-locally -> committed-to-dev-locally.
Description updates: merge to dev, PR dev -> main.

### branding-flow.yaml (UPDATE) [PENDING]

git: main -> git: dev. committed-to-main-locally -> committed-to-dev-locally.

### setup-project-flow.yaml (UPDATE) [PENDING]

git: main -> git: dev. committed-to-main-locally -> committed-to-dev-locally.

### post-mortem-flow.yaml (UPDATE) [PENDING]

git: main -> git: dev.

### development-flow.yaml, tdd-cycle-flow.yaml (UNCHANGED)

These operate on feature branches. git: feature stays.

## 10. Files Summary

### Create (9 files)
- `.templates/docs/spec/behavioral_spec.md.template` [DONE]
- `.templates/docs/spec/simulation_results.md.template` [DONE]
- `.flowr/flows/spec-validation-flow.yaml` [DONE]
- `.opencode/skills/create-behavioral-spec/SKILL.md` [DONE]
- `.opencode/skills/simulate-spec/SKILL.md` [DONE]
- `.opencode/skills/review-simulation/SKILL.md` [DONE]
- `.opencode/skills/fix-spec/SKILL.md` [DONE]
- `.opencode/knowledge/requirements/spec-simulation.md` [PENDING]
- `.opencode/knowledge/domain-modeling/behavioral-contracts.md` [PENDING]

### Modify (20 files)
- `.templates/docs/spec/product_definition.md.template` (trim) [DONE]
- `.flowr/flows/main-flow.yaml` [DONE]
- `.flowr/flows/discovery-flow.yaml` (rework) [DONE]
- `.flowr/flows/architecture-flow.yaml` [DONE]
- `.flowr/flows/planning-flow.yaml` [DONE]
- `.flowr/flows/feature-development-flow.yaml` [PENDING]
- `.flowr/flows/delivery-flow.yaml` [PENDING]
- `.flowr/flows/branding-flow.yaml` [PENDING]
- `.flowr/flows/setup-project-flow.yaml` [PENDING]
- `.flowr/flows/post-mortem-flow.yaml` [PENDING]
- `.opencode/skills/discover-features/SKILL.md` [DONE]
- `.opencode/skills/discover-rules/SKILL.md` [DONE]
- `.opencode/skills/break-down-feature/SKILL.md` [DONE]
- `.opencode/skills/write-bdd-features/SKILL.md` [DONE]
- `.opencode/skills/conduct-interview/SKILL.md` [PENDING]
- `.opencode/skills/map-contexts/SKILL.md` [PENDING]
- `.opencode/skills/define-ubiquitous-language/SKILL.md` [PENDING]
- `.opencode/skills/merge-local/SKILL.md` [PENDING]
- `.opencode/skills/create-pr/SKILL.md` [PENDING]
- `.opencode/knowledge/requirements/feature-discovery.md` [PENDING]
- `.opencode/knowledge/requirements/rule-derivation.md` [PENDING]
- `.opencode/knowledge/architecture/reconciliation.md` [PENDING]
- `.opencode/knowledge/software-craft/git-conventions.md` [PENDING]

### Delete (3 files) [DONE]
- `.opencode/skills/facilitate-event-storming/SKILL.md` [DONE]
- `.opencode/skills/domain-discovery/SKILL.md` [DONE]
- `.opencode/skills/define-product-scope/SKILL.md` [DONE]

### Keep unchanged
- `.templates/docs/spec/glossary.md.template`
- `.templates/docs/spec/domain_model.md.template` (restored, trimmed)
- `.templates/docs/features/<feature_name>.feature.template`
- `.opencode/knowledge/domain-modeling/event-storming.md` (kept for reference)
- All development/TDD skills
- All software-craft knowledge (except git-conventions)

## 11. Rules

1. No "scaffold" word anywhere — use "create", "generate", "build", "set up".
2. No Given/When/Then in behavioral_spec.md — it belongs only in .feature files.
3. No As a/I want/So that anywhere — rules are descriptive statements with unique titles.
4. No @id tags — title-based mapping via pytest-beehave.
5. No numbered prefixes for rules/pain points (R001, SIM-001) — use descriptive text.
6. All `git: main` -> `git: dev` across all flows.
7. All `committed-to-main-locally` -> `committed-to-dev-locally`.
8. Feature branches branch from `dev`, merge to `dev`.
9. Simulation loop capped at 5 iterations; escalation to stakeholder at cap.
10. Spec starts minimal (structural skeleton + external contracts), rules discovered through simulation.
11. Full spec rewrite in fix-spec (not patches) for coherence.
12. `beehave generate <feature_id>` for test stubs, `beehave check` for traceability.
13. External contracts are the primary simulation target — simulate inputs/outputs first.
