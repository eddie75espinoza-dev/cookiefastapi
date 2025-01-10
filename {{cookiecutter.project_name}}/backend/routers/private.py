from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError
from core.middleware import require_bearer_token
from sqlalchemy.sql import text
from sqlalchemy.orm import Session

from db.database import get_db

router = APIRouter(tags=["private"], prefix="/private")


@router.get("/", dependencies=[Depends(require_bearer_token)])
async def read_root_private():
    """Prueba de conexión privada"""
    return JSONResponse(
        content={"status": "success", "name": "fastapi_project"},
        status_code=200
    )


@router.get("/db-test", dependencies=[Depends(require_bearer_token)])
def test_connection(db: Session = Depends(get_db)):
    """Prueba de conexión a la base de datos"""
    try:
        result = db.execute(text("SELECT 1"))
        rows = [row[0] for row in result]
        return JSONResponse(
            content={"status": "success", "rows": rows},
            status_code=200
        )
    
    except SQLAlchemyError as e:
        return JSONResponse(
            content={"status": "error", "detail": str(e)},
            status_code=500
        )
    except Exception as e:
        return JSONResponse(
            content={"status": "error", "detail": str(e)},
            status_code=400
        )