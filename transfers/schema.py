from pydantic import BaseModel, ConfigDict
from common.enums import TransferType
from datetime import datetime

class TransferBase(BaseModel):
    amount: float
    transfer_type: TransferType
    account_id: int


class TransferCreate(TransferBase):
    pass


class TransferResponse(TransferBase):
    model_config = ConfigDict(from_attributes=True) 
    id: int
    timestamp: datetime