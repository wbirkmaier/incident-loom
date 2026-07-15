from pathlib import Path

from incident_loom.adapters import (
    BedrockSummaryProviderAdapter,
    NoneSummaryProviderAdapter,
    OllamaSummaryProviderAdapter,
)
from incident_loom.exceptions import IncidentLoomError
from incident_loom.fixtures import load_event_bundle
from incident_loom.summarize import summarize_timeline
from incident_loom.timeline import build_timeline


def test_summarize_timeline_none_provider_returns_observations() -> None:
    timeline = build_timeline(load_event_bundle(Path("tests/fixtures/incident-evidence")))

    summary = summarize_timeline(timeline, "none")

    assert summary.provider == "none"
    assert summary.evidence_ids == ["github-note-1", "k8s-event-1", "prom-alert-1"]


def test_none_provider_adapter_uses_deterministic_summary() -> None:
    timeline = build_timeline(load_event_bundle(Path("tests/fixtures/incident-evidence")))

    assert NoneSummaryProviderAdapter().summarize(timeline).provider == "none"


def test_unimplemented_provider_adapters_fail_explicitly() -> None:
    timeline = build_timeline(load_event_bundle(Path("tests/fixtures/incident-evidence")))

    for provider in (OllamaSummaryProviderAdapter(), BedrockSummaryProviderAdapter()):
        try:
            provider.summarize(timeline)
        except IncidentLoomError:
            continue
        raise AssertionError("expected IncidentLoomError")
