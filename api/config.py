from pydantic import BaseSettings
from dotenv import dotenv_values

config = dotenv_values(".env")


class CommonSettings(BaseSettings):
    APP_NAME: str = "Media Upload Service"
    DEBUG_MODE: bool = True


class DatabaseSettings(BaseSettings):
    DB_URL: str = config['DB_URL']
    DB_NAME: str = config['DB_NAME']


class ServerSettings(BaseSettings):
    HOST: str = "localhost"
    PORT: int = 8000


class JWTSettings(BaseSettings):
    JWT_SECRET: str = config['JWT_SECRET_KEY']
    JWT_ALGORITHM: str = config['JWT_ALGORITHM']


class Settings(CommonSettings, ServerSettings, DatabaseSettings, JWTSettings):
    pass


settings = Settings()
