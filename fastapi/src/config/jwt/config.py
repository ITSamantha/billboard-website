from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class ConfigJWT(BaseSettings):
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str


settings_jwt = ConfigJWT()
