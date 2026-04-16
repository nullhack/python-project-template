"""Generate and sync pytest test stubs from Gherkin .feature files.

Scans all feature folders under docs/features/{backlog,in-progress,completed}/
and creates or updates test stubs in tests/features/<feature-name>/.

Modes:
    uv run task gen-tests              Sync all features (default)
    uv run task gen-tests -- --check   Dry run — report what would change
    uv run task gen-tests -- --orphans List orphaned tests (no matching @id)

Safety rules:
    - backlog / in-progress: full write (create stubs, update docstrings, rename)
    - completed: only toggle @pytest.mark.deprecated (no docstring changes)
    - Never touches function bodies (code between # Given and end of function)
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from gherkin import Parser as GherkinParser

PROJECT_ROOT = Path(__file__).resolve().parents[4]
FEATURES_DIR = PROJECT_ROOT / "docs" / "features"
TESTS_DIR = PROJECT_ROOT / "tests" / "features"

FEATURE_STAGES = ("backlog", "in-progress", "completed")

ID_TAG_RE = re.compile(r"@id:([a-f0-9]{8})")

TEST_FUNC_RE = re.compile(r"^def (test_\w+)\(.*\)")
TEST_ID_RE = re.compile(r"test_\w+_([a-f0-9]{8})\b")
DEPRECATED_MARKER_RE = re.compile(r"^@pytest\.mark\.deprecated$", re.MULTILINE)
ORPHAN_MARKER_RE = re.compile(
    r'^@pytest\.mark\.skip\(reason="orphan: no matching @id in \.feature files"\)$',
    re.MULTILINE,
)


@dataclass(frozen=True, slots=True)
class GherkinExample:
    """A single Example block parsed from a .feature file."""

    id_hex: str
    title: str
    given: str
    when: str
    then: str
    deprecated: bool
    source_file: str


@dataclass(frozen=True, slots=True)
class FeatureFile:
    """A parsed .feature file with its examples."""

    path: Path
    feature_name: str
    story_slug: str
    examples: list[GherkinExample]


def slugify(name: str) -> str:
    """Convert a feature folder name to a Python-safe slug.

    Args:
        name: The feature folder name (kebab-case).

    Returns:
        Underscore-separated lowercase string.
    """
    return name.replace("-", "_").lower()


def parse_feature_file(path: Path) -> FeatureFile | None:
    """Parse a .feature file into structured data.

    Args:
        path: Path to the .feature file.

    Returns:
        FeatureFile if valid, None if no Feature: line found.
    """
    text = path.read_text(encoding="utf-8")
    doc = GherkinParser().parse(text)
    feature: dict[str, Any] | None = doc.get("feature")
    if not feature or not feature.get("name"):
        return None

    story_slug = path.stem
    examples = _extract_examples(feature, str(path))
    return FeatureFile(
        path=path,
        feature_name=feature["name"],
        story_slug=story_slug,
        examples=examples,
    )


def _extract_examples(
    feature: dict[str, Any], source_file: str
) -> list[GherkinExample]:
    """Extract all Example blocks from a parsed Gherkin feature AST.

    Args:
        feature: The 'feature' dict from gherkin-official Parser output.
        source_file: Path string for provenance tracking.

    Returns:
        List of parsed GherkinExample objects.
    """
    examples: list[GherkinExample] = []
    for child in feature.get("children", []):
        scenario: dict[str, Any] | None = child.get("scenario")
        if scenario is None:
            continue
        example = _scenario_to_example(scenario, source_file)
        if example is not None:
            examples.append(example)
    return examples


def _scenario_to_example(
    scenario: dict[str, Any], source_file: str
) -> GherkinExample | None:
    """Convert a single parsed scenario dict to a GherkinExample.

    Skips scenarios without an @id tag.

    Args:
        scenario: A scenario dict from the Gherkin AST.
        source_file: Path string for provenance tracking.

    Returns:
        GherkinExample if the scenario has an @id tag, None otherwise.
    """
    tags = scenario.get("tags", [])
    id_hex = _extract_id_tag(tags)
    if id_hex is None:
        return None

    deprecated = any(t["name"] == "@deprecated" for t in tags)
    given, when, then = _extract_steps(scenario.get("steps", []))
    return GherkinExample(
        id_hex=id_hex,
        title=scenario.get("name", ""),
        given=given,
        when=when,
        then=then,
        deprecated=deprecated,
        source_file=source_file,
    )


def _extract_id_tag(tags: list[dict[str, Any]]) -> str | None:
    """Find the @id:<hex> tag value from a list of AST tags.

    Args:
        tags: List of tag dicts from the Gherkin AST.

    Returns:
        The 8-char hex ID, or None if no @id tag is present.
    """
    for tag in tags:
        m = ID_TAG_RE.search(tag.get("name", ""))
        if m:
            return m.group(1)
    return None


def _extract_steps(steps: list[dict[str, Any]]) -> tuple[str, str, str]:
    """Extract Given/When/Then text from parsed Gherkin steps.

    Args:
        steps: List of step dicts from the Gherkin AST.

    Returns:
        Tuple of (given, when, then) step text strings.
    """
    given = when = then = ""
    for step in steps:
        keyword_type = step.get("keywordType", "")
        text = step.get("text", "")
        if keyword_type == "Context":
            given = text
        elif keyword_type == "Action":
            when = text
        elif keyword_type == "Outcome":
            then = text
    return given, when, then


def generate_stub(feature_slug: str, example: GherkinExample) -> str:
    """Generate a single test stub function.

    Args:
        feature_slug: Underscored feature folder name.
        example: The parsed Gherkin example.

    Returns:
        Complete test function source code as a string.
    """
    func_name = f"test_{feature_slug}_{example.id_hex}"
    markers = ["@pytest.mark.unit"]
    if example.deprecated:
        markers.append("@pytest.mark.deprecated")

    marker_lines = "\n".join(markers)
    docstring = _build_docstring(example)

    lines = [
        marker_lines,
        f"def {func_name}() -> None:",
        *docstring,
        "    # Given",
        "",
        "    # When",
        "",
        "    # Then",
        "    raise NotImplementedError",
    ]
    return "\n".join(lines) + "\n"


def _build_docstring(example: GherkinExample) -> list[str]:
    """Build properly indented docstring lines for a test stub.

    Args:
        example: The parsed Gherkin example.

    Returns:
        List of indented lines (each with 4-space prefix) including triple quotes.
    """
    return [
        '    """',
        f"    Given: {example.given}",
        f"    When: {example.when}",
        f"    Then: {example.then}",
        '    """',
    ]


