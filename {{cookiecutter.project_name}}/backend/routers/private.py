from fastapi import APIRouter, Depends
from core.middleware import require_bearer_token


router = APIRouter(tags=["private"], prefix="/private")


@router.get("/", dependencies=[Depends(require_bearer_token)])
async def read_root_private():
    return {"msg": "{{cookiecutter.project_name}}"}