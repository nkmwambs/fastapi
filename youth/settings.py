
from pydantic import BaseSettings

from youth import database

class Settings(BaseSettings):
    database_username: str
    database_password: str 
    database_hostname: str 
    database_port: str 
    database_name: str 
    secret_key: str 
    access_token_expire_minutes: int
    algorithm:str

    class Config():
        env_file=".env"


settings = Settings()