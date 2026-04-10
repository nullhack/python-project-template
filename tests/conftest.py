"""Pytest configuration to display BDD docstrings in HTML reports."""

import pytest


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Capture the test function docstring for display in HTML report."""
    outcome = yield
    report = outcome.get_result()
    report.description = item.function.__doc__


def pytest_html_results_table_header(cells):
    """Add a Documentation column to the results table."""
    cells.insert(1, "<th>Documentation</th>")


def pytest_html_results_table_row(report, cells):
    """Populate the Description column with the test docstring."""
    description = getattr(report, "description", None)
    if description:
        # Show full docstring with line breaks for BDD Given/When/Then format
        formatted = description.strip().replace("\n", "<br>")
        cells.insert(1, f"<td>{formatted}</td>")
    else:
        cells.insert(1, "<td></td>")
