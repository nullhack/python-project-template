"""Tests module."""

import pytest


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_terminal_summary(terminalreporter, exitstatus, config):
    if not getattr(config.option, "cov_source", None):
        yield
        return

    cov_report = getattr(config.option, "cov_report", None) or []
    if any(r and r.startswith("term") for r in cov_report):
        yield
        return

    captured = []
    orig_write = terminalreporter.write
    orig_sep = terminalreporter.write_sep

    def _cap(*a, **kw):
        captured.append(("w", a, kw))

    def _sep(*a, **kw):
        captured.append(("s", a, kw))

    terminalreporter.write = _cap
    terminalreporter.write_sep = _sep
    yield
    terminalreporter.write = orig_write
    terminalreporter.write_sep = orig_sep

    if exitstatus != 0:
        for kind, args, kwargs in captured:
            (orig_write if kind == "w" else orig_sep)(*args, **kwargs)