def generate_test_file(
    feature_slug: str, story_slug: str, examples: list[GherkinExample]
) -> str:
    """Generate a complete test file for one .feature file.

    Args:
        feature_slug: Underscored feature folder name.
        story_slug: The story file stem (becomes test file name).
        examples: All examples from that .feature file.

    Returns:
        Complete test module source code.
    """
    header = (
        f'"""Tests for {story_slug.replace("_", " ")} story."""\n\nimport pytest\n\n\n'
    )
    stubs = "\n\n".join(generate_stub(feature_slug, ex) for ex in examples)
    return header + stubs + "\n"


def find_feature_folders() -> dict[str, list[tuple[Path, str]]]:
    """Find all feature folders across all stages.

    Returns:
        Dict mapping feature folder name to list of (feature_file_path, stage).
    """
    features: dict[str, list[tuple[Path, str]]] = {}
    for stage in FEATURE_STAGES:
        stage_dir = FEATURES_DIR / stage
        if not stage_dir.exists():
            continue
        for folder in sorted(stage_dir.iterdir()):
            if not folder.is_dir():
                continue
            feature_files = sorted(folder.glob("*.feature"))
            if feature_files:
                name = folder.name
                features.setdefault(name, [])
                for ff in feature_files:
                    features[name].append((ff, stage))
    return features


def read_existing_test_ids(test_file: Path) -> set[str]:
    """Extract @id hex values from existing test function names.

    Args:
        test_file: Path to existing test file.

    Returns:
        Set of 8-char hex IDs found in test function names.
    """
    if not test_file.exists():
        return set()
    text = test_file.read_text(encoding="utf-8")
    return set(TEST_ID_RE.findall(text))


