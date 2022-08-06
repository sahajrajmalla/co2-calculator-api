from __future__ import annotations

from typing import Any
from typing import List

import crud
import schemas
from db.database import get_db
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

router = APIRouter()


@router.get('/{id}', response_model=schemas.Calculator)
def read_calculator(
    *,
    db: Session = Depends(get_db),
    id: int,
) -> Any:
    """Get calculator by ID"""
    result = crud.calculator.get(db=db, id=id)
    return result


@router.get('/', response_model=List[schemas.Calculator])
def read_calculators(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """Retrieve calculators"""
    result = crud.calculator.get_multi(db=db, skip=skip, limit=limit)
    return result


@router.post('/', response_model=schemas.Calculator)
def create_calculator(
    *,
    db: Session = Depends(get_db),
    calculator_in: schemas.CalculatorCreate,
) -> Any:
    """Create new calculator"""
    result = crud.calculator.create(db=db, obj_in=calculator_in)
    return result


@router.put('/{id}', response_model=schemas.Calculator)
def update_calculator(
    *,
    db: Session = Depends(get_db),
    id: int,
    calculator_in: schemas.CalculatorUpdate,
) -> Any:
    """Update a calculator"""
    result = crud.calculator.find_and_update(db=db, id=id, obj_in=calculator_in)
    return result


@router.delete('/{id}', response_model=schemas.Calculator)
def delete_calculator(
    *,
    db: Session = Depends(get_db),
    id: int,
) -> Any:
    """Delete a calculator"""
    result = crud.calculator.find_and_remove(db=db, id=id)
    return result
