from __future__ import annotations

from dataclasses import dataclass

from incident_loom.exceptions import IncidentLoomError
from incident_loom.models import EventRecord
from incident_loom.summarize import SummaryReport, summarize_timeline


class SummaryProviderAdapter:
    def summarize(self, events: list[EventRecord]) -> SummaryReport:
        raise NotImplementedError


@dataclass(frozen=True)
class NoneSummaryProviderAdapter(SummaryProviderAdapter):
    def summarize(self, events: list[EventRecord]) -> SummaryReport:
        return summarize_timeline(events, "none")


@dataclass(frozen=True)
class OllamaSummaryProviderAdapter(SummaryProviderAdapter):
    def summarize(self, events: list[EventRecord]) -> SummaryReport:
        raise IncidentLoomError("ollama summary provider is not implemented in this cycle")


@dataclass(frozen=True)
class BedrockSummaryProviderAdapter(SummaryProviderAdapter):
    def summarize(self, events: list[EventRecord]) -> SummaryReport:
        raise IncidentLoomError("bedrock summary provider is not implemented in this cycle")


def get_summary_provider(name: str) -> SummaryProviderAdapter:
    if name == "none":
        return NoneSummaryProviderAdapter()
    if name == "ollama":
        return OllamaSummaryProviderAdapter()
    if name == "bedrock":
        return BedrockSummaryProviderAdapter()
    raise IncidentLoomError(f"unsupported summary provider: {name}")
