from __future__ import annotations

from db.database import Base
from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import String
# from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import relationship


class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    lon = Column(Float)
    lat = Column(Float)
    participants = relationship("Participant")
