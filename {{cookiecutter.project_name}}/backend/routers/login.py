from fastapi import APIRouter, Depends
from core.middleware import require_bearer_token


router = APIRouter(tags=["login"], prefix="/login")


@router.get("/", dependencies=[Depends(require_bearer_token)])
async def login():
    return {"msg": "success"}