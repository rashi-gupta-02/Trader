from sqlalchemy import Column, Integer, String
from app.db.models.base import Base

class Interval(Base):
    __tablename__ = "intervals"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    duration_sec = Column(Integer)
