from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated
from infrastructure.database import get_db_session
from sqlalchemy.orm import Session
from .schema import CustomerCreate, CustomerResponse, CustomerUpdate
from .repository import CustomerRepository


router = APIRouter(prefix="/customers", tags=["customers"])


@router.post("", response_model=CustomerResponse)
def create_customer(
    customer_payload: CustomerCreate,
    db: Annotated[Session, Depends(get_db_session)]
    ) -> CustomerResponse:
    repo = CustomerRepository(db)
    db_customer = repo.save_customer(customer_payload)
    return CustomerResponse.model_validate(db_customer)


@router.get("{customer_id}", response_model=CustomerResponse)
def get_customer(
    customer_id: int,
    db: Annotated[Session, Depends(get_db_session)]
    ) -> CustomerResponse:
    repo = CustomerRepository(db)
    try:
        customer = repo.get_customer(customer_id)
    except ValueError as err:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(err)
        )
    else:
        return CustomerResponse.model_validate(customer)


@router.patch("{customer_id}", response_model=CustomerResponse)
def update_customer(
    customer_id: int,
    customer_payload: CustomerUpdate,
    db: Annotated[Session, Depends(get_db_session)],
) -> CustomerResponse:
    repo = CustomerRepository(db)
    try:
        customer = repo.update_customer(customer_id, customer_payload)
    except ValueError as e:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = str(e)
        )
    return CustomerResponse.model_validate(customer)

@router.delete("{customer_id}", response_model=CustomerResponse)
def delete_customer(
    customer_id: int,
    db: Annotated[Session, Depends(get_db_session)]
) -> CustomerResponse:
    repo = CustomerRepository(db)
    try:
        customer = repo.delete_customer(customer_id)
    except ValueError as e:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = str(e)
        )
    return CustomerResponse.model_validate(customer)