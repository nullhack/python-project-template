"""Configuration file for pytest.

This module will inject configuration scripts before running tests.
"""
from pytest_bdd import feature
from pytest_bdd.scenario import get_features_base_dir
from pytest_bdd.utils import get_caller_module_path
from pathlib import Path
import pytest


def pytest_configure(config: pytest.Config) -> None:
    """Configure tests tp include new features.

    Args:
        config (Config): Configuration provided by pytest.

    """
    conftest_dir = Path(__file__).parent
    caller_module_path = get_caller_module_path()
    features_base_dir = get_features_base_dir(caller_module_path)
    features = feature.get_features([features_base_dir])

    for feat in features:

        feature_dir = Path(feat.filename).parent
        file_dir = (
            conftest_dir / "steps" / feature_dir.relative_to(features_base_dir)
        )
        file_name = Path(feat.filename).stem + "_test.py"
        file_path = file_dir / file_name
        feature_rel_path = Path(feat.filename).relative_to(features_base_dir)
        txt = (
            '"""Feature steps implementation.\n'
            "\n"
            f'Source file: {feature_rel_path}\n"""\n'
            "from pytest_bdd import scenarios\n"
            "\n"
            f"""scenarios("{feature_rel_path}")"""
        )

        file_dir.mkdir(parents=True, exist_ok=True)

        if not file_path.exists():
            with open(file_path, "w") as f:
                f.write(txt)
