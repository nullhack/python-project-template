# Changelog

All notable changes to this template will be documented in this file.

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
