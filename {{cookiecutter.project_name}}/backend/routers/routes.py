from fastapi import APIRouter

from routers import login, private
from core.config import Config

api_router = APIRouter()
api_router.include_router(login.router)


if Config.ENVIRONMENT == "development":
    api_router.include_router(private.router)