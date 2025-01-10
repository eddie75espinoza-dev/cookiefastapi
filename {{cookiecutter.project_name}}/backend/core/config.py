import os
import secrets
from dotenv import load_dotenv
from typing import Annotated, Any

from pydantic import (
    AnyUrl,
    BeforeValidator,
    computed_field
)
from pydantic_settings import BaseSettings


load_dotenv()

def parse_cors(v: Any) -> list[str] | str:
    if isinstance(v, str) and not v.startswith("["):
        return [i.strip() for i in v.split(",")]
    elif isinstance(v, list | str):
        return v
    raise ValueError(v)


class Config(BaseSettings):
    SECRET_KEY = secrets.token_urlsafe(32)
    HOST = os.getenv('HOST')
    PORT = int(os.getenv('PORT'))
    BASE_URL = os.getenv('BASE_URL')
    API_V1_STR = "/api/v1"

    SQLALCHEMY_DATABASE_URI = (
        f'postgresql://{os.getenv("POSTGRES_USER")}:'
        f'{os.getenv("POSTGRES_PASSWORD")}@'
        f'{os.getenv("POSTGRES_HOST")}:{os.getenv("POSTGRES_PORT")}/'
        f'{os.getenv("POSTGRES_DB")}'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BACKEND_CORS_ORIGINS: Annotated[
        list[AnyUrl] | str, BeforeValidator(parse_cors)
    ] = []

    @computed_field  # type: ignore[prop-decorator]
    @property
    def all_cors_origins(self) -> list[str]:
        return [str(origin).rstrip("/") for origin in self.BACKEND_CORS_ORIGINS]


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True


class StagingConfig(Config):
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False


ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

if ENVIRONMENT == 'development':
    APP_CONFIG = 'config.DevelopmentConfig'
elif ENVIRONMENT == 'production':
    APP_CONFIG = 'config.ProductionConfig'
elif ENVIRONMENT == 'staging':
    APP_CONFIG = 'config.StagingConfig'