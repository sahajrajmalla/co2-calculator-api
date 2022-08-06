from __future__ import annotations

from app.crud.base import CRUDBase
from app.models.calculator import Calculator
from app.schemas.calculator import CalculatorCreate
from app.schemas.calculator import CalculatorUpdate


class CRUDEvent(CRUDBase[Calculator, CalculatorCreate, CalculatorUpdate]):
    pass


calculator = CRUDEvent(Calculator)