def sync_test_file(
    feature_slug: str,
    story_slug: str,
    examples: list[GherkinExample],
    test_file: Path,
    stage: str,
    *,
    check_only: bool = False,
) -> list[str]:
    """Sync a single test file with its .feature examples.

    Args:
        feature_slug: Underscored feature folder name.
        story_slug: The story file stem.
        examples: Parsed examples from the .feature file.
        test_file: Path to the test file to create/update.
        stage: Feature stage (backlog, in-progress, completed).
        check_only: If True, report changes without writing.

    Returns:
        List of action descriptions taken/planned.
    """
    actions: list[str] = []
    example_ids = {ex.id_hex for ex in examples}

    if not test_file.exists():
        if stage == "completed":
            return actions
        content = generate_test_file(feature_slug, story_slug, examples)
        actions.append(f"CREATE {test_file} ({len(examples)} stubs)")
        if not check_only:
            test_file.parent.mkdir(parents=True, exist_ok=True)
            test_file.write_text(content, encoding="utf-8")
        return actions

    text = test_file.read_text(encoding="utf-8")
    existing_ids = set(TEST_ID_RE.findall(text))

    if stage == "completed":
        actions.extend(_sync_deprecated_markers(examples, test_file, text, check_only))
        return actions

    actions.extend(
        _sync_full(
            feature_slug,
            examples,
            example_ids,
            existing_ids,
            test_file,
            text,
            check_only,
        )
    )
    return actions


def _sync_deprecated_markers(
    examples: list[GherkinExample],
    test_file: Path,
    text: str,
    check_only: bool,
) -> list[str]:
    """For completed features, only toggle @deprecated markers.

    Args:
        examples: Parsed examples from the .feature file.
        test_file: Path to the test file.
        text: Current content of the test file.
        check_only: If True, report without writing.

    Returns:
        List of action descriptions.
    """
    actions: list[str] = []
    modified = text
    for ex in examples:
        func_pattern = re.compile(
            rf"((?:@pytest\.mark\.\w+(?:\(.*?\))?\n)*)def test_\w+_{ex.id_hex}\b"
        )
        match = func_pattern.search(modified)
        if not match:
            continue
        decorators = match.group(1)
        has_deprecated = "@pytest.mark.deprecated" in decorators
        if ex.deprecated and not has_deprecated:
            new_decorators = "@pytest.mark.deprecated\n" + decorators
            modified = (
                modified[: match.start()]
                + new_decorators
                + match.group()[len(decorators) :]
                + modified[match.end() :]
            )
            actions.append(f"ADD @deprecated to test for {ex.id_hex}")
        elif not ex.deprecated and has_deprecated:
            new_decorators = decorators.replace("@pytest.mark.deprecated\n", "")
            modified = (
                modified[: match.start()]
                + new_decorators
                + match.group()[len(decorators) :]
                + modified[match.end() :]
            )
            actions.append(f"REMOVE @deprecated from test for {ex.id_hex}")
    if modified != text and not check_only:
        test_file.write_text(modified, encoding="utf-8")
    return actions


def _sync_full(
    feature_slug: str,
    examples: list[GherkinExample],
    example_ids: set[str],
    existing_ids: set[str],
    test_file: Path,
    text: str,
    check_only: bool,
) -> list[str]:
    """Full sync for backlog/in-progress features.

    Args:
        feature_slug: Underscored feature folder name.
        examples: Parsed examples.
        example_ids: Set of IDs from .feature file.
        existing_ids: Set of IDs found in existing test file.
        test_file: Path to test file.
        text: Current file content.
        check_only: Dry run flag.

    Returns:
        List of action descriptions.
    """
    actions: list[str] = []
    modified = text

    new_ids = example_ids - existing_ids
    orphan_ids = existing_ids - example_ids

    for ex in examples:
        if ex.id_hex in new_ids:
            stub = "\n\n" + generate_stub(feature_slug, ex)
            modified += stub
            actions.append(f"ADD stub for @id:{ex.id_hex}")
        elif ex.id_hex in existing_ids:
            modified, doc_actions = _update_docstring(modified, feature_slug, ex)
            actions.extend(doc_actions)

    for oid in orphan_ids:
        orphan_marker = (
            '@pytest.mark.skip(reason="orphan: no matching @id in .feature files")'
        )
        func_pattern = re.compile(
            rf"((?:@pytest\.mark\.\w+(?:\(.*?\))?\n)*)def test_\w+_{oid}\b"
        )
        match = func_pattern.search(modified)
        if match and orphan_marker not in match.group(1):
            decorators = match.group(1)
            new_decorators = orphan_marker + "\n" + decorators
            modified = (
                modified[: match.start()]
                + new_decorators
                + match.group()[len(decorators) :]
                + modified[match.end() :]
            )
            actions.append(f"MARK orphan: test with @id:{oid}")

    if modified != text and not check_only:
        test_file.write_text(modified, encoding="utf-8")
    return actions


