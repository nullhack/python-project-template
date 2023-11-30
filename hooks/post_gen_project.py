{%- if cookiecutter.include_examples != "true" -%}
"""A module for removing specific directories.

This module provides a function to remove specific directories
using the `shutil` and `pathlib` modules.

Attributes:
    REMOVE_PATHS (List[str]): A list of directory paths to be removed.

"""

import shutil
from pathlib import Path

REMOVE_PATHS = [
    "bdd-features",
    "tests/scenarios/steps",
]

for path in REMOVE_PATHS:
    p = Path(".") / Path(path)
    if p and p.exists() and p.is_dir():
        shutil.rmtree(p)
{% endif %}
