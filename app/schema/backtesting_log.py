from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, Dict, Any
from datetime import datetime
from decimal import Decimal


class BacktestingLogBase(BaseModel):
    strategy_id: Optional[int] = Field(None, description="ID of the strategy used")
    instrument_id: Optional[int] = Field(None, description="ID of the instrument used")
    interval_id: int = Field(..., description="ID of the interval used")
    start_time: datetime = Field(..., description="Start time of the backtest")
    end_time: datetime = Field(..., description="End time of the backtest")
    profit: Decimal = Field(..., description="Profit from the backtest")
    metrics: Optional[Dict[str, Any]] = Field(None, description="Metrics collected during backtest")


class BacktestingLogCreate(BacktestingLogBase):
    pass


class BacktestingLogRead(BacktestingLogBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
