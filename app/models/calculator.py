# from typing import TYPE_CHECKING
from __future__ import annotations

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Enum
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.database import Base
from app.schemas.calculator import AirTransportClass
from app.schemas.calculator import AirTransportSource
from app.schemas.calculator import DietSource
from app.schemas.calculator import ElectricitySource
from app.schemas.calculator import LandTransportCategory
from app.schemas.calculator import LandTransportVechicle


class Calculator(Base):
    __tablename__ = 'calculators'

    id = Column(Integer, primary_key=True, index=True)

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

    event_id = relationship('Event')
    participant_id = relationship('Participant')

    created_at = Column(DateTime, server_default=func.now())
    modified_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
