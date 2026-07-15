from pathlib import Path

from incident_loom.fixtures import load_event_bundle
from incident_loom.rendering import render_markdown
from incident_loom.timeline import build_timeline


def test_render_markdown_matches_expected_output() -> None:
    timeline = build_timeline(load_event_bundle(Path("tests/fixtures/incident-evidence")))

    assert render_markdown(timeline) == Path(
        "tests/fixtures/incident-evidence/expected-render.md"
    ).read_text().rstrip("\n")
