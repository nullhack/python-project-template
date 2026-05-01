# Development Lifecycle Workflow — Non-Deterministic State Machine Design

## Model Rules

- Each stage is a node or a link to another diagram (sub-flow)
- Diagrams can contain cycles, but cycles only point to the same level (not parent/child)
- Each diagram has finite, flat exit points
- Sub-flows are linked from states that require them

## Design Principles

### Priority Order (conflict resolution)

When two principles conflict, the earlier one wins:

**YAGNI > DRY > KISS > OC > SOLID > Design Patterns**

1. **YAGNI** — Don't build what you don't need yet. If a feature isn't required by a .feature file example, it doesn't exist.
2. **DRY** — Don't repeat yourself, but only after YAGNI passes. Duplication is better than the wrong abstraction.
3. **KISS** — Keep it simple, but only after eliminating duplication. The simplest design that passes all .feature examples wins.
4. **OC** — Object Calisthenics, but only after KISS passes. Structure serves simplicity, not the other way around.
5. **SOLID** — Apply SOLID principles, but only after OC passes. SOLID is a tool, not a goal.
6. **Design Patterns** — Use patterns only when simpler approaches don't work. A pattern is justified only when YAGNI, KISS, and OC all point to it.

### Philosophical Principles (from the Zen of Python)

These guide all design decisions. When in doubt, refer to these:

- Beautiful is better than ugly.
- Explicit is better than implicit.
- Simple is better than complex.
- Complex is better than complicated.
- Flat is better than nested.
- Sparse is better than dense.
- Readability counts.
- Special cases aren't special enough to break the rules.
- Although practicality beats purity.
- Errors should never pass silently unless explicitly silenced.
- In the face of ambiguity, refuse the temptation to guess.
- There should be one — and preferably only one — obvious way to do it.
- Now is better than never. Although never is often better than *right now*.
- If the implementation is hard to explain, it's a bad idea.
- If the implementation is easy to explain, it may be a good idea.

### Core Workflow Principles

1. **Fail-fast, shift-left** — issues caught early cost 10x less than issues caught late. The Review sub-step is tiered so the most expensive issues (design) are caught before cheaper issues (conventions) are invested in.
2. **Never invest in Tier 3 work on code that hasn't passed Tier 1** — docstrings, formatting, and conventions are waste on code that may need complete restructuring.
3. **BDD features are the single thread of truth** — written in Planning, used as test spec in Development, validated in Acceptance.
4. **Each artifact is a translation of the previous one** — never skip an artifact. Each one is a checkpoint where you can validate alignment with the domain before investing in the next level of detail. If scope is wrong, .features will be wrong. If .features are wrong, tests will test the wrong things. If signatures don't match the domain model, test bodies will couple to wrong structure.
5. **Architecture must be reviewed before implementation begins** — catching design errors after SE has built everything is 100x more expensive than catching them during architecture. SA's work is reviewed by a separate R hat during Architecture Review & Sign-off, not after Development.
6. **Technical review happens in Development, not after** — R reviews all three tiers (design, structure, conventions) during Development's Review sub-step. Acceptance (PO) is purely business validation. This eliminates redundancy and catches issues where they're cheapest to fix.

---

## Actors

