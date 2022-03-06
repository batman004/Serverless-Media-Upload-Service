from pydantic import BaseSettings

class CommonSettings(BaseSettings):
    APP_NAME: str = "Media Upload Service"
    DEBUG_MODE: bool = True


class Settings(CommonSettings):
    pass


settings = Settings()