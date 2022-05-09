from pydantic import BaseSettings
import os


class CommonSettings(BaseSettings):
    APP_NAME: str = "Media Upload Service"
    DEBUG_MODE: bool = True


class DatabaseSettings(BaseSettings):
    DB_URL: str = os.getenv['DB_URL']
    DB_NAME: str = os.getenv['DB_NAME']


class ServerSettings(BaseSettings):
    HOST: str = "localhost"
    PORT: int = 8000


class Settings(CommonSettings, ServerSettings, DatabaseSettings):
    pass


settings = Settings()
