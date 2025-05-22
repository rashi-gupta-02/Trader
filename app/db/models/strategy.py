from sqlalchemy import Column, Integer, String, Text, DateTime,Boolean,JSON
from app.db.base import Base
from sqlalchemy.dialects.postgresql import JSONB
from datetime import datetime

class Strategy(Base):
    __tablename__ = "strategies"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String)
    parameters = Column(JSONB)
    created_at = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)
