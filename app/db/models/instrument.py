from sqlalchemy import Column, Integer, String,Boolean, ForeignKey, DateTime, Numeric, BigInteger, JSON, UniqueConstraint
from app.db.base import Base
from sqlalchemy.dialects.postgresql import JSONB
class Instrument(Base):
    __tablename__ = "instruments"

    id = Column(Integer, primary_key=True)
    symbol = Column(String, nullable=False)
    name = Column(String)
    exchange = Column(String, nullable=False)
    type = Column(String)  # e.g., EQ, FUT, OPT
    is_active = Column(Boolean, default=True)

    __table_args__ = (UniqueConstraint("symbol", "exchange", name="uq_symbol_exchange"),)

