# syntax=docker/dockerfile:1.7
# Simplified Dockerfile for python-project-template
# Single-stage development-focused build

ARG PYTHON_VERSION=3.13.1

FROM python:${PYTHON_VERSION}-slim AS base

# Install uv for fast Python package management
RUN pip install --upgrade pip uv

# Create non-root user
RUN groupadd --gid 1001 appuser && \
    useradd --uid 1001 --gid appuser --shell /bin/bash --create-home appuser

WORKDIR /app

# Copy dependency files first (better layer caching)
COPY pyproject.toml uv.lock* ./

# Install dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --dev

# Copy source code
COPY . .

# Change ownership to appuser
RUN chown -R appuser:appuser /app
USER appuser

# Configure Python
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Expose common ports
EXPOSE 8000 8080 5678

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -m app || exit 1

# Default command
CMD ["python", "-m", "app"]

# Labels
LABEL maintainer="eol"
LABEL version="3.0.20260414"
LABEL description="Python template with some awesome tools to quickstart any Python project"
LABEL org.opencontainers.image.source="https://github.com/nullhack/python-project-template"