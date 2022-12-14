# from typing import TYPE_CHECKING
from __future__ import annotations

from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Enum
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.sql import func

from app.db.database import Base
from app.schemas.common import JoinMode
from app.schemas.participant import AirTransportClass
from app.schemas.participant import AirTransportSource
from app.schemas.participant import DietSource
from app.schemas.participant import ElectricitySource
from app.schemas.participant import LandTransportCategory
from app.schemas.participant import LandTransportVechicle
# from typing import TYPE_CHECKING
# from typing import TYPE_CHECKING


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
    source_location_lon = Column(Float)
    destination_event_lat = Column(Float)
    source_airport_lon = Column(Float)
    destination_airport_lat = Column(Float)

    category_home_to_airport = Column(Enum(LandTransportCategory))
    vechicle_home_to_airport = Column(Enum(LandTransportVechicle))
    size_home_to_airport = Column(String)
    unit_home_to_airport = Column(String)
    factor_home_to_airport = Column(Integer)

    source_airport_to_airport = Column(Enum(AirTransportSource))
    class_airport_to_airport = Column(Enum(AirTransportClass))
    unit_airport_to_airport = Column(String)
    distance_airport_to_airport = Column(String)
    factor_airport_to_airport = Column(Integer)

    category_airport_to_event = Column(Enum(LandTransportCategory))
    vechicle_airport_to_event = Column(Enum(LandTransportVechicle))
    unit_airport_to_event = Column(String)
    size_airport_to_event = Column(String)
    factor_airport_to_event = Column(Integer)

    source_diet = Column(Enum(DietSource))
    factor_diet = Column(Integer)
    unit_diet = Column(String)

    source_electricity = Column(Enum(ElectricitySource))
    factor_electricity = Column(Integer)
    unit_electricity = Column(String)

    event_id = Column(Integer)
    # participants

    # event_id = Column(Integer, ForeignKey("events.id"))

    # participants_id = Column(Integer, ForeignKey("participants.id"))
    # participants = relationship("Participant", back_populates="calculator_id")

    created_at = Column(DateTime, server_default=func.now())
    modified_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
