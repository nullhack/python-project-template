# 🚀 AI-Enhanced Python Project Template

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen?style=for-the-badge)](docs/coverage/index.html)

[![CI Status](https://github.com/nullhack/python-project-template/workflows/CI/badge.svg?style=for-the-badge)](https://github.com/nullhack/python-project-template/actions/workflows/ci.yml)
[![CodeQL](https://github.com/nullhack/python-project-template/workflows/CodeQL%20Security%20Analysis/badge.svg?style=for-the-badge)](https://github.com/nullhack/python-project-template/actions/workflows/codeql.yml)
[![Python](https://img.shields.io/badge/python-3.13-blue?style=for-the-badge)](https://www.python.org/downloads/)
[![Code Style](https://img.shields.io/badge/code%20style-ruff-000000.svg?style=for-the-badge)](https://github.com/astral-sh/ruff)
[![Security](https://img.shields.io/badge/security-ruff%20%2B%20CodeQL-green?style=for-the-badge)](https://docs.astral.sh/ruff/rules/#flake8-bandit-s)

> **Ship production-ready Python projects faster with AI-powered development workflows**

### Current Version: [v2.0.20260411 - Armored Pangolin](https://github.com/nullhack/python-project-template/releases/tag/v2.0.20260411)

**Modern Python template** delivering enterprise-grade projects with **OpenCode AI agents**, **TDD/BDD workflows**, and **intelligent development assistance**.

## ✨ What You Get

🤖 **Enterprise AI Development Team** - 5 specialized agents: Developer, Architect, Business Analyst, QA Specialist, Release Engineer  
🏗️ **SOLID Architecture** - Object Calisthenics, Dependency Inversion, Protocol-based design with architect review  
🎯 **Mandatory QA Gates** - 4 quality checkpoints enforced by QA specialist throughout development  
⚡ **Modern Development** - Fast uv package manager, pytest + Hypothesis testing, ruff linting  
🔒 **Security-First** - CodeQL analysis, vulnerability scanning, and security-focused workflows  
🔄 **Smart Releases** - Hybrid calver versioning with AI-generated themed names  
📋 **Epic-Based Workflow** - Requirements-driven development with automatic feature progression  
🛠️ **Simple Setup** - Clone, setup, OpenCode - start building immediately

## 🎯 Perfect For

- **Developers** wanting AI-assisted development with modern tooling
- **Teams** needing structured development workflows with quality gates
- **Projects** requiring comprehensive testing and quality assurance
- **Startups** wanting to build production-ready applications quickly
- **Anyone** seeking a modern Python development experience

## 🚀 Quick Start

### Simple 3-Step Setup

```bash
# 1. Clone the template
git clone https://github.com/nullhack/python-project-template.git your-project
cd your-project

# 2. Setup development environment (installs uv automatically if needed)
./setup.py  # Creates virtual environment and installs dependencies

# 3. Start AI-powered development
opencode
```

That's it! Your development environment is ready.

### Start Building with AI Agents

```bash
# In OpenCode, gather requirements first
@requirements-gatherer  # Interviews stakeholders, analyzes needs

# Then start structured development 
@developer /skill epic-workflow start-epic "Your Feature Name"

# Or jump straight into feature development
@developer /skill feature-definition
@developer /skill tdd
@developer /skill implementation
```

## 🛠️ Development Workflow

### Daily Commands

```bash
# Run your application
task run

# Test suite (fast tests + coverage)
task test

# Code quality checks
task lint              # Ruff linting and formatting
task static-check      # Type checking with pyright

# Documentation
task doc-serve         # Live documentation server
task doc-build         # Build static docs

# Development utilities
task test-fast         # Quick tests (skip slow ones)
task test-slow         # Integration tests only
```

### Quality Assurance

The template enforces high standards automatically:
- **100% Test Coverage** - Comprehensive testing with pytest + hypothesis
- **Type Safety** - Full type annotations with pyright checking
- **Code Quality** - Ruff linting with security rules (flake8-bandit)
- **Security** - CodeQL analysis and vulnerability scanning
- **Documentation** - Auto-generated API docs with pdoc

## 🏛️ Architecture & Workflow

### Epic-Based Development with Mandatory QA Gates

1. **Requirements Gathering** → `@requirements-gatherer` conducts stakeholder interviews using BABOK methodology
2. **🔒 QA Gate #1** → `@overseer` enforces requirements completeness review  
3. **Test-Driven Development** → `@developer /skill tdd` creates BDD-style tests with pytest + Hypothesis
4. **🔒 QA Gate #2** → `@overseer` reviews test quality and coverage standards
5. **Design & Architecture** → `@architect` ensures SOLID patterns and design review  
6. **Implementation** → `@developer /skill implementation` follows TDD Red-Green-Refactor cycle
7. **🔒 QA Gate #3** → `@overseer` validates SOLID/DRY/KISS compliance  
8. **Final Quality** → `@developer /skill code-quality` runs comprehensive quality checks
9. **🔒 QA Gate #4** → `@overseer` provides final approval before feature completion
10. **Automatic Progression** → System advances to next feature in epic

**🚫 Development cannot proceed without @overseer approval at each mandatory gate**

### Multi-Session Development State

Complex projects span multiple AI sessions using shared state management:

```bash
# Start any session: read TODO.md, understand current state, continue work
@developer /skill session-workflow

# End any session: update TODO.md, commit progress, hand off to next session  
@developer /skill session-workflow
```

## 🔧 Technology Stack

**⚡ Modern Python Stack**
- UV package manager (5-10x faster than pip)
- Python 3.13 with latest language features  
- Task automation with taskipy
- Comprehensive testing with pytest + hypothesis

**🤖 AI Development Team**
- **@developer**: TDD workflow implementation with QA integration
- **@architect**: SOLID principles and design pattern enforcement  
- **@requirements-gatherer**: Business analysis using BABOK methodology
- **@overseer**: Quality gates and mandatory checkpoint enforcement
- **@repo-manager**: Release management and deployment workflows

**⚡ Modern Python Stack**
- Python 3.13+ with advanced type hints and protocols
- UV package manager (5-10x faster dependency management)
- Ruff formatting and linting (replaces 8+ tools)
- PyTest + Hypothesis for comprehensive testing

**📊 Quality Assurance**
- 100% test coverage requirement with branch coverage
- Property-based testing for edge case discovery
- Static type checking with Pyright
- Mutation testing with mutmut for test quality validation

## 📋 Development Commands

### Native Development

```bash
# Core workflow
task run              # Execute main application
task test             # Complete test suite with coverage
task test-fast        # Fast tests (skip slow integration tests)
task lint             # Ruff formatting and linting
task static-check     # Pyright type checking
task doc-serve        # Live documentation server
task doc-build        # Static API documentation generation
```

### Docker Development

```bash
# Development workflows
docker-compose up                              # Hot reload development
docker-compose --profile test up               # Complete test suite
docker-compose --profile quality up            # Code quality pipeline

# Production workflows  
docker build --target production -t app:prod . # Security-optimized build
docker-compose -f docker-compose.prod.yml up   # Production testing
docker-compose -f docker-compose.prod.yml --profile security up  # Vulnerability scan
```

## 📈 Quality Metrics & Standards

- ✅ **100% Test Coverage** - Branch and line coverage with pytest-cov
- ✅ **Security Hardened** - Distroless containers, non-root execution, vulnerability scanning  
- ✅ **Static Type Safety** - Complete type hints with protocol-based interfaces
- ✅ **Zero Linting Issues** - Automated Ruff formatting and style enforcement
- ✅ **Property-Based Testing** - Hypothesis for robust edge case validation
- ✅ **Architecture Compliance** - AI-enforced SOLID principles and Object Calisthenics
- ✅ **Container Security** - Minimal attack surface with read-only production filesystems

## 🚀 Release Management

### Smart Versioning & Naming

- **Hybrid Calver**: `v{major}.{minor}.{YYYYMMDD}` format
- **AI-Generated Names**: Themed releases based on PR content analysis
  - Performance: `"Swift Falcon"` `"Lightning Cheetah"`
  - Security: `"Guardian Shield"` `"Vigilant Owl"`  
  - Features: `"Creative Fox"` `"Innovative Dolphin"`
  - Infrastructure: `"Solid Foundation"` `"Robust Castle"`

### Deployment Ready

```bash
# Build production-ready container
docker build --target production -t your-project:latest .
docker run your-project:latest

# Smart release with AI naming
@repo-manager /skill git-release
# Example: Creates v1.2.20260411 "Secure Fortress" (Docker security improvements)

# Deploy with confidence
docker-compose -f docker-compose.prod.yml up --detach
```

## 🤝 Contributing

Help make this template the gold standard for Python development:

- 🐛 **Bug Reports & Fixes** - Improve stability and reliability
- ✨ **New AI Agents & Skills** - Expand development automation  
- 🐳 **Container Optimizations** - Enhance security and performance
- 📚 **Documentation** - Help others succeed faster
- 🎯 **Workflow Improvements** - Streamline development processes

```bash
# Quick contribution workflow
git clone https://github.com/nullhack/python-project-template.git
cd python-project-template
@developer /skill feature-definition    # Define your improvement
@developer /skill tdd                  # Test-driven implementation
@repo-manager /skill pr-management     # Professional PR creation
```

## 📄 License

MIT License - see [`LICENSE`](LICENSE) for details.

## 🙏 Built With Excellence

Standing on the shoulders of giants:

- [OpenCode](https://opencode.ai) - Revolutionary AI-powered development platform
- [UV](https://astral.sh/uv/) - Blazing fast Python package and project manager
- [Ruff](https://astral.sh/ruff/) - Extremely fast Python linter and formatter  
- [Docker](https://docker.com) - Industry-standard containerization platform
- [Distroless](https://github.com/GoogleContainerTools/distroless) - Google's minimal container images
- [Trivy](https://trivy.dev/) - Comprehensive security scanner
- [Hypothesis](https://hypothesis.readthedocs.io/) - Property-based testing framework

---

**[⭐ Star this repo](https://github.com/nullhack/python-project-template) to power your next breakthrough project!**

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/nullhack/python-project-template.svg?style=for-the-badge
[contributors-url]: https://github.com/nullhack/python-project-template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/nullhack/python-project-template.svg?style=for-the-badge
[forks-url]: https://github.com/nullhack/python-project-template/network/members
[stars-shield]: https://img.shields.io/github/stars/nullhack/python-project-template.svg?style=for-the-badge
[stars-url]: https://github.com/nullhack/python-project-template/stargazers
[issues-shield]: https://img.shields.io/github/issues/nullhack/python-project-template.svg?style=for-the-badge
[issues-url]: https://github.com/nullhack/python-project-template/issues
[license-shield]: https://img.shields.io/badge/license-MIT-green?style=for-the-badge
[license-url]: https://github.com/nullhack/python-project-template/blob/main/LICENSE