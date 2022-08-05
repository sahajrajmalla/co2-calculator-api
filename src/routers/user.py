from __future__ import annotations

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from db.database import get_db
from src.api.users.user import create_new_user
from src.api.users.user import get_user_by_id
from src.schemas.user import ShowUser
from src.schemas.user import UserType
# from fastapi import status

router = APIRouter(prefix='/user', tags=['Users'])


@router.post('/', response_model=ShowUser)
def create_user(request: UserType, db: Session = Depends(get_db)):
    return create_new_user(request, db)


@router.get('/{id}', response_model=ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return get_user_by_id(id, db)
