from pydantic import BaseSettings
import os
from dotenv import dotenv_values
config = dotenv_values(".env")
class CommonSettings(BaseSettings):
    APP_NAME: str = "Media Upload Service"
    DEBUG_MODE: bool = True
class DatabaseSettings(BaseSettings):
    DB_URL: str 
    DB_NAME: str

class ServerSettings(BaseSettings):
    HOST: str = "localhost"
    PORT: int = 8000
class Settings(CommonSettings, ServerSettings, DatabaseSettings):
    pass


settings = Settings()