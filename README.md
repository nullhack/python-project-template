# Python Project Template

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen?style=for-the-badge)](docs/coverage/index.html)

[![CI](https://img.shields.io/github/actions/workflow/status/nullhack/python-project-template/ci.yml?style=for-the-badge&label=CI)](https://github.com/nullhack/python-project-template/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.13-blue?style=for-the-badge)](https://www.python.org/downloads/)

> Python template with some awesome tools to quickstart any Python project

**🚀 Enterprise Python Project Template** - AI-enhanced development template with TDD workflows, quality standards, and zero-config tooling.

## ⚡ Quick Start

### Using This Template

```bash
# 1. Clone the template
git clone https://github.com/nullhack/python-project-template
cd python-project-template

# 2. Install UV package manager (if not installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 3. Customize the template for your project
python setup_project.py

# 4. Follow the Git configuration commands shown
# (setup_project.py will display the exact commands)

# 5. Initialize AI development environment (optional)
opencode && /init

# 6. Setup development environment  
uv venv && uv pip install -e '.[dev]'

# 7. Validate everything works
task test && task lint && task static-check
```

## 🎯 What This Template Provides

This template creates a production-ready Python project with:

### 🔧 **Project Setup & Customization**
- **Automated setup script** (`setup_project.py`) - Interactive customization with your project details
- **Smart folder renaming** - Automatically renames directories to match your project
- **Git configuration** - Provides ready-to-use Git commands for remotes and user setup
- **Template processing** - Replaces all placeholders with your actual project information

### 🤖 **AI-Enhanced Development Workflow**  
- **Multi-session continuity** - Projects span multiple AI sessions with shared state in `TODO.md`
- **Specialized agents** - Built-in agents for architecture, development, QA, and repository management
- **Skills system** - Modular workflows for TDD, feature definition, prototyping, and releases

### 🏗️ **Enterprise Architecture & Quality**
- **SOLID principles** - Enforced through AI architecture reviews
- **Object Calisthenics** - Clean, behavior-rich code patterns  
- **100% test coverage** - TDD workflows with property-based testing (Hypothesis)
- **Zero-config tooling** - UV, Ruff, PyTest, PyRight pre-configured

## 🤖 AI-Powered Development

This project includes built-in AI agents to accelerate your development.

### Multi-Session Development

Complex projects are developed across multiple AI sessions. `TODO.md` at the root acts as the shared state — any AI agent can pick up exactly where the last session stopped.

```bash
# Start any session: read state, orient, continue
@developer /skill session-workflow

# End any session: update TODO.md, commit progress, hand off
@developer /skill session-workflow
```

### Feature Development Workflow

```bash
# Define new features with SOLID principles
@developer /skill feature-definition

# Create prototypes and validate concepts  
@developer /skill prototype-script

# Write comprehensive tests first (TDD)
@developer /skill tdd

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
- **🧪 TDD Testing** - 100% coverage requirement with property-based tests
- **⚡ Modern Toolchain** - UV, Ruff, PyTest, Hypothesis, PyRight
- **🚀 Smart Releases** - Calver versioning with AI-generated themed names

## 📋 Development Commands

```bash
# Core development workflow
task run              # Execute main application
task test             # Run comprehensive test suite  
task lint             # Format and lint code
task static-check     # Type safety validation
task doc-serve        # Live pdoc documentation server
task doc-build        # Build static pdoc API docs
task doc-publish      # Publish API docs to GitHub Pages

# Quality assurance
task test-report      # Detailed coverage report
task mut-report       # Mutation testing (optional)
```

## 🐳 Docker Usage

Simple Docker setup for development with hot reload and integrated tooling.

```bash
# Development workflows
docker-compose up                     # Hot reload development environment
docker-compose --profile test up      # Run complete test suite
docker-compose --profile docs up      # Documentation server (localhost:8080)
docker-compose --profile quality up   # Code quality checks (lint + typecheck)

# Build standalone image (after running setup_project.py)
docker build -t your-project-name .     # Build development image
```

**Note**: Run `python setup_project.py` first to replace template variables before using Docker.

- **🛠️ Development**: Hot reload, separate services for testing/docs/quality checks



## 🔧 Technology Stack

| Category | Tools |
|----------|-------|
| **Package Management** | UV (blazing fast pip/poetry replacement) |
| **Code Quality** | Ruff (linting + formatting), PyRight (type checking) |
| **Testing** | PyTest + Hypothesis (property-based testing), pytest-html (BDD reports) |
| **AI Integration** | OpenCode agents for development automation |
| **Documentation** | pdoc with search functionality |
| **Containerization** | Docker development environment with hot reload |

## 📈 Quality Metrics

- ✅ **100% Test Coverage** - Comprehensive test suite including edge cases
- ✅ **Static Type Safety** - Full type hints with protocol-based interfaces  
- ✅ **Zero Linting Issues** - Automated formatting and style enforcement
- ✅ **Property-Based Testing** - Hypothesis for robust validation
- ✅ **Architecture Compliance** - AI-enforced SOLID principles

## 🚀 Deployment Ready

Projects generated from this template include Docker support:

```bash
# In your generated project
docker build -t your-project-name .
docker run your-project-name

# Docker Compose development
docker-compose up                     # Development environment
docker-compose --profile test up      # Run tests  
docker-compose --profile docs up      # Documentation server

# API documentation (generated projects)
task doc-build  # Generates docs/api/index.html
task doc-serve  # http://localhost:8080
```

## 🤝 Contributing

Help improve this template for the entire Python community:

### Template Improvements

```bash
# Fork and improve the template
git clone https://github.com/your-username/python-project-template  
cd python-project-template

# Test your changes
python setup_project.py --dry-run --github-username testuser --yes

# Add new skills, agents, or template features
# Submit pull request with improvements
```

### Areas for Contribution
- **New Skills** - Add specialized workflows (deployment, security, performance)
- **Agent Enhancements** - Improve existing agents or add new specialized ones  
- **Template Updates** - Better project structures, additional tooling, improved defaults
- **Documentation** - Usage guides, examples, best practices

## 📄 License

Distributed under the MIT License. See [LICENSE](LICENSE) for details.

## 🙏 Built With

- [Python Project Template](https://github.com/nullhack/python-project-template) - Enterprise-grade Python project template
- [OpenCode](https://opencode.ai) - AI-powered development platform
- [UV](https://astral.sh/uv/) - Modern Python package manager
- [Ruff](https://astral.sh/ruff/) - Extremely fast Python linter

---

**Author:** eol ([@nullhack](https://github.com/nullhack))  
**Project:** [python-project-template](https://github.com/nullhack/python-project-template)  
**Documentation:** [nullhack.github.io/python-project-template](https://nullhack.github.io/python-project-template)

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