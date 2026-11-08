from fastapi import APIRouter, Depends
from .schema import TransferCreate, TransferResponse
from .repository import TransferRepository
from accounts.repository import AccountRepository
from typing import Annotated
from .service import TransferService
from common.dependencies import DBSession

router = APIRouter(
    prefix="/transfers",
    tags=["transfers"]
)

def get_service_dep(db_session: DBSession):
    account_repo = AccountRepository(db_session)
    transfer_repo = TransferRepository(db_session)
    return TransferService(account_repo, transfer_repo)

ServiceDep = Annotated[TransferService, Depends(get_service_dep)]

@router.post("", response_model=TransferResponse) # remove response model later on 
def create_transfer(
    transfer_payload: TransferCreate,
    service: ServiceDep
) -> TransferResponse: # also try it without it
    db_transfer = service.execute_transfer(transfer_payload)
    return TransferResponse.model_validate(db_transfer)
