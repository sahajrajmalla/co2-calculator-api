from __future__ import annotations

from fastapi import FastAPI

from app.api.v1.api import api_router
from app.core.routers import auth
from app.core.routers import root
from app.core.routers import user
from app.db.database import engine
from app.models import CalculatorBase
from app.models import EventBase
from app.models import ParticipantBase
from app.models import UserBase
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UserBase.metadata.create_all(engine)
EventBase.metadata.create_all(engine)
ParticipantBase.metadata.create_all(engine)
CalculatorBase.metadata.create_all(engine)

app.include_router(root.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(api_router)
