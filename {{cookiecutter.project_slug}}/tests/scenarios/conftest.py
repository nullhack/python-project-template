"""A module for configuring pytest to include new features.

This module provides a function to add new features automatically
as test files in pytest. The new features will trigger errors because
steps are not implemented.
"""

from pathlib import Path
from typing import Any, Callable

import pytest
from pytest_bdd.feature import get_features
from pytest_bdd.scenario import get_features_base_dir
from pytest_bdd.utils import get_caller_module_path


def pytest_configure() -> None:
    """Configure tests to include new features.

    This function adds new features automatically as test files.
    Adding new features will trigger errors because steps are not implemented.

    Args:
        config (Config): Configuration provided by pytest.
    """
    conftest_dir = Path(__file__).parent
    caller_module_path = Path(get_caller_module_path())
    features_base_dir = Path(get_features_base_dir(caller_module_path))

    features = (
        get_features([features_base_dir])
        if features_base_dir.exists()
        else []
    )

    for feat in features:
        feature_dir = Path(feat.filename).parent
        file_dir = (
            conftest_dir / "steps" / feature_dir.relative_to(features_base_dir)
        )
        file_name = Path(feat.filename).stem + "_test.py"
        file_path = file_dir / file_name
        feature_rel_path = Path(feat.filename).relative_to(features_base_dir)

        txt = (
            '"""Feature steps implementation.\n\n'
            f"Source file: {feature_rel_path}\n"
            '"""\n'
            "from pytest_bdd import scenarios\n\n"
            f'scenarios("{feature_rel_path}")'
        )

        file_dir.mkdir(parents=True, exist_ok=True)

        if not file_path.exists():
            with Path.open(file_path, "w") as f:
                f.write(txt)


def pytest_bdd_apply_tag(tag: str, function: Callable[..., Any]) -> bool | None:
    """Apply custom tag behavior for pytest-bdd.

    Args:
        tag (str): The tag specified in the feature file.
        function (Callable): The test function the tag applies to.

    Returns:
        bool | None: True if the tag was handled, otherwise None.
    """
    if tag == "todo":
        marker = pytest.mark.skip(reason="Not implemented yet")
        marker(function)
        return True
    return None
