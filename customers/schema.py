from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
from datetime import datetime

# base dto shared properties
class CustomerBase(BaseModel):
    fullname: str
    email: EmailStr


class CustomerCreate(CustomerBase):
    pass


class CustomerResponse(CustomerBase):
    model_config = ConfigDict(from_attributes=True) # could ad extra='forbid' for forbidding extra fields
    id: int
    registered_at: datetime


class CustomerUpdate(CustomerBase):
    email: Optional[EmailStr] = None
    fullname: Optional[str] = None


    
        
