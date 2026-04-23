"""CLI entrypoint for temple8 — invoked via `python -m app`."""

import argparse
import importlib.metadata


def build_parser() -> argparse.ArgumentParser:
    """Build and return the argument parser."""
    meta = importlib.metadata.metadata("temple8")
    parser = argparse.ArgumentParser(
        prog="temple8",
        description=meta["Summary"],
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"temple8 {meta['Version']}",
    )
    return parser


def main() -> None:
    """Run the application."""
    build_parser().parse_args()


if __name__ == "__main__":
    main()
