"""Unit tests for app.__main__ — in-process coverage."""

import argparse
import importlib.metadata
import sys

import pytest

from app.__main__ import build_parser, main


def test_build_parser_returns_argument_parser() -> None:
    """build_parser returns a configured ArgumentParser instance."""
    parser = build_parser()
    assert isinstance(parser, argparse.ArgumentParser)


def test_build_parser_description_matches_package_metadata() -> None:
    """build_parser sets description from package metadata Summary."""
    parser = build_parser()
    expected = importlib.metadata.metadata("temple8")["Summary"]
    assert parser.description == expected


def test_main_exits_0_with_no_args(monkeypatch: pytest.MonkeyPatch) -> None:
    """main() with no argv exits cleanly (code 0)."""
    monkeypatch.setattr(sys, "argv", ["app"])
    main()


def test_main_exits_0_with_help(monkeypatch: pytest.MonkeyPatch) -> None:
    """main() with --help exits with SystemExit(0)."""
    monkeypatch.setattr(sys, "argv", ["app", "--help"])
    with pytest.raises(SystemExit) as exc_info:
        main()
    assert exc_info.value.code == 0


def test_main_exits_0_with_version(monkeypatch: pytest.MonkeyPatch) -> None:
    """main() with --version exits with SystemExit(0)."""
    monkeypatch.setattr(sys, "argv", ["app", "--version"])
    with pytest.raises(SystemExit) as exc_info:
        main()
    assert exc_info.value.code == 0
