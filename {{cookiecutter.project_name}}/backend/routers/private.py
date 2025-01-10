from fastapi import APIRouter


router = APIRouter(tags=["private"], prefix="/private")


@router.get("/")
def read_root_private():
    return {"msg": "{{cookiecutter.project_name}}"}