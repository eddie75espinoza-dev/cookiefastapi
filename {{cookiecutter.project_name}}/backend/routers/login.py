from fastapi import APIRouter


router = APIRouter(tags=["login"], prefix="/login")


@router.get("/")
def login():
    return {"msg": "success"}