from __future__ import annotations

from crud.base import CRUDBase
from models import calculator
from models.calculator import Calculator
from schemas.calculator import CalculatorCreate
from schemas.calculator import CalculatorUpdate


class CRUDEvent(CRUDBase[Calculator, CalculatorCreate, CalculatorUpdate]):
    pass


calculator = CRUDEvent(Calculator)
