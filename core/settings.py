from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    sqlalchemy_database_uri: str
    redis_uri: str
    secret_key: str
    items_per_page: int

    model_config = SettingsConfigDict(env_file="settings.env")


@lru_cache
def get_settings() -> Settings:
    return Settings()
