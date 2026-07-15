from __future__ import annotations

from incident_loom.models import EventRecord
from incident_loom.summarize import SummaryReport


def render_postmortem_draft(events: list[EventRecord], summary: SummaryReport) -> str:
    lines = [
        "# Incident Draft",
        "",
        "## Observations",
    ]
    lines.extend(f"- {observation}" for observation in summary.observations)
    lines.extend(["", "## Timeline"])
    lines.extend(
        f"- `{event.timestamp}` {event.message} (evidence `{event.evidence_id}`)"
        for event in events
    )
    lines.extend(
        ["", "## Notes", "- Root cause not yet established from the current evidence set."]
    )
    return "\n".join(lines)
