# Python Project Template V2

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen?style=for-the-badge)](docs/coverage/index.html)

> **Next-generation Python template** with intelligent project initialization and AI-enhanced development workflows

**Enterprise-grade Python project template** featuring an AI-powered setup agent that replaces cookiecutter with intelligent, interactive project initialization.

---

## ⚡ Quick Start

```bash
# Clone the template
git clone https://github.com/nullhack/python-project-template
cd python-project-template

# Install UV package manager (if not installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Initialize with intelligent setup agent
opencode && @setup-project

# The agent will interactively collect:
# - Project name, description, author details
# - GitHub username and repository settings
# - Package and module names
# Then automatically:
# - Process template files with your values
# - Rename package directories
# - Initialize Git repository
# - Setup development environment
```

## 🤖 V2 Intelligent Setup System

**Revolutionary Template Experience** - No more cookiecutter complexity! The V2 system features an AI agent that intelligently transforms the template into your custom project.

### Intelligent Project Initialization

```bash
# One command setup - AI handles everything
@setup-project

# Interactive metadata collection:
# ✓ Project name: "My Awesome API" 
# ✓ GitHub username: "johndoe"
# ✓ Author details and descriptions
# ✓ Smart defaults and validation

# Automated processing:
# ✓ Template files processed with your values
# ✓ Package directories renamed seamlessly  
# ✓ Git repository initialized
# ✓ Development environment ready
```

### Multi-Session Development

Complex projects span multiple AI sessions. `TODO.md` serves as shared state — any AI agent can continue exactly where the last session stopped.

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

## 🚀 What's New in V2

**Intelligent Setup Revolution** - Say goodbye to cookiecutter complexity!

| Feature | V1 (Cookiecutter) | **V2 (AI Agent)** |
|---------|-------------------|-------------------|
| **Setup Process** | Manual cookiecutter prompts | 🤖 Interactive AI agent |
| **Validation** | Basic input checking | ✅ Comprehensive validation with helpful errors |
| **Error Handling** | Manual cleanup required | 🔄 Automatic backup and rollback |
| **Customization** | Static template processing | 🧠 Intelligent placeholder replacement |
| **Integration** | Separate tool | 🔗 Native OpenCode agent ecosystem |
| **User Experience** | Technical command line | 💬 Conversational, guided setup |

### V2 Advantages
- **🎯 Zero Configuration Errors** - Smart validation prevents common mistakes
- **⚡ 2-Minute Setup** - From clone to ready development environment
- **🔄 Bulletproof Process** - Automatic rollback if anything goes wrong  
- **🤖 AI Integration** - Seamlessly integrates with development agents
- **📝 Clean Templates** - Minimal, maintainable template files

## 🏗️ Architecture & Standards

- **🎯 SOLID Principles** - Single responsibility, dependency inversion, clean interfaces
- **🔧 Object Calisthenics** - No primitives, small classes, behavior-rich objects
- **🧪 TDD Testing** - 100% coverage requirement with property-based tests
- **⚡ Modern Toolchain** - UV, Ruff, PyTest, Hypothesis, PyRight
- **🚀 Smart Releases** - Calver versioning with AI-generated themed names
- **🤖 AI-First Setup** - Intelligent template processing replaces static cookiecutter

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

## 🎯 Project Structure

```
python-project-template/
├── python_package_template/        # Main application package
│   ├── __init__.py                       # Package initialization
│   └── python_module_template.py   # Core module
├── .opencode/                            # AI development agents
│   ├── agents/                           # Specialized AI agents
│   │   ├── developer.md                  # 7-phase development workflow
│   │   ├── architect.md                  # SOLID architecture review
│   │   └── repo-manager.md               # Release and PR management
│   └── skills/                           # Development skills
│       ├── session-workflow/             # Multi-session development state
│       ├── feature-definition/           # Requirements planning
│       ├── tdd/                          # Test-driven development
│       ├── implementation/               # Guided implementation
│       └── code-quality/                 # Quality enforcement
├── tests/                                # Comprehensive test suite
├── docs/                                 # Documentation (api/, tests/, coverage/)
├── TODO.md                               # Development roadmap & session state
├── Dockerfile                            # Multi-stage container build
└── pyproject.toml                        # Project configuration
```

## 🔧 Technology Stack

| Category | Tools |
|----------|-------|
| **Package Management** | UV (blazing fast pip/poetry replacement) |
| **Code Quality** | Ruff (linting + formatting), PyRight (type checking) |
| **Testing** | PyTest + Hypothesis (property-based testing), pytest-html (BDD reports) |
| **AI Integration** | OpenCode agents for development automation |
| **Documentation** | pdoc with search functionality |
| **Containerization** | Docker with optimized multi-stage builds |

## 📈 Quality Metrics

- ✅ **100% Test Coverage** - Comprehensive test suite including edge cases
- ✅ **Static Type Safety** - Full type hints with protocol-based interfaces  
- ✅ **Zero Linting Issues** - Automated formatting and style enforcement
- ✅ **Property-Based Testing** - Hypothesis for robust validation
- ✅ **Architecture Compliance** - AI-enforced SOLID principles

## 🚀 Deployment Ready

```bash
# Production container build
docker build --target prod -t python_package_template:latest .
docker run python_package_template:latest

# Build API documentation
task doc-build  # Generates docs/api/index.html

# Publish API docs to GitHub Pages
task doc-publish  # Pushes docs/api to gh-pages branch

# Smart release management
@repo-manager /skill git-release
# Creates versioned release: v1.2.20260315 "Creative Fox"
```

## 🤝 Getting Started

### Create Your Project

```bash
# Clone the V2 template
git clone https://github.com/nullhack/python-project-template
cd python-project-template

# Let the AI setup agent transform it into your project
opencode && @setup-project

# Start developing with AI assistance
@developer /skill session-workflow
```

### Contributing to Template

Built with AI-assisted development workflows:

```bash
# Template development workflow
@developer /skill feature-definition
@developer /skill prototype-script
@developer /skill tdd
@architect  # Architecture review
@developer /skill implementation
@repo-manager /skill pr-management
```

## 📄 License

Distributed under the MIT License. See [LICENSE](LICENSE) for details.

## 🙏 Built With

- [AI-Enhanced Python Template](https://github.com/nullhack/python-project-template) - Enterprise-grade Python project template
- [OpenCode](https://opencode.ai) - AI-powered development platform
- [UV](https://astral.sh/uv/) - Modern Python package manager
- [Ruff](https://astral.sh/ruff/) - Extremely fast Python linter

---

**Author:** USER_NAME ([@nullhack](https://github.com/nullhack))  
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