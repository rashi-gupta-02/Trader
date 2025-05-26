from pydantic import BaseModel, Field, ConfigDict
from typing import Literal
from datetime import datetime


class PaperTradeBase(BaseModel):
    strategy_name: str = Field(..., description="Name of the strategy used")
    instrument_symbol: str = Field(..., description="Trading symbol of the instrument")
    action: Literal["BUY", "SELL"] = Field(..., description="Trade action: BUY or SELL")
    quantity: int = Field(..., gt=0, description="Quantity of the instrument traded")
    price: float = Field(..., gt=0, description="Price at which the trade was executed")


class PaperTradeCreate(PaperTradeBase):
    pass


class PaperTradeRead(PaperTradeBase):
    id: int
    executed_at: datetime

    model_config = ConfigDict(from_attributes=True)
