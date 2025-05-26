from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime


class UpstoxTokenBase(BaseModel):
    access_token: str = Field(..., description="Access token for Upstox API")
    refresh_token: str = Field(..., description="Refresh token for Upstox API")
    expires_at: datetime = Field(..., description="Token expiry timestamp")


class UpstoxTokenCreate(UpstoxTokenBase):
    pass


class UpstoxTokenRead(UpstoxTokenBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
