# Discovery: temple8

> Append-only session synthesis log.
> Written by the product-owner at the end of each discovery session.
> Each block records one session: a summary paragraph and a table of features whose behaviour changed.
> A row appears only when a `.feature` file would be updated as a result of the session.
> Confirmations of existing behaviour are not recorded here — see `docs/scope_journal.md` for the full Q&A.
> Never edit past blocks — later blocks extend or retire in favour of earlier ones.

---

## Session 2026-04-22

**Summary**: First discovery session for temple8. Established that the product serves Python engineers who want a production-ready project skeleton without setup cost. Confirmed the template ships with exactly one demonstration feature — a CLI entrypoint (`python -m app --help` and `python -m app --version`) implemented entirely in `app/__main__.py` using stdlib only. The feature was chosen for its genuine utility, minimal footprint (zero new dependencies, ~15 lines), and its ability to showcase the full five-step delivery workflow end-to-end.

| Feature | Change | Source questions | Reason |
|---------|--------|-----------------|--------|
| `cli-entrypoint` | created | Q8: "ship with one working demo feature" → one end-to-end example; Q9: "simple useful command, no bloat" → single CLI command; Q11: Option C chosen → `--help` + `--version` combined | New feature: CLI entrypoint with `--help` (prints name, tagline, options, exits 0), `--version` (prints `temple8 <version>` from package metadata, exits 0), and unknown-flag handling (exits 2). All code in `app/__main__.py`, zero new dependencies. |
