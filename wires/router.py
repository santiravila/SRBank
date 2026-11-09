from fastapi import APIRouter, Depends
from common.dependencies import DBSession
from .schema import WireCreate, WireResponse
from .repository import WireRepository
from .service import WireTransferCoordinator
from transfers.service import TransferService
from transfers.repository import TransferRepository
from accounts.repository import AccountRepository
from typing import Annotated


router = APIRouter(
    prefix="/wires",
    tags=["wires"]
)

def get_service_dependency(db: DBSession):
    wire_repo = WireRepository(db)
    account_repo = AccountRepository(db)
    transfer_repo = TransferRepository(db)
    transfer_service = TransferService(
        account_repo=account_repo, 
        transfer_repo=transfer_repo, 
        session=db
    )
    return WireTransferCoordinator(
        transfer_service=transfer_service, 
        wire_repo=wire_repo, 
        session=db
    )

ServiceDep = Annotated[WireTransferCoordinator, Depends(get_service_dependency)]


@router.post("")
def create_wire(
    payload: WireCreate,
    service: ServiceDep
):
    saved_wire = service.execute_wire(payload)
    return WireResponse.model_validate(saved_wire)