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

# 3. **IMPORTANT**: Customize the template for your project
python setup_project.py
# This interactive script will:
# - Rename directories from 'app' to your package name
# - Update pyproject.toml with your project details  
# - Fix Docker configuration paths
# - Replace all template placeholders

# 4. Follow the Git configuration commands shown by setup_project.py
# Example: git remote set-url origin https://github.com/yourname/yourproject

# 5. Setup development environment  
uv venv && uv pip install -e '.[dev]'

# 6. Validate everything works
task test && task lint && task static-check

# 7. Initialize AI development environment (optional)
opencode && /init
```

**⚠️ Template State Notice**: This project is currently in "template state" with placeholder values. The `setup_project.py` script **must** be run to properly configure Docker, package paths, and project metadata before development.

**Requirements**: Python 3.13+ and UV package manager are required.

## 🎯 What This Template Provides

This template creates a production-ready Python project with:

### 🔧 **Project Setup & Customization**
- **Automated setup script** (`setup_project.py`) - Interactive customization with your project details
- **Smart folder renaming** - Automatically renames `app/` directory to match your project
- **Docker path fixing** - Updates Docker configuration to match your project structure  
- **Git configuration** - Provides ready-to-use Git commands for remotes and user setup
- **Template processing** - Replaces all placeholders in pyproject.toml and configuration files

### 🤖 **AI-Enhanced Development Workflow**  
- **Multi-session continuity** - Projects span multiple AI sessions with shared state in `TODO.md`
- **Specialized agents** - Built-in agents for architecture, development, QA, and repository management
- **Skills system** - Modular workflows for TDD, feature definition, prototyping, and releases

### 🏗️ **Enterprise Architecture & Quality**
- **SOLID principles** - Enforced through AI architecture reviews via OpenCode agents
- **Object Calisthenics** - Clean, behavior-rich code patterns enforced by QA workflows
- **100% test coverage** - TDD workflows with acceptance criteria docstrings and property-based testing (Hypothesis)
- **Mutation testing** - mutmut integration for test quality validation
- **Zero-config tooling** - UV, taskipy, Ruff, PyTest, Hypothesis, PyRight pre-configured

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
- **🧪 TDD Testing** - Acceptance criteria format with Given/When/Then docstrings, 100% coverage requirement
- **🔬 Property-Based Testing** - Hypothesis integration for robust edge case validation
- **🧬 Mutation Testing** - mutmut for genetic algorithm-based test quality assurance
- **⚡ Modern Toolchain** - UV, taskipy, Ruff, PyTest, Hypothesis, PyRight
- **🚀 Smart Releases** - Hybrid major.minor.calver versioning with AI-generated themed names

## 📋 Development Commands

This project uses **taskipy** for task automation (configured in `pyproject.toml`):

```bash
# Core development workflow
task run              # Execute version module (demo command)
task test             # Run comprehensive test suite with coverage
task test-fast        # Run fast tests only (skip slow tests)
task test-slow        # Run only slow tests (marked with @pytest.mark.slow)
task lint             # Format and lint code with ruff
task static-check     # Type safety validation with pyright

# Documentation
task doc-serve        # Live pdoc documentation server (localhost:8080)
task doc-build        # Build static pdoc API docs to docs/api/
task doc-publish      # Publish API docs to GitHub Pages

# Quality assurance
task test-report      # Detailed coverage report (included in task test)
task mut              # Mutation testing with mutmut
task mut-clean        # Reset mutation testing cache
```

## 🐳 Docker Usage

**⚠️ Important**: Run `python setup_project.py` first to configure the template before using Docker.

Docker provides development environment with hot reload and integrated tooling:

```bash
# Development environment with hot reload
docker-compose up                     # Main application (ports 8000, 8080, 5678)

# Specialized services (use profiles)
docker-compose --profile test up      # Run complete test suite
docker-compose --profile docs up      # Documentation server (localhost:8080)  
docker-compose --profile quality up   # Code quality checks (lint + typecheck)

# Build standalone image
docker build -t your-project-name .   # Build development image
```

**Current Docker Configuration:**
- **Main service**: Hot reload development with volume mounts
- **Test profile**: Full test suite execution
- **Docs profile**: Live documentation server  
- **Quality profile**: Linting and type checking

**Note**: The Docker configuration currently references template paths and requires `setup_project.py` to be run for proper functionality.



## 🔧 Technology Stack

| Category | Tools |
|----------|-------|
| **Package Management** | UV (blazing fast pip/poetry replacement) |
| **Task Automation** | taskipy (configured in pyproject.toml) |
| **Code Quality** | Ruff (linting + formatting), PyRight (type checking) |
| **Testing** | PyTest + Hypothesis (property-based testing), pytest-html (acceptance criteria reports) |
| **Mutation Testing** | mutmut (genetic algorithm-based mutation testing) |
| **Coverage** | pytest-cov (100% coverage requirement) |
| **AI Integration** | OpenCode agents and skills for development automation |
| **Documentation** | pdoc with search functionality and GitHub Pages publishing |
| **Containerization** | Docker development environment with hot reload and service profiles |

## 📈 Quality Metrics

- ✅ **100% Test Coverage** - pytest-cov with fail-under=100 requirement
- ✅ **Static Type Safety** - PyRight type checking with full type hints  
- ✅ **Zero Linting Issues** - Ruff automated formatting and Google-style conventions
- ✅ **Property-Based Testing** - Hypothesis integration for robust validation
- ✅ **Mutation Testing** - mutmut for genetic algorithm-based test quality validation
- ✅ **Acceptance Criteria Format** - Given/When/Then docstrings with pytest-html reporting
- ✅ **Architecture Compliance** - AI-enforced SOLID principles through OpenCode agents

## 🚀 Deployment Ready

Projects generated from this template include Docker support for development:

```bash
# After running setup_project.py in your configured project
docker build -t your-project-name .
docker run -p 8000:8000 your-project-name

# Docker Compose development environment
docker-compose up                     # Development environment with hot reload
docker-compose --profile test up      # Run test suite
docker-compose --profile docs up      # Documentation server
docker-compose --profile quality up   # Code quality checks

# API documentation
task doc-build  # Generates docs/api/index.html
task doc-serve  # http://localhost:8080 (live server)
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