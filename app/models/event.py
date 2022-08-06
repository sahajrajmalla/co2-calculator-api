from __future__ import annotations

from db.database import Base
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
# from sqlalchemy import ForeignKey


class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    lon = Column(Float)
    lat = Column(Float)
    participants = relationship('Participant')
    calculator_id = Column(Integer, ForeignKey('calculators.id'))

    created_at = Column(DateTime, server_default=func.now())
    modified_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
