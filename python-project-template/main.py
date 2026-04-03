"""Test main file."""

import logging
import fire

logger = logging.getLogger(__name__)

def set_logging(verbosity: int = 0) -> None:
    mapping = {
        1: logging.WARNING,
        2: logging.INFO,
        3: logging.DEBUG,
    }
    level = mapping.get(verbosity, logging.ERROR)
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
