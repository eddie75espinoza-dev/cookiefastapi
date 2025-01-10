from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from core.config import APP_CONFIG


DATABASE_URL = APP_CONFIG.SQLALCHEMY_DATABASE_URI

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_size=20,       # Número máximo de conexiones abiertas
    max_overflow=5,     # Número de conexiones adicionales temporales si todas las conexiones del pool están en uso
    pool_timeout=30,    # Espera hasta 30 segundos si no hay conexiones disponibles
    pool_recycle=1800   # Recicla conexiones después de 30 minutos
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    """Provee una sesión de base de datos para las operaciones"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()