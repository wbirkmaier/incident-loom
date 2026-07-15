from pathlib import Path

from incident_loom.fixtures import load_event_bundle
from incident_loom.timeline import build_timeline


def test_build_timeline_sorts_by_timestamp_then_evidence_id() -> None:
    timeline = build_timeline(load_event_bundle(Path("tests/fixtures/incident-evidence")))

    assert [event.evidence_id for event in timeline] == [
        "github-note-1",
        "k8s-event-1",
        "prom-alert-1",
    ]
