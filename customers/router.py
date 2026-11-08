from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated
from common.dependencies import DBSession
from .schema import CustomerCreate, CustomerResponse, CustomerUpdate
from .repository import CustomerRepository
from .service import CustomerService

router = APIRouter(
    prefix="/customers", 
    tags=["customers"]
)

def get_service_dependency(db: DBSession):
    repo = CustomerRepository(db)
    return CustomerService(repo, db)

ServiceDep = Annotated[CustomerService, Depends(get_service_dependency)]

@router.post("", response_model=CustomerResponse)
def create_customer(
    payload: CustomerCreate,
    service: ServiceDep
    ) -> CustomerResponse:
    db_customer = service.create_customer(payload)
    return CustomerResponse.model_validate(db_customer)


@router.get("{customer_id}", response_model=CustomerResponse)
def get_customer(
    customer_id: int,
    service: ServiceDep
    ) -> CustomerResponse:
    try:
        customer = service.get_customer(customer_id)
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
    payload: CustomerUpdate,
    service: ServiceDep
) -> CustomerResponse:
    try:
        customer = service.update_customer(customer_id, payload)
    except ValueError as e:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = str(e)
        )
    return CustomerResponse.model_validate(customer)


@router.delete("{customer_id}", response_model=CustomerResponse)
def delete_customer(
    customer_id: int,
    service: ServiceDep
) -> CustomerResponse:
    try:
        customer = service.delete_customer(customer_id)
    except ValueError as e:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = str(e)
        )
    return CustomerResponse.model_validate(customer)