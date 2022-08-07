from __future__ import annotations

from typing import Any
from typing import List

from fastapi import APIRouter
from fastapi import Depends
from geopy.geocoders import Nominatim
from sqlalchemy.orm import Session

from app import crud
from app import schemas
from app.db.database import get_db

router = APIRouter()


@router.get('/{id}', response_model=schemas.Event)
def read_event(
    *,
    db: Session = Depends(get_db),
    id: int,
) -> Any:
    """Get event by ID"""
    result = crud.event.get(db=db, id=id)
    return result


@router.get('/', response_model=List[schemas.Event])
def read_events(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """Retrieve events"""
    result = crud.event.get_multi(db=db, skip=skip, limit=limit)
    return result


@router.post('/', response_model=schemas.Event)
def create_event(
    *,
    db: Session = Depends(get_db),
    event_in: schemas.EventCreate,
) -> Any:
    """Create new event"""

    try:
        geolocator = Nominatim(user_agent='geoapiExercises')
        geocode = geolocator.geocode(event_in.address)
        event_in.lat = geocode.latitude
        event_in.lon = geocode.longitude
    except Exception:
        pass
    result = crud.event.create(db=db, obj_in=event_in)
    return result


@router.put('/{id}', response_model=schemas.Event)
def update_event(
    *,
    db: Session = Depends(get_db),
    id: int,
    event_in: schemas.EventUpdate,
) -> Any:
    """Update a event"""
    result = crud.event.find_and_update(db=db, id=id, obj_in=event_in)
    return result


@router.delete('/{id}', response_model=schemas.Event)
def delete_event(
    *,
    db: Session = Depends(get_db),
    id: int,
) -> Any:
    """Delete a event"""
    result = crud.event.find_and_remove(db=db, id=id)
    return result
