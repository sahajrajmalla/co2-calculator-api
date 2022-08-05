from typing import Any, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import crud, schemas
from db.database import get_db

router = APIRouter()


@router.get("/{id}", response_model=schemas.Participant)
def read_participant(
    *,
    db: Session = Depends(get_db),
    id: int,
) -> Any:
    """Get participant by ID"""
    result = crud.participant.get(db=db, id=id)
    return result


@router.get("/", response_model=List[schemas.Participant])
def read_participants(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """Retrieve participants"""
    result = crud.participant.get_multi(db=db, skip=skip, limit=limit)
    return result


@router.post("/", response_model=schemas.Participant)
def create_participant(
    *,
    db: Session = Depends(get_db),
    participant_in: schemas.ParticipantCreate,
) -> Any:
    """Create new participant"""
    result = crud.participant.create(db=db, obj_in=participant_in)
    return result


@router.put("/{id}", response_model=schemas.Participant)
def update_participant(
    *,
    db: Session = Depends(get_db),
    id: int,
    participant_in: schemas.ParticipantUpdate,
) -> Any:
    """Update a participant"""
    result = crud.participant.find_and_update(db=db, id=id, obj_in=participant_in)
    return result


@router.delete("/{id}", response_model=schemas.Participant)
def delete_participant(
    *,
    db: Session = Depends(get_db),
    id: int,
) -> Any:
    """Delete a participant"""
    result = crud.participant.find_and_remove(db=db, id=id)
    return result
