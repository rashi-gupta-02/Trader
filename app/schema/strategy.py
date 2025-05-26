from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, Dict, Any
from datetime import datetime


class StrategyBase(BaseModel):
    name: str = Field(..., description="Unique name of the trading strategy")
    description: Optional[str] = Field(None, description="Brief description of the strategy")
    parameters: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Strategy configuration parameters")
    is_active: Optional[bool] = Field(default=True, description="Whether the strategy is active")


class StrategyCreate(StrategyBase):
    pass


class StrategyRead(StrategyBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
