from __future__ import annotations

from core.auth.jwt_token import get_current_user
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
