from __future__ import annotations

from crud.base import CRUDBase
from models.event import Event
from schemas.event import EventCreate
from schemas.event import EventUpdate


class CRUDEvent(CRUDBase[Event, EventCreate, EventUpdate]):
    pass


event = CRUDEvent(Event)
