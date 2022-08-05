from crud.base import CRUDBase
from models.event import Event
from schemas.event import EventCreate, EventUpdate


class CRUDEvent(CRUDBase[Event, EventCreate, EventUpdate]):
    pass


event = CRUDEvent(Event)
