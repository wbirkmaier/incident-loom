from __future__ import annotations

import json
from pathlib import Path

from pydantic import ValidationError

from incident_loom.exceptions import IncidentLoomError
from incident_loom.models import EventBundle


def load_event_bundle(fixtures_dir: Path) -> EventBundle:
    path = fixtures_dir / "events.json"
    try:
        return EventBundle.model_validate(json.loads(path.read_text()))
    except FileNotFoundError as error:
        raise IncidentLoomError(f"fixture file not found: {path}") from error
    except ValidationError as error:
        raise IncidentLoomError(f"invalid fixture file: {path}: {error}") from error
