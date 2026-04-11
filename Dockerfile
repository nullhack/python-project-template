# syntax=docker/dockerfile:1.7
# Modern Dockerfile for python-project-template
# Features: multi-stage build, distroless prod, security scanning, BuildKit caching

ARG PYTHON_VERSION=3.13.1
ARG BUILDPLATFORM=linux/amd64

# =============================================================================
# Base stage: Python + uv package manager
# =============================================================================
FROM --platform=$BUILDPLATFORM python:${PYTHON_VERSION}-alpine AS base

# Install uv for ultra-fast Python package management
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --upgrade pip uv

# Create non-root user early
RUN addgroup --system --gid 1001 appuser && \
    adduser --system --uid 1001 --ingroup appuser appuser

WORKDIR /app

# =============================================================================
# Dependencies stage: Install and cache Python dependencies  
# =============================================================================
FROM base AS deps

# Install build dependencies
RUN apk add --no-cache \
    build-base \
    linux-headers \
    git

# Copy dependency files first (better layer caching)
COPY pyproject.toml ./

# Install dependencies with uv (much faster than pip)
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=cache,target=/root/.cache/pip \
    uv pip install --system '.[dev]' taskipy

# =============================================================================
# Test stage: Run linting and tests
# =============================================================================
FROM deps AS test

# Copy source code
COPY . .

# Change ownership to appuser
RUN chown -R appuser:appuser /app
USER appuser

# Set build arguments for conditional testing
ARG TESTBUILD=true
ENV TESTBUILD=$TESTBUILD

# Run quality checks and tests if enabled
RUN if [ "$TESTBUILD" = "true" ]; then \
        echo "🔍 Running linting..." && \
        task lint && \
        echo "🧪 Running tests..." && \
        task test && \
        echo "✅ All quality checks passed!"; \
    fi

# =============================================================================
# Build stage: Create wheel distribution
# =============================================================================
FROM test AS build

# Build wheel package
RUN --mount=type=cache,target=/root/.cache/uv \
    uv build --wheel --out-dir dist

# =============================================================================
# Security scanning stage (optional but recommended)
# =============================================================================
FROM aquasec/trivy:latest AS security-scan

# Copy built artifacts for scanning
COPY --from=build /app/dist /scan/dist
COPY --from=build /app/pyproject.toml /scan/

# Run security scan (will fail build on HIGH/CRITICAL vulnerabilities)
RUN trivy fs --exit-code 1 --severity HIGH,CRITICAL /scan || \
    (echo "❌ Security vulnerabilities found! Check the output above." && exit 1)

# =============================================================================
# Runtime preparation: Install wheel in clean Python environment
# =============================================================================
FROM python:${PYTHON_VERSION}-alpine AS runtime-prep

# Install the wheel package in a clean environment
COPY --from=build /app/dist/*.whl /tmp/
RUN pip install --prefix=/app/python /tmp/*.whl

# =============================================================================
# Production stage: Minimal distroless runtime  
# =============================================================================
FROM gcr.io/distroless/python3-debian12:latest AS production

# Copy installed Python packages from runtime prep
COPY --from=runtime-prep /app/python /usr/local

# Set working directory  
WORKDIR /app

# Use non-root user (distroless default nonroot user)
USER nonroot:nonroot

# Configure Python for production
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONHASHSEED=random

# Health check using module execution
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -m python_package_template.python_module_template || exit 1

# Default command
CMD ["python", "-m", "python_package_template.python_module_template"]

# =============================================================================  
# Development stage: For local development with hot reload
# =============================================================================
FROM deps AS development

# Install development tools
RUN --mount=type=cache,target=/root/.cache/uv \
    uv pip install --system watchdog

# Copy source code
COPY . .

# Change ownership and switch to non-root user
RUN chown -R appuser:appuser /app
USER appuser

# Expose common development ports
EXPOSE 8000 8080 5678

# Development command with auto-reload
CMD ["python", "-m", "python_package_template.python_module_template"]

# =============================================================================
# Metadata and labels
# =============================================================================
LABEL maintainer="eol"
LABEL version="0.1.20260411" 
LABEL description="Python project template with modern Docker practices"
LABEL org.opencontainers.image.source="https://github.com/nullhack/python-project-template"
LABEL org.opencontainers.image.documentation="https://github.com/nullhack/python-project-template/tree/main/docs/api/"