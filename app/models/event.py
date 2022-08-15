from __future__ import annotations

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Enum
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.sql import func

from app.db.database import Base
from app.schemas.common import JoinMode
# from sqlalchemy import ForeignKey


class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    address = Column(String)
    join_mode = Column(Enum(JoinMode))
    lat = Column(Float)
    lon = Column(Float)

    event_date = Column(String)
    event_time = Column(String)

    thumbnail = Column(String)

    user_id = Column(Integer)
    # participants = Column(Integer)
    # calculators = Column(Integer)

    # user_id = Column(Integer, ForeignKey("users.id"))
    # participants = relationship('Participant', backref='event', lazy='dynamic')
    # calculators = relationship('Calculator', backref='event', lazy='dynamic')

    created_at = Column(DateTime, server_default=func.now())
    modified_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
