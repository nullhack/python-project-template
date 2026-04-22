# Changelog

All notable changes to this template will be documented in this file.

## [v7.1.20260422] - Precise Hypatia - 2026-04-22

### Added

- **`docs/glossary.md`**: living glossary with five domain terms from `display-version`; append-only with supersession protocol (#107)
- **`docs/adr/`**: two concrete ADRs (`version-source`, `verbosity-validation`) cross-referenced in `system.md` (#107)

### Changed

- **`docs/system.md`**: full rewrite — Summary, Actors, Structure, Key Decisions, External Dependencies, Active Constraints, Domain Model (Entities, Actions, Relationships), C4 Context Mermaid, C4 Container Mermaid, ADR Index, Completed Features; domain actions renamed from "Verbs" to "Actions" (#107)
- **`docs/discovery.md`**, **`docs/scope_journal.md`**: concrete session entries replacing placeholder text; grounded in `display-version` feature (#107)
- **`docs/index.html`**: "Context Diagram" card → "C4 Diagrams" linking `system.md#context` (#107)
- **Workflow and skill improvements**: AGENTS.md, FLOW.md, agent files, and multiple skills updated (architect, define-scope, implement, run-session, select-feature, update-docs, verify, git-release, create-skill) (#107)

### Removed

- **`docs/context.md`**, **`docs/container.md`**: deleted — C4 Context and Container diagrams are now `## Context` and `## Container` sections inside `system.md`, owned by SA (#107)
- **`domain-model.md.template`** (implement skill): removed — domain model is a section of `system.md`, not a separate file (#107)

---

## [v7.0.20260422] - Mighty Titan - 2026-04-22

### Added
- **PyPI publishing pipeline**: `.github/workflows/tag-release.yml` auto-tags on `pyproject.toml` version bump; `.github/workflows/pypi-publish.yml` builds, publishes via OIDC trusted publisher, and creates a GitHub Release (#100)
- **FLOW.md state machine**: replaces `TODO.md` — static workflow state machine with auto-detection rules, prerequisites table, and session log (#100)
- **WORK.md dynamic tracker**: active work items with `@id`, `@state`, `@branch`; append-only session log (#100)
- **`flow` skill**: full state machine design protocol, FLOW/WORK templates, recovery from interruption (#100)
- **`version-control` skill**: Git safety rules, branch lifecycle, commit hygiene, `--no-ff` merge protocol, post-mortem branches (#100)
- **`architect` skill**: Step 2 architecture protocol split from `implement` (#100)
- **System Architect agent** (`system-architect.md`): owns Step 2 (architecture) and Step 4 (adversarial review) — closed SA→SE→SA loop (#100)
- **Post-mortem protocol**: compact post-mortem template, `fix/<stem>` branch from original start commit, `define-scope` post-mortem workflow (#100)
- **Research library**: arc42, Google design docs, RFC/spec patterns, version-control references, Petri Nets, Statecharts, Session Types, Actor Model (entries 59–77) (#100)

### Changed
- **Project renamed to `temple8`**: `pyproject.toml`, README, `template-config.yaml`, `docs/index.html`, `setup-project` agent, git remote all updated (#100)
- **README rewritten**: audience-first structure for developers and PMs/POs; painpoint-led personas, delivery cycle, living documentation views, development standards — no arbitrary metrics tables (#100)
- **8-glyph in assets**: logo and banner SVG updated — `∞` in pediment replaced with `8` between the pillars (rotated 90°) (#100)
- **SA/SE role split**: `reviewer` agent absorbed into `system-architect`; SE owns Step 3 only; SA owns Steps 2 and 4 (#100)
- **`run-session` skill v5.0**: reads FLOW.md, detect-state protocol, branch verification, minimalist output discipline (#100)
- **`git-release` skill**: releases from `main` only guard; `ff-only` pull; release name from `docs/branding.md` (#100)
- **`create-pr` skill**: `--no-ff` merge; ownership moved to system-architect (#100)
- **Skill ownership**: `git-release` → stakeholder; `create-pr` → system-architect (#100)
- **`docs/index.html`**: 6-card landing page (system.md, context.md, features, API, coverage, research) (#100)
- **`docs/research/`**: renamed from `docs/scientific-research/`; new entries for architecture, documentation, version-control (#100)

### Removed
- **`TODO.md`**: superseded by `FLOW.md` + `WORK.md` (#100)
- **`.dockerignore`**: removed (#100)
- **`docs/architecture.md`**: superseded by `docs/system.md` + `docs/adr/` (#100)
- **`reviewer` agent**: absorbed into `system-architect` (#100)

## [v6.4.20260420] - Minimal Prometheus - 2026-04-20

### Added
- **Branding system**: `docs/branding.md` — project identity, colour palette, release naming convention, and wording guidelines; agents read this file to personalise release names, C4 diagram colours, and docs without touching `.opencode/` (#89)
- **Designer agent** (`designer.md`): owns `docs/branding.md` and `docs/assets/`; uses `design-colors` and `design-assets` skills (#89)
- **`design-colors` skill**: step-by-step colour palette selection with WCAG 2.1 AA 4.5:1 contrast validation; Itten/Albers colour theory embedded inline (#89)
- **`design-assets` skill**: SVG banner and logo creation workflow; W3C SVG 2 spec and WCAG 1.1.1 `aria-label` requirements embedded (#89)
- **`setup-project` Step 6 Branding**: collects tagline, mission, vision, tone, theme, and colours; suggests WCAG-validated palettes when user provides a theme but no colours; writes `docs/branding.md` (#89)
- **Output Style + Rule #8** in `run-session` skill: minimalist output discipline — signal only, no tool narration, session ends with `Next:` line (#89)

### Changed
- **Skill renames to verb-noun convention**: `session-workflow → run-session`, `scope → define-scope`, `implementation → implement`, `feature-selection → select-feature`, `living-docs → update-docs`, `pr-management → create-pr`, `design-patterns → apply-patterns`, `code-quality → check-quality` — all references updated across agents, skills, and `AGENTS.md` (#89)
- **`docs/images/` → `docs/assets/`**: asset directory renamed; `README.md` path updated (#89)
- **`git-release` v1.1**: reads `docs/branding.md` for optional release naming and theme; release name omitted from commit/release title if convention is absent (#89)
- **`update-docs` skill**: reads `docs/branding.md` primary/accent colours to apply `%%{init:...}%%` theming to Mermaid C4 diagrams (#89)

## [v6.2.20260419] - Autonomous Stenella - 2026-04-19

### Added
- **pytest-beehave integration**: `@id` tags now auto-assigned to untagged `Example:` blocks on every `pytest` run; test stubs auto-generated from `.feature` files at Step 2 end — no manual ID generation or stub writing required (#78)
- **Self-declaration defense in depth**: all 25 items numbered 1–25 in `implementation/SKILL.md`; `verify/SKILL.md` now hard-gates on completeness (count must equal 25, sequence must be gapless) before item audit begins (#78)

### Changed
- **Naming convention**: `.feature` file paths now use `<feature-stem>` (kebab); test directories use `<feature_slug>` (underscore) — applied consistently across all skills, `AGENTS.md`, and docs (#78)
- **`conftest.py`**: removed manual `deprecated` marker skip hook — now owned entirely by pytest-beehave (#78)
- **`scope/SKILL.md`**: removed all manual `@id` generation instructions and `@id` uniqueness checklist items — assignment is automatic (#78)
- **`product-owner.md`**: removed `@id` from bug handling and gap-resolution table — PO writes `Example:` blocks only (#78)
- **README**: added "Why this template?" section; added `pytest-beehave` to tooling table; replaced static stub example with a two-part Gherkin-in → stub-out illustration (#78)
- **`verify/SKILL.md` report table**: expanded Self-Declaration Audit from 21 collapsed rows to 25 numbered rows matching the implementation template exactly (#78)

## [v6.1.20260419] - Contextual Ambystoma - 2026-04-19 (hotfix)

### Added
- **living-docs skill**: new PO skill for generating C4 architecture diagrams (`docs/c4/context.md`, `docs/c4/container.md`) and maintaining the living glossary (`docs/glossary.md`) after each feature acceptance (Step 5) or on stakeholder demand
- **docs/c4/**: new directory for C4 Level 1 (Context) and Level 2 (Container) Mermaid diagrams; placeholder `.gitkeep` added
- **docs/glossary.md**: new living glossary file owned by `living-docs` skill (PO); terms sourced from completed feature files, `docs/discovery.md` Domain Model, and `docs/architecture.md` decisions
- **Scientific research — documentation.md**: new file with 4 entries (#59–62): Ko et al. 2007 (information needs), Winters et al. 2020 (docs-as-code), Procida 2021 (Diátaxis framework), Allspaw 2012 (blameless post-mortems)
- **Scientific research — domain-modeling.md**: 6 new DDD entries (#63–68): Evans DDD Reference CC-BY, Fowler UbiquitousLanguage bliki, Fowler BoundedContext bliki, Vernon IDDD, Verraes "UL is not a glossary", Evans Whirlpool process
- **Scientific research — architecture.md**: 4 new entries (#55–58): Nygard ADRs, Kruchten 4+1 View Model, Brown C4 Model, Parnas information hiding

### Changed
- **discovery.md template**: `### Scope` section renamed to `### Context` — the section is a session-level general-context synthesis, not a complete project scope definition
- **scope/SKILL.md**: updated `### Scope` references to `### Context` in Step C instructions and template block
- **living-docs/SKILL.md**: glossary entry format updated — `**Context:**` renamed to `**Bounded context:**` (mandatory for multi-context projects); `Domain Event` added as a distinct Type value; secondary-artifact note added to preamble; source-traceability rule replaces "do not invent" rule; checklist updated accordingly
- **implementation/SKILL.md**: Step 2 Read Phase now includes `docs/glossary.md` as item 2 — SE reads existing domain terms before naming classes, methods, and modules to avoid inventing synonyms
- **create-skill/SKILL.md**: `living-docs` added to available skills table
- **AGENTS.md**: skills table updated with `living-docs`; filesystem structure section updated (`docs/c4/`, `docs/glossary.md` added; `docs/architecture/` subtree removed; TODO.md reference updated)

### Removed
- **docs/architecture/**: folder deleted; the ADR log lives at `docs/architecture.md` (SE-owned); the old `adr-template.md` inside the folder was redundant
- **docs/workflow.md**: deleted; canonical workflow reference is `AGENTS.md` and the skills under `.opencode/skills/`
- **Dockerfile / docker-compose.yml**: removed as unused template artifacts

## [v6.0.20260419] - Declarative Nautilus - 2026-04-19

### Added
- **PO Self-Declaration**: mandatory 11-claim checklist (INVEST I/V/S/T, observable Then, no impl details, entity coverage, distinct examples, unique IDs, pre-mortem, scope boundary) written into TODO.md at end of Stage 2 Step B before criteria commit; every DISAGREE is a hard blocker (#71)
- **Reviewer Stance Declaration**: 5-claim block (adversarial mindset, manual trace, boundary check, semantic read, independence) added to verify/SKILL.md report template before APPROVED/REJECTED verdict; DISAGREE allowed with explanation, unexplained DISAGREE = REJECTED (#71)
- **session-workflow**: Step 1 Stage 2 Criteria TODO format section with full Self-Declaration template and Rule 9 enforcing the declaration before criteria commit (#71)
- **Three append-only project docs**: `docs/discovery_journal.md` (raw Q&A), `docs/discovery.md` (synthesis changelog), `docs/architecture.md` (architectural decisions) replace the old flat `docs/features/discovery.md` (#70)

### Changed
- **Discovery model** (breaking): Phase 1 / Phase 2 / Phase 3 / Phase 4 replaced by 2-stage model — Stage 1 Discovery (unified iterative sessions, PO + stakeholder) and Stage 2 Specification (PO alone, per BASELINED feature) (#70)
- **Feature file moves** (breaking): PO is now the sole owner of all `.feature` file moves (backlog → in-progress and in-progress → completed); SE and reviewer explicitly prohibited from moving files with clear escalation protocol (#70)
- **Session protocol**: discovery journal sessions use `Status: IN-PROGRESS` / `Status: COMPLETE` markers; real-time split rule (>2 concerns or >8 candidate Examples splits within the same session); journal writes only answered Q&A in groups (#70)
- **Bug handling**: explicit protocol — PO adds `@bug @id` Example, SE writes both the `@id` test in `tests/features/` and a `@given` Hypothesis property test in `tests/unit/`; both required (#70)
- **scope/SKILL.md**: full rewrite to 2-stage model with session start checklist, question order (general → cross-cutting → per-feature), after-questions steps, baselining section, and bug handling section (#70)
- **feature-selection/SKILL.md**: updated "Phase 4 (Criteria)" reference to "Stage 2 Step B (Criteria)" (#70)
- **All agent files and skills**: updated to reflect new document model, terminology, and chain of responsibility (#70, #71)

## [v5.2.20260418] - Emergent Colugo - 2026-04-18 (hotfix)

### Fixed
- **Role naming**: Replaced stale `developer` agent-role references with `software-engineer` in `implementation/SKILL.md`, `docs/scientific-research/ai-agents.md`, `docs/scientific-research/cognitive-science.md`, and `docs/features/completed/display-version.feature`
- **session-workflow**: Replaced hardcoded agent names in `## Next` line examples with `@<agent-name>` placeholders; added note pointing to `AGENTS.md` as source of truth; added missing Step 2 (Architecture) example

## [v5.1.20260418] - Emergent Colugo - 2026-04-18

### Added
- **refactor skill**: Standalone skill with Fowler's full catalogue, green-bar rule, two-hats rule, SOLID/OC self-declaration table, and preparatory refactoring protocol — loaded on demand at REFACTOR phase
- **feature-selection skill**: WSJF-based backlog prioritisation (Reinertsen 2009) with Kano value scoring and dependency gate — PO loads this when `TODO.md` is idle
- **ADR template**: `docs/architecture/adr-template.md` for Step 2 architectural decisions
- **Logo and banner**: visual identity added to README (SVG assets in `docs/images/`)

### Changed
- **Architecture stubs**: Step 2 now writes stubs directly into `<package>/` instead of an Architecture section in the feature file; stubs have no docstrings (add after GREEN when lint enforces them); folder structure is suggested, not prescribed — `ports/` and `adapters/` only created when a concrete external dependency is confirmed
- **design-patterns skill**: Narrowed to pure GoF catalogue (23 patterns, smell-triggered before/after examples); SOLID, OC, LoD, CQS, Python Zen moved to refactor skill self-declaration checklist
- **session-workflow**: `Next` line in TODO.md now requires `Run @<agent-name>` prefix so the human always knows which agent to invoke; idle state loads `skill feature-selection` instead of a vague prompt
- **verify skill**: Added orphaned-stub check (skip-marked tests that were never implemented); report template now includes structured `Next Steps` block directing the human to the correct agent
- **Scientific research**: `docs/academic_research.md` split into 9 domain files under `docs/scientific-research/` (cognitive-science, testing, architecture, oop-design, refactoring-empirical, requirements-elicitation, domain-modeling, software-economics, ai-agents)

### Fixed
- Stale `docs/architecture/STEP2-ARCH.md` reference removed from workflow diagram and skill
- Protocol smell-check gate now marked N/A when no external dependencies are identified in scope

## [v5.0.20260418] - Structured Phascolarctos - 2026-04-18

### Added
- **design-patterns skill**: Full GoF pattern catalogue with smell-triggered patterns, SOLID, Object Calisthenics, Python Zen, Law of Demeter, CQS, Tell Don't Ask — loaded on demand at Steps 2-3
- **create-agent skill**: Research-backed agent creation guide with OpenAI/Anthropic best practices, ownership boundaries, tool surface design, and escalation rules
- **software-engineer agent**: Dedicated agent file replacing `developer.md`; owns Steps 2-3 and release
- **3-session discovery structure**: Phase 1 and Phase 2 now each use a 3-session template with template gates (§1/§2/§3 must be confirmed before proceeding); active listening protocol (3 levels) codified in scope skill

### Changed
- **5-step workflow** (breaking): Steps restructured — TDD loop merged into Step 3, Verify is Step 4, Accept is Step 5; all agents, skills, and docs updated to match
- **Behavior groups terminology**: "Cluster" renamed to "behavior group" throughout scope skill, AGENTS.md, workflow.md, and templates for clearer AI focus
- **Story candidates terminology**: Phase 3 now derives "story candidates" → `Rule:` blocks, removing ambiguity from the cluster-to-story mapping
- **Test stub format** (breaking): Stubs now use `@pytest.mark.skip(reason="not yet implemented")` instead of `raise NotImplementedError`; skip marker is removed when implementing in RED phase
- **Dropped `@pytest.mark.unit` and `@pytest.mark.integration`**: Only `@pytest.mark.slow` and `@pytest.mark.deprecated` remain; folder structure (`tests/features/` vs `tests/unit/`) encodes test type
- **BASELINED gate enforced**: PO may not move a feature to `in-progress/` unless its discovery section has `Status: BASELINED`; enforced in product-owner.md and session-workflow
- **tdd skill removed**: Replaced by implementation skill with inline TDD guidance
- **gen_test_stubs.py removed**: Script deleted along with tdd skill

### Fixed
- **pyproject.toml**: Removed broken `gen-tests` task; removed `raise NotImplementedError` from coverage exclusions; removed `unit`/`integration` marker definitions
- **Role naming**: `developer` → `software-engineer` across all files
- **Step count**: All references to "6 steps" updated to "5 steps"

## [v4.1.20260416] - Recursive Acinonyx - 2026-04-16

### Added
- **Single `.feature` file per feature**: Each feature is now one `.feature` file with `Rule:` blocks for user stories and `Example:` blocks for ACs — discovery content embedded in the feature description free text; replaces the folder-per-feature structure
- **Rule-scoped test files**: `gen_test_stubs.py` rewritten to parse `Rule:` blocks; each Rule maps to one test file (`<rule-slug>_test.py`); function naming is now `test_<rule_slug>_<id_hex>()`
- **Hypothesis-only `tests/unit/`**: Every test in `tests/unit/` must use `@given`; `@pytest.mark.slow` is mandatory on all Hypothesis tests; plain `assert` tests without `@given` are forbidden
- **Mandatory `## Self-Declaration` in TODO.md**: Developer writes the 21-item checklist into a `## Self-Declaration (@id:<hex>)` block in `TODO.md` at `SELF-DECLARE` phase before requesting reviewer check (Rule 8 in session-workflow)

### Changed
- **`gen_test_stubs.py`**: Scans `docs/features/{backlog,in-progress,completed}/*.feature` directly (not subfolders); generates one test file per `Rule:` block
- **`gen_todo.py`**: `find_in_progress_feature()` now finds `.feature` files directly in `in-progress/`; source path is `docs/features/in-progress/<name>.feature`
- **`skills/tdd/SKILL.md`**: Test Tool Decision table updated to separate `tests/features/` (plain pytest, generated) from `tests/unit/` (Hypothesis only); `tests/unit/` rules section added
- **`skills/implementation/SKILL.md`**: Unit test rule tightened — `@given` required, `@pytest.mark.slow` mandatory, plain tests forbidden
- **`skills/verify/SKILL.md`**: Two new rows in section 4f: `@given` check and `@slow` check; two new rows in Standards Summary
- **`skills/scope/SKILL.md`**: All four phases rewritten for file-based workflow; `discovery-template.md` converted to `.feature` file template
- **`skills/session-workflow/SKILL.md`**: Step 4 TODO format updated with mandatory `## Self-Declaration` block template; Rule 8 added
- **Completed feature migrated**: `docs/features/completed/display-version/` (three files) merged into `docs/features/completed/display-version.feature` (single file with two `Rule:` blocks)

### Fixed
- **OC-8 clarification**: The only valid fix for > 2 `self.x` is a new named class (Rule 3 or Rule 4); hardcoded constants, class-level variables, inlined literals, and parent-class moves are all invalid workarounds and remain FAIL

## [v4.0.20260416] - Precise Tarsius - 2026-04-16

### Added
- **Per-test Design Self-Declaration**: After REFACTOR, developer fills a 20-item checklist (YAGNI → KISS → DRY → SOLID-S/O/L/I/D → OC rules 1–9) with `file:line` evidence before requesting reviewer check; reviewer independently audits claims using an 11-row comparison table (#58)
- **Package Verification step**: Mandatory before writing any code — read `pyproject.toml → [tool.setuptools] packages`, confirm directory exists on disk; hard stop if missing (#58)
- **SELF-DECLARE phase**: New phase added to the Red-Green-Refactor cycle between REFACTOR and REVIEWER; Cycle State now `RED | GREEN | REFACTOR | SELF-DECLARE | REVIEWER(code-design) | COMMITTED` (#58)
- **template-config.yaml**: Declarative single source of truth for all setup-project substitutions — `defaults:` block with 6 parameters, `substitutions:` map with literal `old:` strings, `{variable}` `new:` patterns, and expected `count:` per file (#58)
- **Post-mortem docs**: Two ping-pong-cli post-mortems documenting the systemic failures that drove this release (#58)

### Changed
- **verify/SKILL.md Scope Guard**: Reviewer receives completed Design Self-Declaration and independently verifies each claim; responds using structured 11-row comparison table (#58)
- **verify/SKILL.md section 4g**: New row — `Imports use correct package name` (check imports match `[tool.setuptools] packages`); existing rows made more precise with `pyproject.toml` references (#58)
- **reviewer.md per-test Step 4 section**: Rewritten to reference `skill implementation` verification table; clarifies no commands run during Step 4 reviews (#58)
- **reviewer.md Zero-Tolerance Rule 1**: Scoped to `(Step 5 only — per-test Step 4 checks are code-design only, no commands)` (#58)
- **setup-project.md**: Reads `template-config.yaml`; each apply step delegates to the config map rather than carrying implicit pattern knowledge (#58)
- **Template app simplified**: `app/version.py` deleted; `app/__main__.py` reduced from 41 to 23 lines (#58)

### Fixed
- **gen_todo.py path**: `parents[5]` → `parents[4]` — was resolving one directory above the project root (#58)
- **session-workflow Cycle State**: `SELF-DECLARE` phase added to documented phase list and Rule 6 (#58)
- **code-quality/SKILL.md**: Removed "has been absorbed" migration language (#58)
- **Dockerfile stale references**: `python_package_template.python_module_template` → `app` in HEALTHCHECK and CMD (#58)
- **docker-compose.yml stale references**: `python_package_template` → `app` in volume mounts and command (#58)

### Breaking Changes
- `project_defaults.json` deleted — replaced by `template-config.yaml` (#58)
- `app/version.py` and `tests/version_test.py` deleted — template app simplified to minimal `__main__.py` + one Hypothesis unit test (#58)

## [v3.2.20260415] - Vigilant Mantis - 2026-04-15

### Added
- **Adversarial verification mandate**: Reviewer's default hypothesis is now "the code is broken despite green checks" — job is to find the failure mode, not confirm it works (#54)
- **Production-grade gate**: New step 3 in verification — app must exit cleanly AND output must change when input changes; static output regardless of input = REJECTED (#54)
- **UUID Drift bash check**: One-liner detects duplicate UUIDs across test functions; any duplicate = REJECTED with fix instructions (#54)
- **docs/academic_research.md**: 15 cognitive and social science mechanisms with full citations grounding every workflow design decision (pre-mortem, implementation intentions, adversarial collaboration, elaborative encoding, and 11 more) (#54)
- **Design pattern decision table**: Added to `developer.md` and `implementation/SKILL.md`; any detected anti-pattern = REJECTED (#54)
- **Architecture contradiction check**: Developer must cross-check ADRs against ACs before writing production code (#54)
- **PO pre-mortem**: Added at scope step and acceptance step (#54)
- **Semantic alignment rule**: Tests must operate at same abstraction level as AC (#54)
- **Integration test requirement**: Multi-component features require at least one integration test through the public entry point (#54)
- **Verification Philosophy section**: Added to AGENTS.md — automated checks verify syntax-level correctness; human review verifies semantic-level correctness; both required (#54)

### Changed
- **Verification order**: Code review before automated commands; run app first as production-grade gate (#54)
- **All review sections converted to tables**: Correctness, KISS, SOLID, ObjCal, Design Patterns, Tests, Versions/Build all have PASS/FAIL/Fix columns (#54)
- **UUID Uniqueness rule**: If only Given varies it is a property — use Hypothesis `@given` + `@example`, not multiple test functions; if When/Then differs use `extend-criteria` (#54)
- **Production-grade self-check in implementation**: Developer must verify output changes with input before handoff (#54)

## [v3.1.20260414] - Tidal Capybara - 2026-04-14

### Added
- **extend-criteria skill**: New skill for any agent to add acceptance criteria discovered mid-flight or post-merge, with decision rule (gap within scope vs. new feature), per-role procedures, and commit protocol
- **Source: field on acceptance criteria**: Mandatory traceability field on every criterion (`stakeholder | po | developer | reviewer | bug`) — records who originated the requirement

### Changed
- **Test function naming**: `test_<short_title>` replaces `test_<condition>_should_<outcome>`
- **Test docstring first line**: UUID only (no trailing description) — `"""<uuid>\n\nGiven: ...`
- **development commands**: All skill and agent files now use `uv run task` consistently (not bare `task`)
- **tests/ layout**: Documented as flat (no unit/ or integration/ subdirectories)
- **pytest.skip prohibition**: Aligned across files — allowed with written justification in the docstring
- **Marker decision table**: Moved to tdd/SKILL.md only (developer's decision, not PO's)
- **mv to in-progress**: Ownership reassigned to developer Step 2 (not PO scope step)
- **TODO.md status markers**: Added `[~]` (in progress) and `[-]` (cancelled) to documented legend
- **--doctest-modules**: Documented in implementation/SKILL.md (task test runs doctest modules)
- **verify/SKILL.md**: Report template uses flat `tests/<file>:<function>` path format
- **exit code wording**: `exit non-124` (was ambiguous `exit 0 or 124`) in developer.md
- **README.md**: `uv sync --all-extras` and `uv run task` commands throughout

### Fixed
- Removed stale `docs/features/in-progress/auto-publish-docs.md`
- Split compound acceptance criterion (two outcomes in one Then) into two single-outcome criteria
- Added `@pytest.mark.slow` to Hypothesis tests in reference implementation
- Added `# Given / # When / # Then` body comments to all reference tests
- Removed duplicate assertion from `test_version_logs_correct_message`
- Moved `StringIO` import from test body to module-level imports

## [v3.0.20260414] - Drifting Axolotl - 2026-04-14

### Breaking Changes
- **Workflow redesigned**: 8-phase/6-role system replaced with 6-step/3-role (Product Owner, Developer, Reviewer)
- **Roles removed**: architect, manager, repo-manager, requirements-gatherer, overseer agents deleted
- **Feature directories restructured**: `docs/features/{business,architecture}/` replaced with flat `docs/features/{backlog,in-progress,completed}/`

### Added
- **product-owner agent**: Defines scope, acceptance criteria, picks features, accepts deliveries (Steps 1 + 6)
- **reviewer agent**: Read+bash only, runs all commands, produces APPROVED/REJECTED report (Step 5)
- **scope skill**: PO guide for writing user stories + UUID acceptance criteria
- **verify skill**: Reviewer guide for running commands and code review checklist
- **Unified docs site**: `docs/index.html` landing page linking to API Reference, Coverage, Test Results
- **ghp-import**: One-liner `task doc-publish` replaces complex inline Python

### Changed
- **developer agent**: Owns all of Steps 2-4+6 including architecture, tests, code, and release
- **9 skills rewritten**: session-workflow, tdd, implementation, code-quality, pr-management, git-release, create-skill (lean, <150 lines each)
- **Test markers reduced**: from 11 (with duplicate) to 3: `unit`, `integration`, `slow`
- **doc-build**: Now generates all three outputs (pdoc API + pytest-cov HTML + pytest-html)
- **CI workflow**: Cleaned up to use `uv run task <name>` consistently
- **setup-project agent**: No longer uses setup_project.py; agent applies changes directly

### Removed
- 11 skills deleted (architectural-analysis, delegation-coordination, epic-workflow, feature-definition, qa-enforcement, requirements-management, signature-design, workflow-coordination, prototype-script, create-agent, reference/)
- `setup_project.py` script and `.opencode/templates/` directory
- Wrong `dotenv` dependency (replaced nothing — was unused)
- `mutmut` dev dependency (YAGNI)

## [v2.2.20260413] - Luminous Kestrel - 2026-04-13

### Added
- **Architecture-First Feature System** - New directory structure separating business and architecture features
- **Architectural Analysis Skill** - Systematic architecture documentation for each feature
- **8-Phase Development Cycle** - Expanded from 7-phase with dedicated Architecture Analysis phase

### Changed
- **BDD → Acceptance Criteria** - Renamed gherkin-validation to acceptance-criteria-validation for accurate terminology
- **Consistency Updates** - Fixed phase numbering, cross-references, and documentation across all agents and skills
- **Epic-Workflow Refactor** - Converted from epic-based to feature-selection with architecture-first priority
- **Manager Agent** - Enhanced with test signature creation capabilities

### Migration Notes
- No breaking changes in this release
- Projects can continue using existing workflow

## [v2.1.20260413] - Polished Gecko - 2026-04-13

### Added
- Docker simplification and cleanup
- V2 Development Workflow with CI/CD fixes
- Template refactoring for generic app package
- Enhanced QA enforcement skills

### Changed
- Complexity fixes for CI compliance
- CodeQL config conflict resolved

## [v2.0.20260411] - Armored Pangolin - 2026-04-11

### 🚀 MAJOR RELEASE - V1 → V2 Architecture Transition

This represents a fundamental architectural shift from V1 (template validation workflows) to V2 (project development workflows).

### Breaking Changes
- **Workflow Architecture**: Complete transition from template validation (V1) to project development (V2)
- **CI/CD Pipeline**: New comprehensive GitHub Actions workflow replacing template-specific workflows
- **Branch Structure**: V2/init becomes the new development foundation
- **Agent Configuration**: Updated agent roles and capabilities for project development

### Security Improvements
- Enhanced GitHub Actions workflow security with proper permissions blocks
- Removed risky PIP_USER environment variable from CI/CD pipeline
- Added secure error handling to shell scripts with 'set -euo pipefail'
- Implemented job-level permissions for all CI workflow operations

### Infrastructure & DevOps
- Modernized Docker setup with security-first containerization approach
- Comprehensive CI/CD pipeline with GitHub Actions integration
- Improved workflow security following GitHub Advanced Security recommendations
- Full project development workflow implementation

### Development Experience
- Complete project-focused development environment
- Better error handling and security practices in automation
- Enhanced development workflow with secure defaults
- Improved CI/CD reliability and security posture

### Migration Notes
- **BREAKING**: This is a major version requiring migration from V1 template workflows
- V1 template validation workflows are replaced by V2 project development workflows
- Projects using V1 should plan migration to V2 architecture
- All security improvements follow GitHub security best practices

## [v1.7.20260410] - Vivid Cardinal - 2026-04-10

### Added
- **QA-gated Epic Workflow** - Complete epic-based development with mandatory quality checkpoints at each phase
- **Epic-workflow Skill** - Manages epic-based development with automatic feature progression
- **EPICS.md Template** - Epic tracking and management file for generated projects

### Changed
- Updated all agent descriptions to use industry-standard roles (Development Lead, Software Architect, QA Specialist, Business Analyst, Release Engineer)
- Removed model specifications from all agents to make template model-agnostic
- Updated AGENTS.md to properly document all 5 generated project agents and all skills
- Updated README.md with new workflow and agent roles

### Fixed
- Documentation now accurately reflects what exists in template

## [v1.6.20260409] - Guardian Owl - 2026-04-09

### Added
- **Overseer Agent** - Quality assurance agent that reviews work after each test implementation and requests changes if needed
- **Requirements Gatherer Agent** - Agent that asks questions to understand project needs, updates documentation, creates detailed analysis for architect

### Changed
- Updated developer workflow to include `@overseer` calls after Phase 3 (TDD tests) and Phase 7 (Quality Assurance)
- Updated AGENTS.md with new agents and updated workflow examples

## [v1.0.0] - 2026-03-12

### Added
- **AI-Enhanced Development Workflow** - Complete OpenCode integration for AI-powered development
- **Developer Agent** - Main development agent with 8-phase TDD workflow
- **Architect Agent** - Design review agent for SOLID principles and object calisthenics compliance
- **Repository Manager Agent** - Git operations, PRs, and themed releases management
- **Development Skills** - feature-definition, prototype-script, tdd, signature-design, implementation, code-quality
- **Repository Skills** - git-release (hybrid calver versioning with themed releases), pr-management
- **Meta Skills** - create-skill, create-agent for extending OpenCode
- **Template Management** - template-manager agent, template-test, template-release skills
- **Comprehensive CI Workflow** - Template validation, generated project tests, Docker builds
- **Validation Scripts** - cookiecutter.json, pyproject.toml, YAML frontmatter validation

### Changed
- Updated README.md with modern AI-focused branding
- Updated generated project README template with AI development workflow

### Features
- **7-Phase Development Cycle**: Feature Definition → Prototype → TDD → Signature Design → Architecture Review → Implementation → Quality Assurance
- **SOLID Principles Enforcement** - Single responsibility, dependency inversion, interface segregation
- **Object Calisthenics** - No primitives, small classes, behavior-rich objects
- **Hybrid Calver Versioning**: v1.2.20260302 format with themed releases
- **Themed Release Names**: "Swift Cheetah", "Vigilant Owl", "Creative Fox" based on PR sentiment
- **Property-Based Testing**: Hypothesis integration for robust test coverage

### Migration Notes
- This is the first semantic version release
- No breaking changes to cookiecutter.json structure
- Generated projects now include OpenCode agents and skills
- Existing projects can regenerate to get new features
