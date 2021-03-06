from pydantic import BaseSettings

class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        # specify the path to .env-file
        #env_file = "../.env"

        env_file = ".env"



# Instance of Settings-Class
settings = Settings()