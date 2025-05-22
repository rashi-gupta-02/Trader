import os
from typing import Any, Dict, Optional
from dotenv import load_dotenv
from pydantic import PostgresDsn
from pydantic_settings import BaseSettings
from pydantic import field_validator

# Load environment variables from .env file
load_dotenv()

class Settings(BaseSettings):
    PROJECT_NAME: str = "Trader_API"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your_secret_key_here")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  
    
    # Database settings
    DATABASE_URL: Optional[PostgresDsn] = os.getenv("DATABASE_URL")
    
    @field_validator("DATABASE_URL", mode="before")
    @classmethod
    def assemble_db_connection(cls, v: Optional[str]) -> str:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=os.getenv("POSTGRES_USER", "postgres"),
            password=os.getenv("POSTGRES_PASSWORD", "postgres"),
            host=os.getenv("POSTGRES_SERVER", "localhost"),
            port=os.getenv("POSTGRES_PORT", "5432"),
            path=f"/{os.getenv('POSTGRES_DB', 'trader_api')}",
        )
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"

    class Config:
        case_sensitive = True
settings = Settings() 