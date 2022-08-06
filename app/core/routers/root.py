from __future__ import annotations

from core.auth.jwt_token import get_current_user
from core.repositories.distance import get_top_cloest_airport
from core.repositories.factor import fetch_factor_data
from fastapi import APIRouter
from fastapi import Depends
from models.user import User

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
