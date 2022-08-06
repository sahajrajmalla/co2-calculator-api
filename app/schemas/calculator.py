from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class DietSource(str, Enum):
    """Different diets that participants can choose"""

    vegan = 'vegan'
    vegetarian = 'vegetarian'
    nonvegan = 'nonvegan'


class ElectricitySource(str, Enum):
    """Different electricity options that participants can choose"""

    renewable = 'renewable'
    nonrenewable = 'nonrenewable'


class LandTransportCategory(str, Enum):
    """Different electricity categoreis options that participants can choose"""

    private = 'private'
    public = 'public'


class LandTransportVechicle(str, Enum):
    """Different electricity vechiles options that participants can choose"""

    car = 'car'
    petrol_hybrids = 'petrol_hybrids'
    taxi = 'taxi'
    bus = 'bus'
    train = 'train'
    bike = 'bike'
    walk = 'walk'
    electric_car = 'electric_car'


class AirTransportSource(str, Enum):
    """Different electricity sources options that participants can choose"""

    domestic = 'domestic'
    short_haul_international = 'short_haul_international'
    long_haul_international = 'long_haul_international'


class AirTransportClass(str, Enum):
    """Different electricity classes options that participants can choose"""

    average = 'average'
    economy = 'economy'
    business = 'business'
    premium_economy = 'premium_economy'
    first = 'first'


class CalculatorBase(BaseModel):
    source_location_lon: Optional[float] = None
    destination_event_lat: Optional[float] = None
    source_airport_lon: Optional[float] = None
    destination_airport_lat: Optional[float] = None

    category_home_to_airport: Optional[LandTransportCategory] = None
    vechicle_home_to_airport: Optional[LandTransportVechicle] = None
    size_home_to_airport: Optional[str] = None
    unit_home_to_airport: Optional[str] = None
    factor_home_to_airport: Optional[int] = None

    source_airport_to_airport: Optional[AirTransportSource] = None
    class_airport_to_airport: Optional[AirTransportClass] = None
    unit_airport_to_airport: Optional[str] = None
    distance_airport_to_airport: Optional[str] = None
    factor_airport_to_airport: Optional[int] = None

    category_airport_to_event: Optional[LandTransportCategory] = None
    vechicle_airport_to_event: Optional[LandTransportVechicle] = None
    unit_airport_to_event: Optional[str] = None
    size_airport_to_event: Optional[str] = None
    factor_airport_to_event: Optional[int] = None

    source_diet: Optional[DietSource] = None
    factor_diet: Optional[int] = None
    unit_diet: Optional[str] = None

    source_electricity: Optional[ElectricitySource] = None
    factor_electricity: Optional[int] = None
    unit_electricity: Optional[str] = None

    event_id: Optional[int] = None
    participants_id: Optional[int] = None


class CalculatorCreate(CalculatorBase):
    source_location_lon: float
    destination_event_lat: float
    source_airport_lon: float
    destination_airport_lat: float

    category_home_to_airport: LandTransportCategory
    vechicle_home_to_airport: LandTransportVechicle
    size_home_to_airport: str
    unit_home_to_airport: str
    factor_home_to_airport: int

    source_airport_to_airport: AirTransportSource
    class_airport_to_airport: AirTransportClass
    unit_airport_to_airport: str
    distance_airport_to_airport: str
    factor_airport_to_airport: int

    category_airport_to_event: LandTransportCategory
    vechicle_airport_to_event: LandTransportVechicle
    unit_airport_to_event: str
    size_airport_to_event: str
    factor_airport_to_event: int

    source_diet: DietSource
    factor_diet: int
    unit_diet: str

    source_electricity: ElectricitySource
    factor_electricity: int
    unit_electricity: str

    event_id: int
    participants_id: int


class CalculatorUpdate(CalculatorBase):
    pass


class CalculatorInDBBase(CalculatorBase):
    id: int

    source_location_lon: float
    destination_event_lat: float
    source_airport_lon: float
    destination_airport_lat: float

    category_home_to_airport: LandTransportCategory
    vechicle_home_to_airport: LandTransportVechicle
    size_home_to_airport: str
    unit_home_to_airport: str
    factor_home_to_airport: int

    source_airport_to_airport: AirTransportSource
    class_airport_to_airport: AirTransportClass
    unit_airport_to_airport: str
    distance_airport_to_airport: str
    factor_airport_to_airport: int

    category_airport_to_event: LandTransportCategory
    vechicle_airport_to_event: LandTransportVechicle
    unit_airport_to_event: str
    size_airport_to_event: str
    factor_airport_to_event: int

    source_diet: DietSource
    factor_diet: int
    unit_diet: str

    source_electricity: ElectricitySource
    factor_electricity: int
    unit_electricity: str

    event_id: int
    participants_id: int

    created_at: datetime
    modified_at: datetime

    class Config:
        orm_mode = True


# Properties stored in DB
class CalculatorInDB(CalculatorInDBBase):
    pass


# Properties to return to client
class Calculator(CalculatorInDBBase):
    pass
