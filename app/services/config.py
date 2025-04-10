from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_USER: str
    DB_PASS: str

    class Config:
        env_file = ".env"


settings = Settings()
