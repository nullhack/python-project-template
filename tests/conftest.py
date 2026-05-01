import pytest


def pytest_collection_modifyitems(items):
    skip_deprecated = pytest.mark.skip(reason="deprecated acceptance criterion")
    for item in items:
        if "deprecated" in item.keywords:
            item.add_marker(skip_deprecated)
