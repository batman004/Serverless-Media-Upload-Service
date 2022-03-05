from pydantic import BaseSettings
from dotenv import dotenv_values
config = dotenv_values(".env")

class CommonSettings(BaseSettings):
    APP_NAME: str = "Media Upload Service"
    DEBUG_MODE: bool = True

# class AWSSettings(BaseSettings):


class Settings(CommonSettings):
    pass


settings = Settings()