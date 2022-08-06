from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from app.schemas.common import JoinMode

UID = str


class EventBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    address: Optional[str] = None
    join_mode: Optional[JoinMode] = None
    lat: Optional[float] = None
    lon: Optional[float] = None
    year: Optional[int] = None
    month: Optional[int] = None
    day: Optional[int] = None
    hour: Optional[int] = None
    minute: Optional[int] = None
    thumbnail: Optional[str] = None
    user_id: Optional[int] = None
    # participants: List[Participant] = []
    # calculators: List[Calculator] = []


# Properties to receive on event creation
class EventCreate(EventBase):
    name: str
    description: str
    address: str
    join_mode: JoinMode
    lat: float
    lon: float
    year: int
    month: int
    day: int
    hour: int
    minute: int
    thumbnail: str
    user_id: int
    # participants: List[Participant] = []
    # calculators: List[Calculator] = []

    class Config:
        orm_mode = True


# Properties to receive on update
class EventUpdate(EventBase):
    pass


# Properties shared by models stored in DB
class EventInDBBase(EventBase):
    id: int
    name: str
    description: str
    address: str
    join_mode: JoinMode
    lat: float
    lon: float
    year: int
    month: int
    day: int
    hour: int
    minute: int
    thumbnail: str
    user_id: int
    # participants: List[ParticipantInDB] = []
    # calculators: List[CalculatorInDB] = []
    created_at: datetime
    modified_at: datetime

    class Config:
        orm_mode = True


# Properties stored in DB
class EventInDB(EventInDBBase):
    pass


# Properties to return to client
class Event(EventInDBBase):
    pass
