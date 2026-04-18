# Changelog

All notable changes to this template will be documented in this file.

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
