from datetime import datetime
from pydantic import BaseModel, ConfigDict


class WireBase(BaseModel):
    sender_account_id: int
    receiver_account_id: int
    amount: float


class WireCreate(WireBase):
    pass


class WireResponse(WireBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    timestamp: datetime