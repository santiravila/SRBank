from transfers.service import TransferService
from .repository import WireRepository
from sqlalchemy.orm import Session
from .models import Wire
from .schema import WireCreate
from common.enums import TransferType
from transfers.schema import TransferCreate


class WireTransferCoordinator:
    def __init__(self, transfer_service: TransferService, wire_repo: WireRepository, session: Session) -> None:
        self.transfer_service = transfer_service
        self.wire_repo = wire_repo
        self.session = session

    def execute_wire(self, payload: WireCreate):
        try:
            wire = Wire(**payload.model_dump())
            if wire.sender_account_id == wire.receiver_account_id:
                raise ValueError("Sender and receiver account ids must be different")

            self.transfer_service.execute_transfer(
                TransferCreate(account_id=wire.sender_account_id, transfer_type=TransferType.WITHDRAWAL, amount=wire.amount),
                commit=False
            )

            self.transfer_service.execute_transfer(
                TransferCreate(account_id=wire.receiver_account_id, transfer_type=TransferType.DEPOSIT, amount=wire.amount),
                commit=False
            )

            self.wire_repo.save(wire)

            self.session.commit()
            return wire
        except Exception:
            self.session.rollback()
            raise
