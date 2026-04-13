# Changelog

All notable changes to this template will be documented in this file.

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
