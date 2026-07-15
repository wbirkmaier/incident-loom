from pathlib import Path

from incident_loom.fixtures import load_event_bundle
from incident_loom.summarize import summarize_timeline
from incident_loom.timeline import build_timeline


def test_summarize_timeline_none_provider_returns_observations() -> None:
    timeline = build_timeline(load_event_bundle(Path("tests/fixtures/incident-evidence")))

    summary = summarize_timeline(timeline, "none")

    assert summary.provider == "none"
    assert summary.evidence_ids == ["github-note-1", "k8s-event-1", "prom-alert-1"]
