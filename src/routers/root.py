from __future__ import annotations

from fastapi import APIRouter
from fastapi import Depends

from db.models.user import User
from src.api.auth.jwt_token import get_current_user

router = APIRouter(prefix='', tags=['Root'])


@router.get('/health')
def check_health():
    return {'status': 'ok'}


@router.get('/check_auth', response_model=str)
def check_auth(current_user: User = Depends(get_current_user)):
    return 'Hello World!'
