#!/bin/bash
# template_test.sh - Comprehensive cookiecutter template testing script

set -e

# Configuration
TEMPLATE_DIR=$(pwd)
TEST_DIR="/tmp/template-tests-$(date +%s)"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

log_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

log_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

log_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

log_error() {
    echo -e "${RED}❌ $1${NC}"
}

# Clean up function
cleanup() {
    if [ -d "$TEST_DIR" ]; then
        rm -rf "$TEST_DIR"
        log_info "Cleaned up test directory: $TEST_DIR"
    fi
}

# Set up trap for cleanup
trap cleanup EXIT

# Create test directory
mkdir -p "$TEST_DIR"
cd "$TEST_DIR"

log_info "Starting cookiecutter template tests at $TIMESTAMP"
log_info "Test directory: $TEST_DIR"

# Test 1: Default configuration
log_info "Test 1: Default configuration"
cookiecutter "$TEMPLATE_DIR" --no-input
default_project=$(ls -d */ | head -1 | sed 's/\///')
log_success "Generated project: $default_project"

# Test 2: Custom configuration
log_info "Test 2: Custom configuration"
cookiecutter "$TEMPLATE_DIR" --no-input \
  full_name="Test Developer" \
  email="test@example.com" \
  github_username="test-dev" \
  project_name="Custom Test Project" \
  project_short_description="Testing template with custom values" \
  minimum_coverage="95" \
  license="MIT" \
  version="1.0.0"

custom_project="custom-test-project"
log_success "Generated project: $custom_project"

# Test 3: Edge cases  
log_info "Test 3: Edge case configuration"
cookiecutter "$TEMPLATE_DIR" --no-input \
  project_name="Edge Case Project With Long Name" \
  project_short_description="This is a very long description to test edge cases and ensure the template handles it properly without breaking anything in the generated files or configuration" \
  minimum_coverage="100" \
  github_username="edge-case-user"

edge_project="edge-case-project-with-long-name"
log_success "Generated project: $edge_project"

# Validation function
validate_project() {
    local project_dir=$1
    local project_name=$2
    
    log_info "Validating $project_dir..."
    
    cd "$project_dir"
    
    # Structure validation
    local required_dirs=(".opencode" ".opencode/agents" ".opencode/skills" "tests" "docs")
    local required_files=("pyproject.toml" "README.md" "AGENTS.md")
    
    for dir in "${required_dirs[@]}"; do
        if [ ! -d "$dir" ]; then
            log_error "Missing directory: $dir"
            return 1
        fi
    done
    
    for file in "${required_files[@]}"; do
        if [ ! -f "$file" ]; then
            log_error "Missing file: $file"
            return 1
        fi
    done
    
    log_success "Project structure validation passed"
    
    # Check for unsubstituted variables
    if grep -r "{{cookiecutter" . --exclude-dir=venv --exclude-dir=.git 2>/dev/null | grep -v ".pyc"; then
        log_error "Found unsubstituted cookiecutter variables"
        return 1
    fi
    log_success "No unsubstituted variables found"
    
    # Validate pyproject.toml syntax
    if ! python3 -c "import tomllib; tomllib.load(open('pyproject.toml', 'rb'))" 2>/dev/null; then
        log_error "pyproject.toml syntax validation failed"
        return 1
    fi
    log_success "pyproject.toml syntax is valid"
    
    # Validate YAML frontmatter in agents
    for agent in .opencode/agents/*.md; do
        if [ -f "$agent" ]; then
            if ! python -c "
import yaml, sys
with open('$agent', 'r') as f:
    content = f.read()
    if '---' in content:
        parts = content.split('---')
        if len(parts) >= 3:
            try:
                yaml.safe_load(parts[1])
            except Exception as e:
                print(f'Invalid YAML in $agent: {e}')
                sys.exit(1)
" 2>/dev/null; then
                log_error "YAML validation failed for $agent"
                return 1
            fi
        fi
    done
    log_success "Agent YAML validation passed"
    
    # Validate YAML frontmatter in skills
    for skill in .opencode/skills/*/SKILL.md; do
        if [ -f "$skill" ]; then
            if ! python -c "
import yaml, sys
with open('$skill', 'r') as f:
    content = f.read()
    if '---' in content:
        parts = content.split('---')
        if len(parts) >= 3:
            try:
                yaml.safe_load(parts[1])
            except Exception as e:
                print(f'Invalid YAML in $skill: {e}')
                sys.exit(1)
" 2>/dev/null; then
                log_error "YAML validation failed for $skill"
                return 1
            fi
        fi
    done
    log_success "Skills YAML validation passed"
    
    # Check project name appears in key files
    if ! grep -q "$project_name" README.md; then
        log_error "Project name not found in README.md"
        return 1
    fi
    
    if ! grep -q "$project_name" AGENTS.md; then
        log_error "Project name not found in AGENTS.md"
        return 1
    fi
    log_success "Project name validation passed"
    
    # Install dependencies and test
    log_info "Installing dependencies..."
    
    # Check if Python is available
    if ! command -v python3 &> /dev/null; then
        log_error "Python is not available"
        return 1
    fi
    
    # Create virtual environment
    python3 -m venv venv
    source venv/bin/activate
    
    # Install UV and dependencies
    if ! pip install uv &>/dev/null; then
        log_error "Failed to install uv"
        return 1
    fi
    
    if ! uv pip install '.[dev]' &>/dev/null; then
        log_error "Failed to install project dependencies"
        return 1
    fi
    log_success "Dependencies installed"
    
    # Run quality checks
    log_info "Running quality checks..."
    
    # Linting
    if ! python -m ruff check . &>/dev/null; then
        log_error "Ruff linting failed"
        return 1
    fi
    log_success "Linting passed"
    
    # Type checking  
    if ! python -m pyright . &>/dev/null; then
        log_error "Type checking failed"
        return 1
    fi
    log_success "Type checking passed"
    
    # Tests
    if ! python -m pytest tests/ -v &>/dev/null; then
        log_error "Tests failed"
        return 1
    fi
    log_success "Tests passed"
    
    # Documentation build
    if ! python -m mkdocs build &>/dev/null; then
        log_error "Documentation build failed"
        return 1
    fi
    log_success "Documentation build passed"
    
    log_success "Project $project_dir validation completed successfully"
    cd ..
    return 0
}

# Run validations
log_info "Starting project validations..."

if validate_project "$default_project" "Python Project Example"; then
    log_success "Default configuration validation passed"
else
    log_error "Default configuration validation failed"
    exit 1
fi

if validate_project "$custom_project" "Custom Test Project"; then
    log_success "Custom configuration validation passed"
else
    log_error "Custom configuration validation failed"
    exit 1
fi

if validate_project "$edge_project" "Edge Case Project With Long Name"; then
    log_success "Edge case configuration validation passed"
else
    log_error "Edge case configuration validation failed"
    exit 1
fi

log_success "🎉 All template tests passed successfully!"
echo
log_info "📊 Test Summary:"
echo "   - Default configuration: ✅"
echo "   - Custom configuration: ✅"
echo "   - Edge case configuration: ✅"
echo "   - Structure validation: ✅"
echo "   - YAML validation: ✅"
echo "   - Quality checks: ✅"
echo "   - Generated projects work: ✅"
echo
log_success "Template testing completed successfully at $(date)"