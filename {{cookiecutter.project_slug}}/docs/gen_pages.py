"""This module generates readme and feature files for mkdocs.

As part of the mkdocs-gen-file plugin, this module helps to automate
readme generation using the README file and feature pages using the feature
files if they do exist.
"""

from pathlib import Path

import mkdocs_gen_files

docs_parent_dir = Path(__file__).parent.parent

# Automagically injects README file into the documentation
readme_path = docs_parent_dir / "README.md"
if readme_path.exists():
    with Path.open(readme_path, "r") as r, mkdocs_gen_files.open(
        "readme.md", "w"
    ) as f:
        f.write(r.read())

