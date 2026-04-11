"""Test main file."""

import logging
from typing import Literal

import fire

from python_package_template.python_module_template import version

logger = logging.getLogger(__name__)

LOGGER_LEVELS = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL,
}

ValidVerbosity = Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]


def main(verbosity: ValidVerbosity = "INFO") -> None:
    """Run with --verbosity=LEVEL (DEBUG, INFO, WARNING, ERROR, CRITICAL)."""
    # Validate verbosity at runtime
    verbosity_upper = verbosity.upper()
    if verbosity_upper not in LOGGER_LEVELS:
        valid_levels = ", ".join(LOGGER_LEVELS.keys())
        raise ValueError(
            f"Invalid verbosity level '{verbosity}'. Valid options: {valid_levels}"
        )

    logging.basicConfig(
        level=LOGGER_LEVELS[verbosity_upper],
        format="%(levelname)s - %(name)s: %(message)s",
    )
    version()


if __name__ == "__main__":
    fire.Fire(main)
