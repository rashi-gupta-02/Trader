from pydantic import BaseModel, Field, ConfigDict
from typing import Optional


class IntervalBase(BaseModel):
    name: str = Field(..., description="Name of the interval (e.g., '1m', '5m', '1d')")
    duration_sec: int = Field(..., ge=1, description="Duration of the interval in seconds")


class IntervalCreate(IntervalBase):
    pass


class IntervalRead(IntervalBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
