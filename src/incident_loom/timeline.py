from __future__ import annotations

from incident_loom.models import EventBundle, EventRecord


def build_timeline(bundle: EventBundle) -> list[EventRecord]:
    return sorted(bundle.events, key=lambda item: (item.timestamp, item.evidence_id))
