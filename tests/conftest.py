import pytest


def pytest_html_report_title(report):
    report.title = "Test Report"


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    docstring = item.obj.__doc__ or ""
    report.docstrings = docstring


def pytest_html_results_table_header(cells):
    cells.insert(2, "<th>Documentation</th>")


def pytest_html_results_table_row(report, cells):
    docstring = getattr(report, "docstrings", "") or ""
    cells.insert(2, f"<td style='white-space: pre-wrap;'>{docstring}</td>")


def pytest_collection_modifyitems(items):
    """Automatically skip tests marked as deprecated."""
    for item in items:
        if item.get_closest_marker("deprecated"):
            item.add_marker(pytest.mark.skip(reason="deprecated"))
