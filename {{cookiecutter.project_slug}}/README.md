# {{cookiecutter.project_name}}

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![{{cookiecutter.license}} License][license-shield]][license-url]
[![Coverage](https://img.shields.io/badge/coverage-{{cookiecutter.minimum_coverage}}%25-brightgreen?style=for-the-badge)](docs/htmlcov/index.html)

> {{cookiecutter.project_short_description}}

**AI-Enhanced Python Project** built with enterprise-grade architecture, TDD/BDD workflows, and zero-config quality standards.

---

## ⚡ Quick Start

```bash
# Clone and setup
git clone https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}
cd {{cookiecutter.project_slug}}

# Install UV package manager (if not installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Initialize AI development environment
opencode && /init

# Setup development environment
uv venv && uv pip install -e '.[dev]'

# Validate everything works
task test && task lint && task static-check
```

## 🤖 AI-Powered Development

This project includes built-in AI agents to accelerate your development:

```bash
# Define new features with SOLID principles
@developer /skill feature-definition

# Create prototypes and validate concepts  
@developer /skill prototype-script

# Write comprehensive tests first (TDD)
@developer /skill tdd-bdd

# Get architecture review before implementing
@architect

# Implement with guided TDD workflow
@developer /skill implementation

# Create releases with smart versioning
@repo-manager /skill git-release
```

## 🏗️ Architecture & Standards

- **🎯 SOLID Principles** - Single responsibility, dependency inversion, clean interfaces
- **🔧 Object Calisthenics** - No primitives, small classes, behavior-rich objects
- **🧪 TDD/BDD Testing** - {{cookiecutter.minimum_coverage}}% coverage requirement with property-based tests
- **⚡ Modern Toolchain** - UV, Ruff, PyTest, Hypothesis, PyRight
- **🚀 Smart Releases** - Calver versioning with AI-generated themed names

## 📋 Development Commands

```bash
# Core development workflow
task run              # Execute main application
task test             # Run comprehensive test suite  
task lint             # Format and lint code
task static-check     # Type safety validation
task doc-serve        # Live documentation server

# Quality assurance
task test-report      # Detailed coverage report
task mut-report       # Mutation testing (optional)
task doc-publish      # Deploy documentation

# Container workflows
docker build --target test -t {{cookiecutter.package_name}}:test
docker build --target prod -t {{cookiecutter.package_name}}:prod
```

## 🎯 Project Structure

```
{{cookiecutter.project_slug}}/
├── {{cookiecutter.package_name}}/        # Main application package
│   ├── __init__.py                       # Package initialization
│   └── {{cookiecutter.module_name}}.py  # Core module
├── .opencode/                            # AI development agents
│   ├── agents/                           # Specialized AI agents
│   │   ├── developer.md                  # 7-phase development workflow
│   │   ├── architect.md                  # SOLID architecture review
│   │   └── repo-manager.md               # Release and PR management
│   └── skills/                           # Development skills
│       ├── feature-definition/           # Requirements planning
│       ├── tdd-bdd/                      # Test-driven development
│       ├── implementation/               # Guided implementation
│       └── code-quality/                 # Quality enforcement
├── tests/                                # Comprehensive test suite
├── docs/                                 # Documentation
├── Dockerfile                            # Multi-stage container build
└── pyproject.toml                        # Project configuration
```

## 🔧 Technology Stack

| Category | Tools |
|----------|-------|
| **Package Management** | UV (blazing fast pip/poetry replacement) |
| **Code Quality** | Ruff (linting + formatting), PyRight (type checking) |
| **Testing** | PyTest + Hypothesis (property-based testing) |
| **AI Integration** | OpenCode agents for development automation |
| **Documentation** | MkDocs with modern theme |
| **Containerization** | Docker with optimized multi-stage builds |

## 📈 Quality Metrics

- ✅ **{{cookiecutter.minimum_coverage}}% Test Coverage** - Comprehensive test suite including edge cases
- ✅ **Static Type Safety** - Full type hints with protocol-based interfaces  
- ✅ **Zero Linting Issues** - Automated formatting and style enforcement
- ✅ **Property-Based Testing** - Hypothesis for robust validation
- ✅ **Architecture Compliance** - AI-enforced SOLID principles

## 🚀 Deployment Ready

```bash
# Production container build
docker build --target prod -t {{cookiecutter.package_name}}:latest .
docker run {{cookiecutter.package_name}}:latest

# Documentation deployment  
task doc-publish  # Deploys to GitHub Pages

# Smart release management
@repo-manager /skill git-release
# Creates versioned release: v1.2.20240315r1 "Creative Fox"
```

## 🤝 Contributing

Built with AI-assisted development workflows:

```bash
# Start a new feature
@developer /skill feature-definition
@developer /skill prototype-script
@developer /skill tdd-bdd
@architect  # Architecture review
@developer /skill implementation
@repo-manager /skill pr-management
```

See [DEVELOPMENT_WORKFLOW.md](DEVELOPMENT_WORKFLOW.md) for the complete 7-phase development process.

## 📄 License

Distributed under the {{cookiecutter.license}} License. See [LICENSE](LICENSE) for details.

## 🙏 Built With

- [AI-Enhanced Python Template](https://github.com/nullhack/python-project-template) - Enterprise-grade Python project template
- [OpenCode](https://opencode.ai) - AI-powered development platform
- [UV](https://astral.sh/uv/) - Modern Python package manager
- [Ruff](https://astral.sh/ruff/) - Extremely fast Python linter

---

**Author:** {{cookiecutter.full_name}} ([@{{cookiecutter.github_username}}](https://github.com/{{cookiecutter.github_username}}))  
**Project:** [{{cookiecutter.project_slug}}](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}})  
**Documentation:** [{{cookiecutter.github_username}}.github.io/{{cookiecutter.project_slug}}](https://{{cookiecutter.github_username}}.github.io/{{cookiecutter.project_slug}})

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}.svg?style=for-the-badge
[contributors-url]: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}.svg?style=for-the-badge
[forks-url]: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/network/members
[stars-shield]: https://img.shields.io/github/stars/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}.svg?style=for-the-badge
[stars-url]: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/stargazers
[issues-shield]: https://img.shields.io/github/issues/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}.svg?style=for-the-badge
[issues-url]: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/issues
[license-shield]: https://img.shields.io/badge/license-{{cookiecutter.license}}-green?style=for-the-badge
[license-url]: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/blob/main/LICENSE