| Actor | Abbreviation | Responsibility | Documents they own |
|---|---|---|---|
| **Product Owner** | PO | Business requirements, scope validation, acceptance sign-off | interview-notes/*.md, product_definition.md, features/<file>.feature |
| **Domain Expert** | DE | Domain knowledge, ubiquitous language | domain_model.md, glossary.md, event_map |
| **Software Architect** | SA | Architecture decisions, context mapping, interface contracts | context_map.md, adr/*.md, technical_design.md, system.md, py_stubs, test_stubs |
| **Software Engineer** | SE | Implementation, test design, code quality | test_bodies, function_bodies, commits |
| **Reviewer** | R | Independent verification, cannot review own work | Review evidence (categorized by tier), approval records |

**Key principle: You cannot review your own work.** R is a separate hat (not necessarily a separate person). If SA designed the architecture, someone else must wear the R hat for Architecture Review & Sign-off. If SE wrote the code, someone else must wear the R hat for Development's Review sub-step.

In small teams, PO+DE may be one person, and SA+SE may be one person. But the **responsibilities are distinct** — the same person wears different hats. The R hat ensures independent verification at critical gates.

---

## Process Support

The `.opencode/` directory provides the meta-process infrastructure that guides how the flows are executed. It is separate from project artifacts — it is the procedural and reference system, not the work product.

**Entry point**: `AGENTS.md` (project root) is loaded every session. It provides navigation, wikilink resolution, and discovery commands. See `agent-design/principles` for design rationale.

**Discover, don't enumerate**: The number and names of agents, skills, and knowledge files change. AGENTS.md provides discovery commands rather than inventories:

```bash
ls .opencode/agents/                    # agent identity definitions
ls .opencode/skills/                    # skill directories (each has SKILL.md)
find .opencode/knowledge -name '*.md'   # knowledge files
```

### Agent-Role Mapping

| Agent | Abbreviation | Decides |
|---|---|---|
| Product Owner | PO | Scope, priority, acceptance |
| Domain Expert | DE | Domain model, ubiquitous language |
| System Architect | SA | Architecture, ADRs, project structure |
| Reviewer | R | Pass/fail (cannot review own work) |

Each flow state specifies its owner (PO, DE, SA, SE, or R). The owner maps to the agent file in `.opencode/agents/`. Agent files contain identity only (who I am, what I decide) — no skill lists, no routing, no knowledge content.

### Skill Loading

Each flow state loads skills on demand. The flow YAML `skills` field specifies which skill to invoke. Skills are procedural (step-by-step instructions) and are the only files that load knowledge. See `skill-design/principles` for skill structure.

### Knowledge Resolution

Skills reference knowledge via `[[domain/concept]]` wikilinks, resolved to `.opencode/knowledge/{domain}/{concept}.md`. Knowledge files use 4-section progressive disclosure:

| Fragment | Loads | Token Savings |
|---|---|---|
| `[[domain/concept#key-takeaways]]` | Frontmatter + Key Takeaways | ~80% |
| `[[domain/concept#concepts]]` | Frontmatter + Key Takeaways + Concepts | ~65% |
| `[[domain/concept]]` | Entire file | 0% |

Knowledge domains: `architecture`, `domain-modeling`, `requirements`, `software-craft`, `workflow`, `agent-design`, `skill-design`, `knowledge-design`.

---

## Main Flow: Development Lifecycle

The main flow separates project-level work (done once) from feature-level work (looped per feature).

```
Discovery → Architecture → Feature Development ←┐
     ↑            ↑                   │            │
     │            └ needs_architecture┘            │
     └ needs_discovery           next-feature ─────┘
                            completed ──► [Completed]
                            cancelled ──► [Cancelled]
```

Terminal exits: **completed** | **cancelled**

| State | Purpose | Sub-flow | Transitions |
|---|---|---|---|
| **Discovery** | Domain understanding & scope | → Discovery Flow | `complete` → Architecture |
| **Architecture** | Architecture & context mapping | → Architecture Flow | `complete` → Feature Development, `needs_discovery` → Discovery |
| **Feature Development** | Feature-level loop: Planning → Dev → Acceptance → PR | → Feature Development Flow | `next-feature` → Feature Development (loop), `needs_architecture` → Architecture, `cancelled` → Cancelled, `completed` → Completed |

**Why separate project-level and feature-level?** Discovery and Architecture establish the domain model and technical foundation once for the entire project. Feature Development then loops: each feature goes through Planning → Development → Acceptance → PR Creation. When all features are delivered (or none remain), the project completes.

---

## Hotfix Process

Hotfixes use the same Main Flow (Discovery → Architecture → Feature Development) but with constrained scope:

**Scope constraints:**
- **Discovery**: Focused on root cause analysis of the specific issue
- **Architecture**: Minimal change that fixes the issue without breaking existing contracts
- **Planning**: PO decides the specification approach:
  - *Add new example* to existing .feature file (missing edge case)
  - *Create new .feature file* (completely new behavior required)
  - *Fix existing examples* (current specification is wrong)
- **Development**: Same TDD cycle and Review sub-flow - no shortcuts
- **Acceptance**: Same acceptance process - PO verifies business behavior
- **PR Creation**: Same PR process

**Key principle: Quality gates remain the same.** Speed comes from smaller scope and focused specification changes, not skipped steps. A hotfix that breaks architecture or introduces technical debt creates bigger problems than the original issue.

---

## Test Body Design Pattern (cross-cutting)

Every test body across all levels follows **Given/When/Then maps to Arrange/Act/Assert** — but the scope of what's under test differs:

| Test Level | Scope | "Given" sets up | "When" triggers | "Then" asserts |
|---|---|---|---|---|
| **Unit** | Single domain object | Value objects, primitives | A method/command on one object | State changes, return values, exceptions |
| **Integration** | Aggregate + persistence | Aggregate via repository, test DB | A command through the aggregate root | Events emitted, state persisted, invariants held |
| **Acceptance (BDD)** | Full bounded context | Application service, test doubles | A use case through the API/entry point | End-to-end behavior matching BDD examples |

---

## Discovery Flow — DDD Strategic Phase

```
Stakeholder Interview ──► Event Storming ──► Language Definition ──► Domain Modeling ──► Scope Boundary
         │          ↑            ↑                  │                      │          ↑
         │          │            └ needs_restorming─┘                      │          │
         ├── needs_full_discovery┘                                              │          │
         ├── needs_scope_only ──────────────────────────────────────────────┘          │
         ├── already_known ──► [complete]                                             │
         │                                                                           │
         └── needs_reinterview ◄─────────────── Domain Modeling ─────────────────────┘
```

| State | Owner | Input Artifacts | Edited Artifacts | Output Artifacts |
|---|---|---|---|---|
| **Stakeholder Interview** | PO | — | — | interview-notes/*.md#pain_points, interview-notes/*.md#business_goals, interview-notes/*.md#terms_to_define, interview-notes/*.md#quality_attributes |
| **Event Storming** | DE | interview-notes/*.md#pain_points, interview-notes/*.md#business_goals, interview-notes/*.md#terms_to_define | — | domain_model.md#event_map, domain_model.md#context_candidates, domain_model.md#aggregate_candidates |
| **Language Definition** | DE | interview-notes/*.md#terms_to_define, domain_model.md#event_map | — | glossary.md |
| **Domain Modeling** | DE | glossary.md, domain_model.md#event_map, domain_model.md#aggregate_candidates, domain_model.md#context_candidates | domain_model.md#bounded_contexts, domain_model.md#entities, domain_model.md#relationships, domain_model.md#aggregate_boundaries, domain_model.md#summary | — |
| **Scope Boundary** | PO | domain_model.md#bounded_contexts, domain_model.md#aggregate_boundaries, domain_model.md#context_candidates, domain_model.md#summary, glossary.md | — | product_definition.md#what_is, product_definition.md#what_is_not, product_definition.md#why, product_definition.md#users, product_definition.md#out_of_scope, product_definition.md#delivery_order, product_definition.md#quality_attributes, product_definition.md#deployment |

**Routing from Stakeholder Interview:**
- `needs_full_discovery` → Event Storming (new domain/concept)
- `needs_scope_only` → Scope Boundary (domain understood, scope new work)
- `already_known` → complete (no discovery needed)

**Iteration loops:**
- Event Storming → `needs_reinterview` → Stakeholder Interview (workshop reveals gaps)
- Language Definition → `needs_restorming` → Event Storming (language contradicts event map)
- Domain Modeling → `contradiction_found` → Language Definition (model contradicts language)
- Domain Modeling → `needs_reinterview` → Stakeholder Interview (model reveals missing domain knowledge)
- Scope Boundary → `needs_reinterview` → Stakeholder Interview (scope questions reveal missing requirements)

**Why this order?** Event Storming (Brandolini) is an exploratory technique that surfaces domain events, commands, and aggregate *candidates* — it comes before formal modeling. Language Definition formalizes the ubiquitous language from interviews + event storming terms — it comes before the domain model because the model is *expressed in* the ubiquitous language. Domain Modeling then formalizes the candidates into proper entities, invariants, and aggregate boundaries using glossary terms.

**domain_model.md is an evolving document:** Event Storming fills the Event Map, Aggregate Candidates, and Context Candidates sections (workshop draft). Domain Modeling then formalizes these into the Bounded Contexts, Entities, Relationships, and Aggregate Boundaries sections. Both steps edit the same document — no separate event storming artifact needed.

**Carried forward to Architecture Flow:** glossary.md, domain_model.md, product_definition.md

---

## Architecture Flow — DDD Tactical + Technical Design

```
Architecture Assessment ──► no_architecture_needed ──► [complete] (when architecture_exists)
      │
      ├── needs_context_update ──► Context Mapping ──► Technical Design ──┐
      │                               │                                    │
      │                               └── needs_discovery                  │
      ├── needs_technical_design ──────────────────────────────────────►  │
      │                                         │ needs_decisions        │
      │                                         └──► ADR Draft ─────────►│
      │                                                                  ▼
      └── needs_discovery ──► [needs_discovery]           Review & Sign-off
                                                               │
                                                               └── inconsistent ──► Architecture Assessment
```

| State | Owner | Input Artifacts | Edited Artifacts | Output Artifacts |
|---|---|---|---|---|
| **Architecture Assessment** | SA | product_definition.md#what_is, product_definition.md#delivery_order, product_definition.md#deployment, product_definition.md#quality_attributes, domain_model.md#bounded_contexts, domain_model.md#summary, system.md, technical_design.md, context_map.md | product_definition.md#deployment* | — |
| **Context Mapping** | SA | domain_model.md#bounded_contexts, domain_model.md#context_candidates, product_definition.md#what_is, product_definition.md#what_is_not, product_definition.md#out_of_scope, glossary.md | — | context_map.md#context_relationships, context_map.md#context_map_diagram, context_map.md#integration_points, context_map.md#anti_corruption_layers |
| **Technical Design** | SA | context_map.md#context_relationships, context_map.md#integration_points, context_map.md#anti_corruption_layers, domain_model.md#entities, domain_model.md#relationships, domain_model.md#aggregate_boundaries, glossary.md, system.md, product_definition.md#what_is, product_definition.md#what_is_not, product_definition.md#out_of_scope, product_definition.md#deployment, product_definition.md#quality_attributes | technical_design.md#architectural_style, technical_design.md#quality_attributes, technical_design.md#stack, technical_design.md#module_structure, technical_design.md#api_contracts, technical_design.md#event_contracts, technical_design.md#interface_definitions, technical_design.md#c4_diagrams, technical_design.md#dependencies, technical_design.md#configuration_keys, system.md#context, system.md#container, system.md#module_structure, system.md#delivery | — |
| **ADR Draft** | SA | technical_design.md#architectural_style, technical_design.md#quality_attributes, technical_design.md#stack, technical_design.md#module_structure, context_map.md#context_relationships, domain_model.md#bounded_contexts, domain_model.md#aggregate_boundaries, product_definition.md#what_is, product_definition.md#quality_attributes, glossary.md, system.md | system.md#key_decisions, system.md#active_constraints | adr/*.md |
| **Review & Sign-off** | R | context_map.md, technical_design.md, system.md, adr/*.md†, product_definition.md#what_is, product_definition.md#what_is_not, product_definition.md#quality_attributes, domain_model.md#bounded_contexts, domain_model.md#aggregate_boundaries, glossary.md | — | — |

**Routing from Architecture Assessment:**
- `no_architecture_needed` → complete (when `architecture_exists`: system_md, technical_design_md, context_map_md all exist — feature fits existing architecture)
- `needs_technical_design` → Technical Design (new API contracts, modules, or interfaces)
- `needs_context_update` → Context Mapping (when `architecture_exists` — bounded context boundaries change, but base architecture exists)
- `needs_discovery` → needs_discovery exit (domain model insufficient)

**Routing from Context Mapping:**
- `done` → Technical Design (context boundaries updated, contracts must be verified)
- `needs_discovery` → needs_discovery exit (bounded contexts in domain_model.md don't hold up under mapping)

**Routing from Technical Design:**
- `done` → Review & Sign-off (no significant decisions needed)
- `needs_decisions` → ADR Draft (architecturally significant choice required)

**Why assessment first?** Most features fit the existing architecture. Forcing context mapping and technical design for every feature is wasteful. SA assesses the feature against existing architecture and only does the work that's needed. This also gives SA a chance to interview the stakeholder about technical constraints (deployment target, infrastructure preferences) before making architectural decisions.

**First-run safety (architecture_exists guard):** The `no_architecture_needed` and `needs_context_update` routes are guarded by the `architecture_exists` condition, which checks that system.md, technical_design.md, and context_map.md all exist. This prevents accidentally skipping architecture on a project's first feature where these artifacts don't yet exist.

**Why is ADR conditional?** ADRs record architecturally significant decisions — most features don't involve such decisions. Forcing an ADR per feature creates noise. When SA discovers a decision is needed during technical design, they route to ADR Draft. Otherwise they skip it.

**Why does ADR Draft edit system.md?** system.md is the living reference for the current system state. ADR summaries (key decisions) and risk constraints (active constraints) belong there so that R can verify implementation against them during Review Gate, and so that future SA assessments have a concise summary of architectural decisions without reading every ADR.

**Dual ownership of product_definition.md#deployment\***: PO sets an initial deployment preference during Discovery (Scope Boundary). SA may override it during Architecture Assessment when technical constraints demand a different mechanism. SA has final say — deployment mechanism is an architectural decision, not a business preference.

**Routing from Review & Sign-off:**
- `approved` → complete (all documents consistent and aligned)
- `inconsistent` → Architecture Assessment (documents contradict each other — SA must re-examine)
- `needs_discovery` → needs_discovery exit (domain model insufficient)

**Reconciliation (explicit in review-signoff):** R verifies cross-document consistency before approving:
- technical_design.md ↔ domain_model.md (module structure matches bounded contexts; API contracts match entities)
- technical_design.md ↔ product_definition.md (out-of-scope items not in design; quality attributes addressed)
- technical_design.md ↔ glossary.md (terms in contracts match ubiquitous language)
- context_map.md ↔ domain_model.md (integration points match context boundaries)
- adr/*.md ↔ technical_design.md (ADRs consistent with actual design)

**Conditional input †**: Review & Sign-off lists `adr/*.md` as input, but ADRs may not exist when Technical Design routes directly to Review & Sign-off (no `needs_decisions`). R reads whatever ADRs exist — zero ADRs is valid.

**needs_discovery from different sources**: Both Assessment and Context Mapping can exit with `needs_discovery`. Assessment triggers it when the domain model is insufficient to make architectural decisions. Context Mapping triggers it when bounded contexts don't hold up under relationship analysis. Review & Sign-off can also trigger `needs_discovery` when R finds architectural problems that stem from flawed discovery. All three route back to the full Discovery cycle — this is deliberate over-correction: partial discovery rework risks reintroducing the same gaps.

**inconsistent from Review & Sign-off**: When R finds that the architecture documents contradict each other (e.g., technical design uses terms not in the glossary, or context map doesn't align with domain model boundaries), the flow routes back to Architecture Assessment rather than Discovery. The domain model may be fine — the problem is that the architecture doesn't consistently translate it.

**Carried forward to Feature Development Flow:** context_map.md, adr/*.md, technical_design.md, system.md

---

## Planning Flow — BDD Story Definition

```
Feature Selection → Feature Specification → Feature Breakdown → BDD Features → Definition of Done → Ready
        │                    │                      ↑                  ↑
        │                    └ needs_architecture───┘                  │
        │                                          └ needs_respecification─┘
        │
        └ no_features → [completed]
```

| State | Owner | Input Artifacts | Edited Artifacts | Output Artifacts |
|---|---|---|---|---|
| **Feature Selection** | PO | product_definition.md#what_is, product_definition.md#why, product_definition.md#delivery_order, technical_design.md#feature, technical_design.md#module_structure | — | — |
| **Feature Specification** | PO | product_definition.md#what_is, product_definition.md#users, product_definition.md#quality_attributes, product_definition.md#out_of_scope, domain_model.md#bounded_contexts, domain_model.md#entities, domain_model.md#aggregate_boundaries, glossary.md, technical_design.md#api_contracts, technical_design.md#feature | — | interview-notes/*.md |
| **Feature Breakdown** | PO | product_definition.md#what_is, product_definition.md#why, product_definition.md#users, product_definition.md#delivery_order, technical_design.md#feature, technical_design.md#module_structure, interview-notes/*.md | — | feature_list |
| **BDD Features** | PO | feature_list, product_definition.md#what_is, product_definition.md#users, product_definition.md#quality_attributes, domain_model.md#entities, domain_model.md#aggregate_boundaries, glossary.md | — | features/<file>.feature |
| **Definition of Done** | PO | features/<file>.feature, product_definition.md#quality_attributes | product_definition.md#definition_of_done | — |
| **Ready** | PO | features/<file>.feature, product_definition.md#definition_of_done | — | — |

**Exits:** `complete` → Development, `needs_architecture` → Architecture, `no_features` → Completed (no more features to develop)

**Why feature selection first?** Before planning a feature, PO must verify that the architecture covers it. If technical_design.md doesn't address the feature, Planning routes back to Architecture rather than proceeding with incomplete design.

**Why feature specification?** The initial stakeholder interview in Discovery covers domain understanding at scope level, not feature-level behavioral detail. Feature Specification is a targeted conversation about one feature's concrete behavior — behavioral rules, scenarios, and acceptance criteria — informed by domain constraints (domain_model.md, glossary.md) and technical contracts (technical_design.md#api_contracts).

**Key design principle:** BDD features are the **contract between Planning and Development**. Each example becomes:
1. A test specification (test body design)
2. The acceptance criteria (Acceptance validates against them)

Feature Specification fills the gap between Discovery's scope-level interview and feature-level behavioral detail. Feature Breakdown then decomposes the specified feature into stories. BDD features are written using both the breakdown and the specification interview notes.

**Feature file convention:** Flows work on one feature at a time. Artifact references use `features/<file>.feature` (singular placeholder), not `features/*.feature` (glob). The flow engine processes a single feature per cycle through the Feature Development loop.

**Iteration loops:** Feature Breakdown and BDD Features can route back to Feature Specification via `needs_respecification` when decomposition reveals that the specification was incomplete or inconsistent.

**Carried forward to Development Flow:** features/<file>.feature, product_definition.md (with DoD), feature_list, interview-notes/*.md

**Project convention (not per-feature):** Branch naming convention, PR template, merge policy are established once at project start and referenced from product_definition.md, not repeated each planning cycle. Trunk-based: short-lived feature branches from trunk, PR before merge.

---

## Development Flow — TDD Implementation

```
Project Structuring → [TDD Cycle Flow] → [Review Gate Flow] → Commit
         ↑                    │                    │
         └── blocked ─────────┘                    │
         │                                         │
         └── needs_planning                        │
                                                   │
                              fail ────────────────┘
```

### Project Structuring (owned by SA)

| Step | What gets created | Source artifact | Output Artifacts |
|---|---|---|---|
| Package/module directories | Folder structure matching bounded context design | technical_design.md#module_structure | git_branch |
| `.py` stubs/signatures | Class names, typed attributes, method signatures, interfaces — **NO behavior** | domain_model.md#entities + domain_model.md#relationships + domain_model.md#bounded_contexts + glossary.md + technical_design.md#api_contracts + technical_design.md#interface_definitions + technical_design.md#dependencies + technical_design.md#configuration_keys + context_map.md#context_relationships + context_map.md#integration_points + context_map.md#anti_corruption_layers + adr/*.md + product_definition.md#quality_attributes | py_stubs |
| Test class stubs | One test file per `.feature` file, example function names as placeholders — **no fixtures/assertions** | features/<file>.feature | test_stubs |

**Why signatures before tests?** The `.py` stubs consolidate domain ideas into code structure. Test stubs then map `.feature` examples onto that structure. If signatures are wrong (don't match the domain), test bodies will couple to wrong abstractions — and refactoring both tests and implementation is expensive. Signatures are cheap to change; coupled tests are not.

### TDD Cycle Flow (separate flow, owned by SE)

| State | Owner | Input Artifacts | Edited Artifacts | Output Artifacts |
|---|---|---|---|---|
| **RED** | SE | test_stubs, py_stubs | — | test_bodies |
| **GREEN** | SE | test_bodies, py_stubs | — | function_bodies |
| **REFACTOR** | SE | function_bodies, test_bodies | function_bodies | refactored_code |

**Exits:** `all_green` → Review Gate, `blocked` → Project Structuring

### Review Gate Flow (separate flow, owned by R)

| State | Owner | Input Artifacts | Edited Artifacts | Output Artifacts |
|---|---|---|---|---|
| **Design Review** | R | domain_model.md#bounded_contexts, domain_model.md#entities, domain_model.md#aggregate_boundaries, glossary.md, technical_design.md#module_structure, technical_design.md#api_contracts, technical_design.md#event_contracts, context_map.md#context_relationships, system.md, product_definition.md#quality_attributes, adr/*.md, refactored_code | — | design_review_evidence |
| **Structure Review** | R | coverage_reports, test_output, refactored_code, features/<file>.feature, domain_model.md#entities, domain_model.md#aggregate_boundaries, glossary.md | — | structure_review_evidence |
| **Conventions Review** | R | linter_output, refactored_code, product_definition.md#project_conventions, glossary.md | — | conventions_review_evidence |

**Exits:** `pass` → Commit, `fail` → TDD Cycle

| Tier | Name | What R checks | Evidence sources | Fail routes SE to |
|---|---|---|---|---|
| **1** | **Design** | Domain alignment, DDD patterns, ubiquitous language, architecture compliance, priority order (YAGNI → DRY → KISS → OC → SOLID → Design Patterns) | R's judgment, domain_model.md#bounded_contexts, domain_model.md#entities, glossary.md, technical_design.md#module_structure, technical_design.md#api_contracts, context_map.md#context_relationships, system.md (key decisions + active constraints) | → REFACTOR (design is wrong — do not polish) |
| **2** | **Structure** | Test coverage, test coupling, BDD examples pass, missing test cases, behavior vs structure testing | Coverage reports, test runner output, R's judgment | → TDD Cycle (tests need work) |
| **3** | **Conventions** | Formatting, docstrings, type hints, import ordering, lint rules unrelated to design | Linter/formatter output, R's judgment | → quick surface fix |

**Why this order?** If Tier 1 fails, the design is wrong and will be restructured. Writing docstrings (Tier 3) for code that will be rewritten is pure waste. If Tier 2 fails, behavior is broken — no point formatting broken code. Tier 3 is cheap to fix but only worth it when design and behavior are stable.

**Key principle:** R uses automated tools as **evidence**, not as a replacement for judgment. A linter passing doesn't mean R approves the structure. R might say "tests pass but they're testing implementation details, not behavior" — that's a Tier 2 judgment automation can't make.

### Commit (owned by SE)

| State | Owner | Input Artifacts | Edited Artifacts | Output Artifacts |
|---|---|---|---|---|
| **Commit** | SE | test_bodies, function_bodies, review_gate_evidence, features/<file>.feature | — | commits |

**Carried forward to Acceptance:** Feature branch (with all commits), test results, coverage report, example traceability

---

## Feature Development Flow — Feature-Level Loop

After Architecture completes, the project enters the feature development loop. Each feature goes through Planning → Development → Acceptance → PR Creation. After a feature is merged, the loop starts again for the next feature. Post-mortem routes back to Planning (most common root cause: specification issues), with an escalation path to Architecture when needed.

```
Planning ──► Development ──► Acceptance ──► PR Creation ──► [next-feature]
    │                          │      │          │
    │                          │      └ rejected─┤
    │                          │                 │
    └ needs_architecture       └ rejected  Post-mortem ──► Planning (replan)
    └ no_features ──► [completed]                    ├──► [needs_architecture]
                                                    └──► [cancelled]
```

**Exits:** `next-feature` → loop again, `needs_architecture` → Architecture (parent), `cancelled` → Cancelled (parent), `completed` → Completed (parent)

### Acceptance (owned by PO)

Technical review (design, structure, conventions) already happened in Development Flow's Review sub-step (owned by R). Acceptance is purely business validation by PO.

| State | Owner | Input Artifacts | Edited Artifacts | Output Artifacts |
|---|---|---|---|---|
| **Acceptance** | PO | features/<file>.feature, product_definition.md#quality_attributes, product_definition.md#definition_of_done | — | acceptance_evidence, approval_record |

**Transitions:** `approved` → PR Creation, `rejected` → Post-mortem

**Why no technical review here?** R already reviewed all three tiers (design, structure, conventions) during Development's Review sub-step. Acceptance is PO's domain: did we build the *right thing*, not did we build the *thing right*.

### PR Creation (owned by SE)

| State | Owner | Input Artifacts | Edited Artifacts | Output Artifacts |
|---|---|---|---|---|
| **PR Creation** | SE | commits, approval_record, features/<file>.feature | — | pull_request |

**Transitions:** `merged` → next-feature (when `ci_passes=true` + `no_changes_requested=true`), `rejected` → Post-mortem

---

## Post-mortem Flow — Failure Analysis

```
Root Cause Analysis ──► Document Findings ──► Extract Lessons ──► Action Items ──► Complete (→ Planning)
         │                                                                     │
         └── no_issues_found ──► No Action                                     ├──► needs_architecture (→ Architecture)
                                                                               └──► No Action (→ Cancelled)
```

| State | Owner | Input Artifacts | Edited Artifacts | Output Artifacts |
|---|---|---|---|---|
| **Root Cause Analysis** | R | — | — | root_cause |
| **Document Findings** | R | root_cause | — | post-mortem/PM_YYYYMMDD_<slug>.md#failed_at, post-mortem/PM_YYYYMMDD_<slug>.md#root_cause, post-mortem/PM_YYYYMMDD_<slug>.md#missed_gate |
| **Extract Lessons** | R | post-mortem/PM_YYYYMMDD_<slug>.md#root_cause, post-mortem/PM_YYYYMMDD_<slug>.md#missed_gate | post-mortem/PM_YYYYMMDD_<slug>.md#fix | — |
| **Action Items** | R | post-mortem/PM_YYYYMMDD_<slug>.md#fix | post-mortem/PM_YYYYMMDD_<slug>.md#restart_check | — |

**Exits:** `complete` → Planning (replan), `needs_architecture` → Architecture (architectural root cause), `no_action` → Cancelled

**Why route to Planning, not Architecture?** Most PR rejections are specification problems — the feature didn't match what was intended, or scenarios were incomplete. Routing through Architecture every time wastes a cycle for the common case. When the root cause is architectural (wrong bounded context boundaries, wrong technical design), the `needs_architecture` exit escalates to the parent flow.

---

## Document Registry — Complete Artifact List

### Living Documents (maintained throughout project)

| Document | Path | Owner | When Changed | Purpose |
|---|---|---|---|---|
| **interview-notes/*.md** | `docs/interview-notes/IN_YYYYMMDD_<slug>.md` | PO | Append-only per session (Discovery + Feature Specification) | Raw stakeholder Q&A, reconstruction source |
| **product_definition.md** | `docs/product_definition.md` | PO (SA overrides #deployment) | When scope changes | IS/IS NOT boundaries, out of scope, users, project conventions |
| **glossary.md** | `docs/glossary.md` | DE | When domain terms emerge or change | Ubiquitous language dictionary |
| **domain_model.md** | `docs/domain_model.md` | DE | When domain understanding evolves | Event map, aggregate/context candidates, bounded contexts, entities, relationships, aggregate boundaries. Evolving: Event Storming fills candidates, Domain Modeling formalizes them |
| **context_map.md** | `docs/context_map.md` | SA | When contexts or relationships change | DDD relationships: upstream/downstream, anti-corruption layers |
| **system.md** | `docs/system.md` | SA | When domain understanding changes (rare) | C4 context/container diagrams, module structure, domain model documentation |
| **technical_design.md** | `docs/technical_design.md` | SA | When stack/contracts change | Stack choices, API/event contracts, interface definitions |
| **adr/*.md** | `docs/adr/ADR_YYYYMMDD_<slug>.md` | SA | New decisions or status changes | Architecture decisions with risk assessment |
| **features/*.feature** | `docs/features/feature-name/feature-name.feature` | PO | When requirements change | BDD features in Gherkin format — the single thread of truth (flows process one `<file>.feature` at a time) |

### Intermediate Documents (produced, consumed, then archived)

| Document | Path | Owner | Purpose |
|---|---|---|---|
| **Feature list** | Directory structure of `docs/features/` | PO | Decomposed into .feature files, then becomes reference |

### Transient Artifacts (not maintained as documents)

| Artifact | Location | Purpose |
|---|---|---|
| **py_stubs** | `src/**/*.py` | Class signatures, typed attributes, interfaces — NO behavior |
| **test_stubs** | `tests/**/*.py` | Example function names as placeholders — no fixtures/assertions |
| **test_bodies** | `tests/**/*.py` | Executable specification |
| **function_bodies** | `src/**/*.py` | Production code |
| **CI pipeline results** | CI logs | Per-run output |
| **Coverage reports** | CI artifacts | Per-run metrics |

### Meta-Process Documents

| Document | Path | Owner | When Created | Purpose |
|---|---|---|---|---|
| **post-mortem/*.md** | `docs/post-mortem/PM_YYYYMMDD_<slug>.md` | R | When PR is rejected | Root cause analysis, lessons, action items |

### Process Support Files (`.opencode/`)

These files are the meta-process infrastructure, not project artifacts. They guide how the flows are executed.

| Type | Path | Loaded When | Purpose |
|---|---|---|---|
| **Navigation** | `AGENTS.md` (project root) | Every session | Where files live, wikilink resolution, discovery commands |
| **Agent identity** | `.opencode/agents/{role}.md` | When role invoked | Who I am, what I decide |
| **Skill procedure** | `.opencode/skills/{skill}/SKILL.md` | On demand | Step-by-step instructions for a flow state |
| **Knowledge reference** | `.opencode/knowledge/{domain}/{concept}.md` | On demand, via wikilinks | What and why (progressive disclosure) |
| **Research notes** | `docs/research/{domain}/{concept}.md` | When knowledge file references them | Source material cited by knowledge files |

### File Structure Convention

- **Folders**: kebab-case (`interview-notes/`, `post-mortem/`)
- **Documents**: snake_case (`domain_model.md`, `product_definition.md`)
- **Features**: kebab-case folder + matching filename (`display-version/display-version.feature`)
- **Agents**: `.opencode/agents/{role}.md`
- **Skills**: `.opencode/skills/{skill}/SKILL.md`
- **Knowledge**: `.opencode/knowledge/{domain}/{concept}.md`
- **Research**: `docs/research/{domain}/{concept}.md`
- **ADRs**: `docs/adr/ADR_YYYYMMDD_{slug}.md`

---

## Consolidation Summary — What Flows Where

```
Discovery ──► interview-notes/*.md
           ──► domain_model.md#event_map + domain_model.md#context_candidates + domain_model.md#aggregate_candidates (from Event Storming)
           ──► glossary.md (from Language Definition, using interview-notes + domain_model.md#event_map)
           ──► domain_model.md#bounded_contexts + #entities + #relationships + #aggregate_boundaries (formalized by Domain Modeling)
           ──► product_definition.md#what_is + #what_is_not + #why + #users + #out_of_scope + #delivery_order + #quality_attributes + #deployment (from Scope Boundary)
                    │
                    ▼
Architecture ──► [Assessment: SA interviews stakeholder + decides routing; when guards prevent skipping on first run]
             ──► (no_architecture_needed, when architecture_exists) → skip to Feature Development
             ──► context_map.md#context_relationships + #context_map_diagram + #integration_points + #anti_corruption_layers (if context boundaries change)
              ──► technical_design.md#architectural_style + #quality_attributes + #stack + #module_structure + #api_contracts + #event_contracts + #interface_definitions + #c4_diagrams + #dependencies + #configuration_keys (edited by Technical Design)
              ──► system.md#context + #container + #module_structure + #delivery (edited by Technical Design)
             ──► adr/*.md (conditional — only when architecturally significant decision required)
             ──► system.md#key_decisions + #active_constraints (edited by ADR Draft)
                    │
                    ▼
Feature Development ──► [Feature-level loop: Planning → Development → Acceptance → PR Creation per feature]
                    │
                    ├── Planning ──► [Feature Selection: PO picks next feature, verifies architecture coverage; routes needs_architecture if gap found]
                    │             ──► interview-notes/*.md (from Feature Specification, using domain_model + glossary + technical_design#api_contracts)
                    │             ──► feature_list (from Feature Breakdown, using product_definition.md#what_is + #why + #users + #delivery_order + interview-notes/*.md)
                    │             ──► features/<file>.feature (from BDD Features, using feature_list + product_definition.md#what_is + #users + product_definition.md#quality_attributes + domain_model.md#entities + #aggregate_boundaries + glossary.md)
                    │             ──► product_definition.md#definition_of_done (edited by Definition of Done)
                    │             ──► no_features → Completed (project done)
                    │                    │
                    │                    ▼  (BDD features → test specifications AND acceptance criteria)
                    ├── Development ──► py_stubs + test_stubs + git_branch (from Project Structuring)
                    │              ──► [TDD Cycle Flow]: test_bodies (RED) → function_bodies (GREEN) → refactored_code (REFACTOR)
                    │              ──► [Review Gate Flow]: design_review_evidence → structure_review_evidence → conventions_review_evidence
                    │              ──► commits (from Commit)
                    │                    │
                    │                    ▼
                    ├── Acceptance ──► acceptance_evidence + approval_record (PO validates against BDD scenarios + quality attributes)
                    │                    │
                    │                    ▼
                    ├── PR Creation ──► merged (when ci_passes + no_changes_requested) → next-feature (loop)
                    │              ──► rejected → Post-mortem
                    │                    │
                    │                    ▼ (if rejected)
                    └── Post-mortem ──► root_cause → post-mortem#failed_at + #root_cause + #missed_gate → #fix → #restart_check
                                   ──► complete → Planning (replan — most common: specification issues)
                                   ──► needs_architecture → Architecture (architectural root cause)
                                   ──► no_action → Cancelled
```

The **BDD feature is the single thread of truth** — written in Planning (PO), used as test spec in TDD Cycle Flow (RED), validated in Acceptance (PO), and traced in PR Creation (release notes reference which examples were delivered).

The **Review Gate Flow ensures design issues are caught before conventions investment** — fail-fast, shift-left, tier by tier (Design → Structure → Conventions). Never invest in Tier 3 work on code that hasn't passed Tier 1. R reviews ALL three tiers and reports categorized findings to SE.

The **artifact chain ensures each translation is validated before the next level of detail is invested** — scope → features → signatures → test stubs → test bodies → function bodies. The Review Gate Flow checks these artifacts, not creates new ones.

The **"cannot review own work" principle prevents conflicts of interest** — Architecture Review & Sign-off (R verifies SA's architecture before implementation), Review Gate Flow (R verifies SE's implementation across all three tiers, cannot be same person as SE). Acceptance (PO) is purely business validation, not technical review.
