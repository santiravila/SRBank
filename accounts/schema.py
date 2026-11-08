from pydantic import BaseModel, ConfigDict
from accounts.models import AccountType
from datetime import datetime


class AccountBase(BaseModel):
    account_type: AccountType
    balance: float
    password: str
    customer_id: int


class AccountCreate(AccountBase):
    pass


class AccountResponse(AccountBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    created_at: datetime


class AccountUpdate(AccountBase):
    account_type: AccountType | None = None
    balance: float | None = None 
    password: str | None = None