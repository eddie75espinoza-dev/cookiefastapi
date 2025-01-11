from fastapi import APIRouter

from routers import login, private
from core.config import APP_CONFIG


api_router = APIRouter()
api_router.include_router(login.router)

if APP_CONFIG.ENVIRONMENT == "development":
    api_router.include_router(private.router)