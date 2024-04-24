import pathlib

from pydantic_settings import BaseSettings
import environ


BASE_DIR = pathlib.Path(__file__).parent.parent
env = environ.Env()
environ.Env.read_env(str(BASE_DIR.joinpath(".env")))


class Settings(BaseSettings):
    debug: bool = env("DEBUG", default=False)


settings = Settings()
