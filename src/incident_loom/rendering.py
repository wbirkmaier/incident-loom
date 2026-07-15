from __future__ import annotations

from incident_loom.models import EventRecord


def render_markdown(events: list[EventRecord]) -> str:
    lines = ["# Incident Timeline", ""]
    for event in events:
        resource = f" ({event.resource})" if event.resource else ""
        lines.append(
            f"- `{event.timestamp}` [{event.source}/{event.category}] {event.message}{resource} "
            f"evidence=`{event.evidence_id}` confidence=`{event.confidence}`"
        )
    return "\n".join(lines)
