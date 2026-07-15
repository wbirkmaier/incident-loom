from __future__ import annotations

from pydantic import BaseModel

from incident_loom.exceptions import IncidentLoomError
from incident_loom.models import EventRecord


class SummaryReport(BaseModel):
    provider: str
    observations: list[str]
    evidence_ids: list[str]


def summarize_timeline(events: list[EventRecord], provider: str) -> SummaryReport:
    if provider != "none":
        raise IncidentLoomError(f"unsupported summary provider: {provider}")

    first = events[0].timestamp if events else "unknown"
    last = events[-1].timestamp if events else "unknown"
    observations = [
        f"Timeline contains {len(events)} normalized events between {first} and {last}.",
        f"Sources observed: {', '.join(sorted({event.source for event in events}))}.",
    ]
    return SummaryReport(
        provider=provider,
        observations=observations,
        evidence_ids=[event.evidence_id for event in events],
    )
