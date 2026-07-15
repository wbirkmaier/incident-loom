from pathlib import Path

from incident_loom.adapters import get_summary_provider
from incident_loom.drafting import render_postmortem_draft
from incident_loom.fixtures import load_event_bundle
from incident_loom.timeline import build_timeline


def test_render_postmortem_draft_matches_expected_output() -> None:
    timeline = build_timeline(load_event_bundle(Path("tests/fixtures/incident-evidence")))
    summary = get_summary_provider("none").summarize(timeline)

    assert render_postmortem_draft(timeline, summary) == Path(
        "tests/fixtures/incident-evidence/expected-draft.md"
    ).read_text().rstrip("\n")
