import inspect

from _pytest.config import Config
from _pytest.nodes import Item


def pytest_configure(config: Config) -> None:
    """Initialize per-session state for docstring printing.

    Creates a set on the config object used to track which test
    node IDs (without parameterization suffixes) have already had
    their docstrings printed.
    """
    config._printed_docstrings = set()  # type: ignore[attr-defined]


def pytest_runtest_setup(item: Item) -> None:
    """Print a test function's docstring the first time it is encountered.

    The docstring is printed only once per “base” nodeid. For example,
    a parametrized test like ``test_func[param]`` will only have its
    docstring printed for the first parameterization. Subsequent cases
    skip printing.
    """
    tr = item.config.pluginmanager.getplugin("terminalreporter")
    if not tr:
        return

    # strip parameterization suffix:
    # "path/to/test.py::test_func[param]" → keep the part before "["
    base_nodeid = item.nodeid.split("[", 1)[0]

    if base_nodeid in item.config._printed_docstrings:  # type: ignore[attr-defined]
        return

    doc = inspect.getdoc(item.obj) or ""
    if not doc.strip():
        item.config._printed_docstrings.add(base_nodeid)  # type: ignore[attr-defined]
        return

    for line in doc.splitlines():
        tr.write_line("  " + line)
    tr.write_line("")

    item.config._printed_docstrings.add(base_nodeid)  # type: ignore[attr-defined]
