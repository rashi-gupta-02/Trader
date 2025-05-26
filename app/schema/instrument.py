from pydantic import BaseModel, Field, ConfigDict
from typing import Optional


class InstrumentBase(BaseModel):
    symbol: str = Field(..., description="Trading symbol of the instrument")
    name: Optional[str] = Field(None, description="Full name of the instrument")
    exchange: str = Field(..., description="Exchange where the instrument is traded")
    type: Optional[str] = Field(None, description="Type of instrument, e.g., EQ, FUT, OPT")
    is_active: Optional[bool] = Field(default=True, description="Whether the instrument is active")


class InstrumentCreate(InstrumentBase):
    pass


class InstrumentRead(InstrumentBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
