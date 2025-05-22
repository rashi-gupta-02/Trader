from sqlalchemy import Column, Integer, String, Float, DateTime
from app.db.models.base import Base
from datetime import datetime

class PaperTrade(Base):
    __tablename__ = "paper_trades"

    id = Column(Integer, primary_key=True)
    strategy_name = Column(String)
    instrument_symbol = Column(String)
    action = Column(String)  # BUY or SELL
    quantity = Column(Integer)
    price = Column(Float)
    executed_at = Column(DateTime, default=datetime.utcnow)
