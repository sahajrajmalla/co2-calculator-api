from __future__ import annotations

from core.routers import auth
from core.routers import root
from core.routers import user
from db.database import engine
from fastapi import FastAPI
from models.user import Base
# from starlette.middleware.cors import CORSMiddleware

app = FastAPI()


Base.metadata.create_all(engine)

app.include_router(root.router)
app.include_router(user.router)
app.include_router(auth.router)
