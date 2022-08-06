# from typing import TYPE_CHECKING
from __future__ import annotations

from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Enum
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy.sql import func

from app.db.database import Base
from app.schemas.common import JoinMode


class Participant(Base):
    __tablename__ = 'participants'

    id = Column(Integer, primary_key=True, index=True)
    join_mode = Column(Enum(JoinMode))
    lon = Column(Float)
    lat = Column(Float)
    active = Column(Boolean)

    calculator_id = Column(Integer)
    event_id = Column(Integer)
    user_id = Column(Integer)
    # one-to-many collection
    # calculator_id = relationship("Calculator", back_populates="participants")

    # event_id = Column(Integer, ForeignKey('events.id'))

    created_at = Column(DateTime, server_default=func.now())
    modified_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
