"""Test main file."""

import logging

logger = logging.Logger(__name__)
sh = logging.StreamHandler()
sh.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
sh.setFormatter(formatter)
logger.addHandler(sh)


def main() -> str:
    """Just a main function."""
    logger.info("Hello from python-project-uv!")


if __name__ == "__main__":
    main()
