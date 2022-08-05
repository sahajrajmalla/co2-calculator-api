from __future__ import annotations

from fastapi import FastAPI

from db.database import engine
from db.models.user import Base
from src.routers import auth
from src.routers import root
from src.routers import user
# from starlette.middleware.cors import CORSMiddleware

app = FastAPI()


Base.metadata.create_all(engine)

app.include_router(root.router)
app.include_router(user.router)
app.include_router(auth.router)
