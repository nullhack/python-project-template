import inspect
from typing import Any

from _pytest.config import Config
from _pytest.nodes import Item


def pytest_configure(config: Config) -> None:
    """Initialize per-session state for docstring printing.

    Creates a set on the config object used to track which test
    node IDs (without parameterization suffixes) have already had
    their docstrings printed.
    """
    # use getattr/setattr to avoid static-type warnings about unknown attrs
    if getattr(config, "_printed_docstrings", None) is None:
        setattr(config, "_printed_docstrings", set())


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

    printed = getattr(item.config, "_printed_docstrings", set())
    if base_nodeid in printed:
        return

    # obtain the underlying Python object for the test in a safe way
    # different pytest versions / stubs expose different attributes; try common ones
    obj: Any = getattr(item, "obj", None) or getattr(item, "function", None) or item

    doc = inspect.getdoc(obj) or ""
    if not doc.strip():
        printed.add(base_nodeid)
        setattr(item.config, "_printed_docstrings", printed)
        return

    # call write_line if available; otherwise fall back to a write() if present
    write_line = getattr(tr, "write_line", None)
    if callable(write_line):
        for line in doc.splitlines():
            write_line("  " + line)
        write_line("")
    else:
        write = getattr(tr, "write", None)
        if callable(write):
            # write() often expects raw text including newline
            for line in doc.splitlines():
                write("  " + line + "\n")
            write("\n")

    printed.add(base_nodeid)
    setattr(item.config, "_printed_docstrings", printed)
