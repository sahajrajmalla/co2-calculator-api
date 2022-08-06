from __future__ import annotations

from api.v1.api import api_router
from core.routers import auth
from core.routers import root
from core.routers import user
from db.database import engine
from fastapi import FastAPI
from models import CalculatorBase
from models import EventBase
from models import ParticipantBase
from models import UserBase
# from starlette.middleware.cors import CORSMiddleware

app = FastAPI()


UserBase.metadata.create_all(engine)
EventBase.metadata.create_all(engine)
ParticipantBase.metadata.create_all(engine)
CalculatorBase.metadata.create_all(engine)

app.include_router(root.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(api_router)
