from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime
from decimal import Decimal


class CandleDataBase(BaseModel):
    instrument_id: int = Field(..., description="ID of the instrument")
    interval_id: int = Field(..., description="ID of the interval")
    timestamp: datetime = Field(..., description="Timestamp for the candle")

    open: Decimal = Field(..., description="Open price")
    high: Decimal = Field(..., description="High price")
    low: Decimal = Field(..., description="Low price")
    close: Decimal = Field(..., description="Close price")
    volume: int = Field(..., description="Volume of trades")

    is_adjusted: Optional[bool] = Field(default=False, description="Whether the candle is adjusted")
    source: Optional[str] = Field(default=None, description="Data source (e.g., 'upstox')")


class CandleDataCreate(CandleDataBase):
    pass


class CandleDataRead(CandleDataBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
