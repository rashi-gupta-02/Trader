from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime, UniqueConstraint,BigInteger,Numeric,Boolean,String
from sqlalchemy.orm import relationship
from app.db.models.base import Base

class CandleData(Base):
    __tablename__ = "ohlcv_data"

    id = Column(BigInteger, primary_key=True)
    instrument_id = Column(Integer, ForeignKey("instruments.id", ondelete="CASCADE"), nullable=False)
    interval_id = Column(Integer, ForeignKey("intervals.id"), nullable=False)
    timestamp = Column(DateTime, nullable=False)

    open = Column(Numeric(16, 4), nullable=False)
    high = Column(Numeric(16, 4), nullable=False)
    low = Column(Numeric(16, 4), nullable=False)
    close = Column(Numeric(16, 4), nullable=False)
    volume = Column(BigInteger, nullable=False)

    is_adjusted = Column(Boolean, default=False)
    source = Column(String)  # e.g., "upstox"

    __table_args__ = (
        UniqueConstraint("instrument_id", "interval_id", "timestamp", name="uq_ohlcv_data"),
    )

