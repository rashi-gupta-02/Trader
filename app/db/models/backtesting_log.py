from sqlalchemy import Column, Integer, String, DateTime, Text,ForeignKey,Numeric,JSON
from sqlalchemy.dialects.postgresql import JSONB
from datetime import datetime
from .base import Base

class BacktestingLog(Base):
    __tablename__ = "backtesting_logs"

    id = Column(Integer, primary_key=True)
    strategy_id = Column(Integer, ForeignKey("strategies.id", ondelete="SET NULL"))
    instrument_id = Column(Integer, ForeignKey("instruments.id", ondelete="SET NULL"))
    interval_id = Column(Integer, ForeignKey("intervals.id"))
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    profit = Column(Numeric(16, 4))
    metrics = Column(JSONB)
    created_at = Column(DateTime, default=datetime.utcnow)

