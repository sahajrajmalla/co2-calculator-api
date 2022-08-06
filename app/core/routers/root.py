from __future__ import annotations

import random
import shutil
from datetime import datetime
from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import File
from fastapi import status
from fastapi import UploadFile
from geopy.geocoders import Nominatim
from sqlalchemy.orm import Session

from app.core.auth.jwt_token import get_current_user
from app.core.repositories.distance import get_top_cloest_airport
from app.core.repositories.distance import measure_geodesic_distance
from app.core.repositories.factor import fetch_factor_data
from app.db.database import get_db
from app.models.calculator import Calculator
from app.models.event import Event
from app.models.participant import Participant
from app.models.user import User
from app.schemas import CalculatorInDB
from app.schemas import EventInDB
from app.schemas import ParticipantInDB

router = APIRouter(prefix='', tags=['Root'])


@router.get('/health')
def check_health():
    return {'status': 'ok'}


@router.get('/check_auth', response_model=str)
def check_auth(current_user: User = Depends(get_current_user)):
    return 'Hello World!'


@router.get('/get_factor_data', response_model=dict)
def get_factor_data():
    response_data = fetch_factor_data()
    return response_data


@router.get('/get_nearest_airport', response_model=list)
def get_nearest_airport(lat: float, lon: float):
    response_data = get_top_cloest_airport(lat, lon)
    return response_data


@router.get('/get_geodesic_distance', response_model=int)
def get_geodesic_distance(lat1: float, lon1: float, lat2: float, lon2: float):
    response_data = measure_geodesic_distance(lat1, lon1, lat2, lon2)
    return response_data


@router.get('/fetch_event', response_model=List[EventInDB], status_code=status.HTTP_200_OK)
def filter_event_by_user_id(user_id: int, db: Session = Depends(get_db)):
    item = db.query(Event).filter(Event.user_id == user_id).all()
    return item


@router.get('/fetch_calculator', response_model=List[CalculatorInDB], status_code=status.HTTP_200_OK)
def filter_calculator_by_event_id(event_id: int, db: Session = Depends(get_db)):
    item = db.query(Calculator).filter(Calculator.event_id == event_id).all()
    return item


@router.get('/fetch_participants', response_model=List[ParticipantInDB], status_code=status.HTTP_200_OK)
def filter_participants_by_event_id(user_id: int, db: Session = Depends(get_db)):
    item = db.query(Participant).filter(Participant.user_id == user_id).all()
    return item


@router.get('/fetch_lat_lng', response_model=dict, status_code=status.HTTP_200_OK)
def fetch_lat_lng(address: str):
    try:
        geolocator = Nominatim(user_agent='geoapiExercises')
        geocode = geolocator.geocode(address)
        response = {
            'address': address,
            'lat': geocode.latitude, 'lng': geocode.longitude,
        }

        return response
    except Exception:
        return {'error': 'Could not find address'}


@router.post(
    '/upload_file', response_model=str,
    status_code=status.HTTP_201_CREATED,
)
def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):

    now = datetime.now()
    url = str(f'media/{now}_{file.filename}')

    with open(url, 'wb+') as image:
        shutil.copyfileobj(file.file, image)

    return url


@router.get('/search', response_model=List[EventInDB], status_code=status.HTTP_200_OK)
def search_items(query: str, db: Session = Depends(get_db)):
    items = db.query(Event).filter(
        Event.name.contains(query) | Event.address.contains(
            query,
        ) | Event.join_mode.contains(query) | Event.description.contains(query),
    ).all()
    random.shuffle(items)
    return items
