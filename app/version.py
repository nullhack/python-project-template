"""Module Docstring."""

import logging
import tomllib
from pathlib import Path

logger = logging.getLogger("app")


def version() -> str:
    """Log version at INFO level.

    Returns:
        Version string from pyproject.toml.

    Examples:
        >>> result = version()  # doctest: +ELLIPSIS
        >>> isinstance(result, str)
        True
        >>> len(result) > 0
        True
        >>> '.' in result  # Version should contain dots
        True

    """
    pyproject_path = Path(__file__).parent.parent / "pyproject.toml"

    with Path(pyproject_path).open("rb") as f:
        data = tomllib.load(f)

    version_str = data["project"]["version"]
    logger.info("Version: %s", version_str)
    return version_str


if __name__ == "__main__":
    version()
