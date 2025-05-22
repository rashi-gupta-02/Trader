from sqlalchemy import Column, Integer, String, DateTime
from app.db.models.base import Base
from datetime import datetime

class UpstoxToken(Base):
    __tablename__ = "upstox_tokens"

    id = Column(Integer, primary_key=True, index=True)
    access_token = Column(String)
    refresh_token = Column(String)
    expires_at = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)
