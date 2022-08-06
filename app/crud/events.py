from __future__ import annotations

from app.crud.base import CRUDBase
from app.models.event import Event
from app.schemas.event import EventCreate
from app.schemas.event import EventUpdate


class CRUDEvent(CRUDBase[Event, EventCreate, EventUpdate]):
    pass


event = CRUDEvent(Event)
