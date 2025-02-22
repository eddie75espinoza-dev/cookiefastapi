import os
import secrets
from typing import Annotated, Any, List

from pydantic import AnyUrl, Field, validator, BeforeValidator
from pydantic_settings import BaseSettings


def parse_cors(value: Any) -> List[str]:
    if isinstance(value, str):
        return [i.strip() for i in value.split(",")] if value else []
    if isinstance(value, list):
        return value
    raise ValueError(f"Invalid CORS origins: {value}")


class Config(BaseSettings):
    ENVIRONMENT: str = Field(..., env="ENVIRONMENT")
    PROJECT_NAME: str = Field(..., env="PROJECT_NAME")
    SECRET_KEY: str = Field(default_factory=lambda: secrets.token_urlsafe(32))
    HOST: str = Field(..., env="HOST")
    PORT: int = Field(..., env="PORT")
    BASE_URL: str | None = Field(None, env="BASE_URL")
    API_V1_STR: str = "/api/v1"
    TOKEN_SECRET_KEY: str = Field(default_factory=lambda: secrets.token_urlsafe(32))
    SUB: str = Field(..., env="SUB")

    POSTGRES_USER: str = Field(..., env="POSTGRES_USER")
    POSTGRES_PASSWORD: str = Field(..., env="POSTGRES_PASSWORD")
    POSTGRES_HOST: str = Field(..., env="POSTGRES_HOST")
    POSTGRES_PORT: int = Field(..., env="POSTGRES_PORT")
    POSTGRES_DB: str = Field(..., env="POSTGRES_DB")

    BACKEND_CORS_ORIGINS: Annotated[
        List[AnyUrl] | str, BeforeValidator(parse_cors)
    ] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def validate_cors(cls, value: Any) -> List[str]:
        return parse_cors(value)

    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        return (
            f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@"
            f"{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )


class DevelopmentConfig(Config):
    DEBUG: bool = True
    TESTING: bool = True


class StagingConfig(Config):
    DEBUG: bool = False
    TESTING: bool = False


class ProductionConfig(Config):
    DEBUG: bool = False
    TESTING: bool = False


def get_config(environment: str) -> Config:
    config_classes = {
        "development": DevelopmentConfig,
        "staging": StagingConfig,
        "production": ProductionConfig,
    }
    return config_classes.get(environment, DevelopmentConfig)()


APP_CONFIG = get_config(environment=os.getenv('ENVIRONMENT'))
