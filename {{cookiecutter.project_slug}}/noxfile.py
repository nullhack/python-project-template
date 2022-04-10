# -*- coding: utf-8 -*-
"""Nox file used to run default routines."""

from pathlib import Path

import nox

nox.options.sessions = ["install-dev", "pre-commit"]


@nox.session(python=False, name="run")
def run(session):
    """Run the project main module."""
    session.run(
        "poetry",
        "run",
        "python",
        "-m",
        "{{cookiecutter.package_name}}.{{cookiecutter.module_name}}",
    )


@nox.session(python=False, name="install-poetry")
def install_poetry(session):
    """Install poetry."""
    session.run("pip", "install", "poetry")


@nox.session(python=False, name="install")
def install(session):
    """Install project itself."""
    install_poetry(session)
    session.run("poetry", "install", "--no-dev")


@nox.session(python=False, name="install-dev")
def install_dev(session):
    """Install project dependencies for development."""
    install_poetry(session)
    session.run("poetry", "install")
    session.run("git", "init")
    session.run(
        "poetry",
        "run",
        "pre-commit",
        "install",
        "--hook-type",
        "pre-commit",
        "--hook-type",
        "pre-push",
    )


@nox.session(python=False, name="tests")
def tests(session):
    """Run default tests."""
    install_dev(session)
    session.run("poetry", "run", "pytest")


@nox.session(python=False, name="pre-commit")
def pre_commit(session):
    """Run pre-commit checks."""
    install_dev(session)
    session.run("poetry", "run", "pre-commit", "run", "--all-files")


@nox.session(python=False, name="black")
def black(session):
    """Fix code structure using black."""
    install_dev(session)
    session.run("poetry", "run", "black", "src", "tests", "noxfile.py")


@nox.session(python=False, name="lint")
def lint(session):
    """Check styling using Flake8 and external packages."""
    install_dev(session)
    session.run("poetry", "run", "flake8")


@nox.session(python=False, name="uml")
def uml(session):
    """Generate UML diagrams."""
    install_dev(session)
    p = Path(r"src").glob("*")
    folders = [x for x in p if x.is_dir()]
    for folder in folders:
        package_name = folder.name
        session.run(
            "poetry",
            "run",
            "pyreverse",
            "-ASmy",
            package_name,
            "-d",
            "docs/uml/artifacts",
            "-p",
            package_name,
        )
        session.run(
            "poetry",
            "run",
            "pyreverse",
            "-ASmy",
            package_name,
            "-d",
            "docs/uml/diagrams",
            "-p",
            package_name,
            "-o",
            "png",
        )


@nox.session(python=False, name="test-docs")
def test_docs(session):
    """Run default tests."""
    install_dev(session)
    session.run(
        "poetry",
        "run",
        "pytest",
        "--html=docs/pytest_report.html",
        "--self-contained-html",
        "--cov-report",
        "html:docs/cov-report",
    )


@nox.session(python=False, name="api-docs")
def api_docs(session):
    """Generate API documentation using docstrings and pdoc3."""
    install_dev(session)
    session.run(
        "poetry",
        "run",
        "pdoc",
        "--html",
        ".",
        "--force",
        "--output-dir",
        "docs/api",
    )
