import os
from typing import Optional
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Settings:
    
    def __init__(self):
        # Database settings
        self.DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./trader.db")
        
        # API settings
        self.API_HOST: str = os.getenv("API_HOST", "localhost")
        self.API_PORT: int = int(os.getenv("API_PORT", "8000"))
        
        # Security settings
        self.SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-here-change-in-production")
        
        # Trading settings
        self.DEFAULT_TIMEFRAME: str = os.getenv("DEFAULT_TIMEFRAME", "1h")
        self.MAX_POSITIONS: int = int(os.getenv("MAX_POSITIONS", "10"))
        
        # Debug settings
        self.DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
        
    def __repr__(self):
        return f"Settings(DATABASE_URL={self.DATABASE_URL}, API_HOST={self.API_HOST})"

settings = Settings()

if __name__ == "__main__":
    print("Current Settings:")
    print(f"DATABASE_URL: {settings.DATABASE_URL}")
    print(f"API_HOST: {settings.API_HOST}")
    print(f"API_PORT: {settings.API_PORT}")
    print(f"DEFAULT_TIMEFRAME: {settings.DEFAULT_TIMEFRAME}")
    print(f"MAX_POSITIONS: {settings.MAX_POSITIONS}")
    print(f"DEBUG: {settings.DEBUG}")