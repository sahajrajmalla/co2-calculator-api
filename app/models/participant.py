# from typing import TYPE_CHECKING
from __future__ import annotations

from db.database import Base
from schemas.common import JoinMode
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Enum
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer

# if TYPE_CHECKING:
#     from .event import Event  # noqa


class Participant(Base):
    __tablename__ = 'participants'

    id = Column(Integer, primary_key=True, index=True)
    join_mode = Column(Enum(JoinMode))
    lon = Column(Float)
    lat = Column(Float)
    active = Column(Boolean)
    event_id = Column(Integer, ForeignKey('events.id'))