def _update_docstring(
    text: str, feature_slug: str, example: GherkinExample
) -> tuple[str, list[str]]:
    """Update the docstring of an existing test to match the .feature file.

    Args:
        text: Full test file content.
        feature_slug: Underscored feature folder name.
        example: The Gherkin example to match.

    Returns:
        Tuple of (modified_text, list_of_actions).
    """
    actions: list[str] = []
    func_re = re.compile(
        rf'(def test_\w+_{example.id_hex}\(.*?\).*?:\n\s+""")'
        rf"(.*?)"
        rf'(""")',
        re.DOTALL,
    )
    match = func_re.search(text)
    if not match:
        return text, actions

    new_docstring = (
        f"\n    Given: {example.given}\n"
        f"    When: {example.when}\n"
        f"    Then: {example.then}\n    "
    )
    old_docstring = match.group(2)
    if old_docstring.strip() != new_docstring.strip():
        text = text[: match.start(2)] + new_docstring + text[match.end(2) :]
        actions.append(f"UPDATE docstring for @id:{example.id_hex}")

    old_func = re.search(rf"def (test_\w+_{example.id_hex})\b", text)
    if old_func:
        expected_name = f"test_{feature_slug}_{example.id_hex}"
        if old_func.group(1) != expected_name:
            text = text.replace(old_func.group(1), expected_name)
            actions.append(f"RENAME {old_func.group(1)} -> {expected_name}")
    return text, actions


def find_duplicate_ids() -> list[str]:
    """Find @id hex values that appear in more than one .feature file.

    Args:
        None.

    Returns:
        List of warning strings describing each duplicate @id.
    """
    id_sources: dict[str, list[str]] = {}
    for name, files in find_feature_folders().items():
        for fpath, _stage in files:
            parsed = parse_feature_file(fpath)
            if not parsed:
                continue
            for ex in parsed.examples:
                id_sources.setdefault(ex.id_hex, []).append(f"{name}/{fpath.name}")

    warnings: list[str] = []
    for id_hex, sources in sorted(id_sources.items()):
        if len(sources) > 1:
            locations = ", ".join(sources)
            warnings.append(f"@id:{id_hex} appears in multiple features: {locations}")
    return warnings


def find_orphaned_tests() -> list[str]:
    """Find all test files with IDs that don't match any .feature file.

    Returns:
        List of orphan descriptions.
    """
    all_feature_ids: set[str] = set()
    features = find_feature_folders()
    for name, files in features.items():
        for fpath, _stage in files:
            parsed = parse_feature_file(fpath)
            if parsed:
                all_feature_ids.update(ex.id_hex for ex in parsed.examples)

    orphans: list[str] = []
    if not TESTS_DIR.exists():
        return orphans
    for test_file in TESTS_DIR.rglob("*_test.py"):
        ids = read_existing_test_ids(test_file)
        for tid in ids:
            if tid not in all_feature_ids:
                orphans.append(f"{test_file}: @id:{tid}")
    return orphans


def main() -> int:
    """Entry point for the gen-tests command.

    Returns:
        Exit code (0 = success, 1 = changes needed in check mode).
    """
    check_only = "--check" in sys.argv
    orphans_only = "--orphans" in sys.argv

    if orphans_only:
        orphans = find_orphaned_tests()
        if orphans:
            print("Orphaned tests (no matching @id in .feature files):")
            for o in orphans:
                print(f"  {o}")
            return 1
        print("No orphaned tests found.")
        return 0

    features = find_feature_folders()
    if not features:
        print("No feature folders with .feature files found.")
        return 0

    duplicates = find_duplicate_ids()
    for warning in duplicates:
        print(f"WARNING: {warning}")

    all_actions: list[str] = []
    for name, files in sorted(features.items()):
        feature_slug = slugify(name)
        for fpath, stage in files:
            parsed = parse_feature_file(fpath)
            if not parsed:
                print(f"SKIP {fpath} — no Feature: line found")
                continue
            story_slug = slugify(parsed.story_slug)
            test_dir = TESTS_DIR / name
            test_file = test_dir / f"{story_slug}_test.py"
            actions = sync_test_file(
                feature_slug,
                story_slug,
                parsed.examples,
                test_file,
                stage,
                check_only=check_only,
            )
            all_actions.extend(actions)

    if all_actions:
        mode = "Would" if check_only else "Did"
        print(f"{mode} perform {len(all_actions)} action(s):")
        for a in all_actions:
            print(f"  {a}")
        return 1 if check_only else 0

    print("All test stubs are in sync.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
