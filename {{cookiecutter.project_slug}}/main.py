"""Test main file."""

import logging
import fire

logger = logging.getLogger(__name__)

def set_logging(verbosity: int = 0) -> None:
    if verbosity >= 3:
        level = logging.DEBUG
    elif verbosity == 2:
        level = logging.INFO
    elif verbosity == 1:
        level = logging.WARNING
    else:
        level = logging.ERROR
    logging.basicConfig(
            level=level,
            format="%(levelname)s - %(name)s: %(message)s"
        )

def main(verbosity: int = 0):
    """Run with --verbosity=N (0..3+)"""
    set_logging(verbosity)
    logger.debug("debug")
    logger.info("info")
    logger.warning("warning")
    logger.error("error")
    return "done"

if __name__ == "__main__":
    fire.Fire(main)
