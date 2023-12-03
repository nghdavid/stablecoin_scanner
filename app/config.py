import os
from datetime import timedelta
from typing import Any, Dict, List, Optional

from pydantic_settings import BaseSettings
from pydantic import validator

class DBSettings(BaseSettings):
    DB_HOST: str
    DB_PORT: int = 3306
    DB_USER: str = "stablecoin"
    DB_PASSWORD: str
    DB_NAME: str = "cex"
    SQLALCHEMY_DATABASE_URL: Optional[str] = None
    API_KEY: str
    TRON_API_KEY: str
    TELEGRAM_KEY: str
    ENV: str = "local"
    @validator("SQLALCHEMY_DATABASE_URL", pre=True)
    def assemble_db_uri(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return f"mysql+mysqlconnector://{values.get('DB_USER')}:{values.get('DB_PASSWORD')}@{values.get('DB_HOST')}:{values.get('DB_PORT')}/{values.get('DB_NAME')}"

    class Config:
        # env_file = ".env"
        env_file = "/home/ec2-user/stablecoin_scanner/.env"



def get_settings() -> DBSettings:
    configs = {
        "local": DBSettings,
    }
    _env = os.getenv("ENV", "local")
    return configs.get(_env)()

settings = get_settings()