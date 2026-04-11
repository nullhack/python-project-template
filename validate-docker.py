#!/usr/bin/env python3
"""
Docker Setup Validation Script
Validates the new Docker configuration without requiring Docker to be installed.
"""

import re
from pathlib import Path


def validate_dockerfile(dockerfile_path: Path) -> list[str]:
    """Validate Dockerfile syntax and best practices."""
    issues = []

    if not dockerfile_path.exists():
        issues.append(f"Dockerfile not found: {dockerfile_path}")
        return issues

    content = dockerfile_path.read_text()
    lines = content.split("\n")

    # Check for syntax directive
    if not content.startswith("# syntax="):
        issues.append("Missing BuildKit syntax directive")

    # Check for multi-stage build
    from_count = len(re.findall(r"^FROM .* AS ", content, re.MULTILINE))
    if from_count < 2:
        issues.append(
            "Should use multi-stage build (found {} stages)".format(from_count)
        )

    # Check for security practices
    if "USER root" in content:
        issues.append("Avoid running as root user")

    if "--mount=type=cache" not in content:
        issues.append("Missing BuildKit cache mounts for optimization")

    # Check for distroless
    if "distroless" not in content:
        issues.append("Consider using distroless images for production")

    # Check for health check
    if "HEALTHCHECK" not in content:
        issues.append("Missing health check configuration")

    # Check for Python version pinning
    python_from_lines = [
        line for line in lines if line.startswith("FROM") and "python:" in line
    ]
    for line in python_from_lines:
        if "python:3-" in line or "python:latest" in line:
            issues.append(f"Pin specific Python version: {line.strip()}")

    return issues


def validate_dockerignore(dockerignore_path: Path) -> list[str]:
    """Validate .dockerignore completeness."""
    issues = []

    if not dockerignore_path.exists():
        issues.append(".dockerignore file missing")
        return issues

    content = dockerignore_path.read_text()

    # Essential patterns that should be ignored
    essential_patterns = [
        "__pycache__",
        (".git", "*.pyc", "*.py[cod]"),  # Either *.pyc or *.py[cod] is fine
        ".pytest_cache",
        "docs/",
        "*.log",
    ]

    for pattern in essential_patterns:
        if isinstance(pattern, tuple):
            # Check if any of the alternatives exist
            if not any(alt in content for alt in pattern):
                issues.append(
                    f"Missing .dockerignore pattern (one of): {', '.join(pattern)}"
                )
        else:
            if pattern not in content:
                issues.append(f"Missing .dockerignore pattern: {pattern}")

    return issues


def validate_compose_files(compose_paths: list[Path]) -> list[str]:
    """Validate docker-compose files."""
    issues = []

    for compose_path in compose_paths:
        if not compose_path.exists():
            issues.append(f"Compose file missing: {compose_path}")
            continue

        content = compose_path.read_text()

        # Check for version (should use modern format without version key)
        if content.strip().startswith("version:"):
            issues.append(f"{compose_path.name}: Remove deprecated 'version' key")

        # Check for named volumes
        if "volumes:" not in content:
            issues.append(f"{compose_path.name}: Consider using named volumes")

        # Check for health checks
        if "healthcheck:" not in content:
            issues.append(f"{compose_path.name}: Missing health checks")

    return issues


def main():
    """Main validation function."""
    print("🐳 Docker Setup Validation")
    print("=" * 50)

    project_root = Path(__file__).parent
    all_issues = []

    # Validate Dockerfile
    print("\n📄 Validating Dockerfile...")
    dockerfile_issues = validate_dockerfile(project_root / "Dockerfile")
    if dockerfile_issues:
        print("⚠️  Issues found:")
        for issue in dockerfile_issues:
            print(f"   - {issue}")
        all_issues.extend(dockerfile_issues)
    else:
        print("✅ Dockerfile looks good!")

    # Validate .dockerignore
    print("\n🚫 Validating .dockerignore...")
    dockerignore_issues = validate_dockerignore(project_root / ".dockerignore")
    if dockerignore_issues:
        print("⚠️  Issues found:")
        for issue in dockerignore_issues:
            print(f"   - {issue}")
        all_issues.extend(dockerignore_issues)
    else:
        print("✅ .dockerignore looks good!")

    # Validate compose files
    print("\n🐙 Validating Docker Compose files...")
    compose_files = [
        project_root / "docker-compose.yml",
        project_root / "docker-compose.prod.yml",
    ]
    compose_issues = validate_compose_files(compose_files)
    if compose_issues:
        print("⚠️  Issues found:")
        for issue in compose_issues:
            print(f"   - {issue}")
        all_issues.extend(compose_issues)
    else:
        print("✅ Compose files look good!")

    # Summary
    print("\n" + "=" * 50)
    if all_issues:
        print(f"❌ Found {len(all_issues)} issues to address")
        return 1
    else:
        print("🎉 All Docker configurations look great!")
        print("\n📚 Usage Examples:")
        print("   Development: docker-compose up")
        print("   Testing:     docker-compose --profile test up")
        print("   Production:  docker-compose -f docker-compose.prod.yml up")
        return 0


if __name__ == "__main__":
    exit(main())
