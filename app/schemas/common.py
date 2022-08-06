from __future__ import annotations

from enum import Enum

from pydantic import BaseModel
from pydantic import confloat


class JoinMode(str, Enum):
    """Ways in which event participants can join"""

    online = 'online'
    physical = 'physical'
    hybrid = 'hybrid'


class GeoCoordinates(BaseModel):
    """Schema for a lon-lat geo-location"""

    lon: confloat(ge=-180.0, lt=180.0)  # type: ignore
    lat: confloat(ge=-90.0, lt=90.0)  # type: ignore
