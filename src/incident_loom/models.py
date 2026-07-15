from __future__ import annotations

from pydantic import BaseModel, Field


class EventRecord(BaseModel):
    timestamp: str
    source: str
    category: str
    message: str
    evidence_id: str
    source_ref: str
    confidence: str
    resource: str | None = None


class EventBundle(BaseModel):
    events: list[EventRecord] = Field(default_factory=list)
