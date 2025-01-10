from fastapi import APIRouter, Depends
from core.middleware import require_bearer_token
from sqlalchemy.orm import Session

from db.database import get_db

router = APIRouter(tags=["private"], prefix="/private")


@router.get("/", dependencies=[Depends(require_bearer_token)])
async def read_root_private():
    """Prueba de conexión privada"""
    return {"status": "success", "name": "{{cookiecutter.project_name}}"}


@router.get("/db-test", dependencies=[Depends(require_bearer_token)])
def test_connection(db: Session = Depends(get_db)):
    """Prueba de conexión a la base de datos"""
    try:
        result = db.execute("SELECT 1")
        return {"status": "success", "result": [row for row in result]}
    
    except Exception as e:
        return {"status": "error", "detail": str(e)}