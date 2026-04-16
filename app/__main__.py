"""Entry point for running the application as a module."""

import logging

import fire

logger = logging.getLogger(__name__)


def main(verbosity: str = "INFO") -> None:
    """Run the application.

    Args:
        verbosity: Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL).
    """
    logging.basicConfig(
        level=getattr(logging, verbosity.upper(), logging.INFO),
        format="%(levelname)s - %(name)s: %(message)s",
    )
    logger.info("Ready.")


if __name__ == "__main__":
    fire.Fire(main)
