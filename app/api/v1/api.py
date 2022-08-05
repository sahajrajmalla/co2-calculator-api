"""Register API routers and modules"""
from fastapi import APIRouter

from api.v1.endpoints import (
    events,
    participants,
)


api_router = APIRouter()


api_router.include_router(
    events.router,
    prefix="/events",
    tags=["Events"],
)

api_router.include_router(
    participants.router,
    prefix="/participants",
    tags=["Participants"],
)

