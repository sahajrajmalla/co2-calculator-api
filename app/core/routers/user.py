from __future__ import annotations

from core.repositories.user import create_new_user
from core.repositories.user import get_user_by_id
from db.database import get_db
from fastapi import APIRouter
from fastapi import Depends
from schemas.user import ShowUser
from schemas.user import UserType
from sqlalchemy.orm import Session
# from fastapi import status

router = APIRouter(prefix='/user', tags=['Users'])


@router.post('/', response_model=ShowUser)
def create_user(request: UserType, db: Session = Depends(get_db)):
    return create_new_user(request, db)


@router.get('/{id}', response_model=ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return get_user_by_id(id, db)