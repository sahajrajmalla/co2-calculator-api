from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class LoginSchema(BaseModel):
    username: str
    password: str


class TokenData(BaseModel):
    username: Optional[str] = None
