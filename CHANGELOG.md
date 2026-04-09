# Changelog

All notable changes to this template will be documented in this file.

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
- **Developer Agent** - Main development agent with 7-phase TDD workflow
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
