"""Register API routers and modules"""
from __future__ import annotations

from api.v1.endpoints import events
from api.v1.endpoints import participants
from fastapi import APIRouter


api_router = APIRouter()


api_router.include_router(
    events.router,
    prefix='/events',
    tags=['Events'],
)

api_router.include_router(
    participants.router,
    prefix='/participants',
    tags=['Participants'],
)
