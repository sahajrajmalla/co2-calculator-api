from __future__ import annotations

from fastapi import HTTPException
from fastapi import status
from sqlalchemy.orm import Session

from app.core.auth.hashing import Hash
from app.models.user import User
from app.schemas.user import UserType


def create_new_user(request: UserType, db: Session):
    new_user = User(
        name=request.name, email=request.email,
        password=Hash.bcrypt(request.password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def get_user_by_id(id: int, db: Session):
    user = db.query(User).filter(User.id == id).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'USer id {id} does not exist.',
        )

    return user
