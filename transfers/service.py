from common.enums import TransferType
from .models import Transfer
from accounts.repository import AccountRepository
from sqlalchemy.orm import Session



class TransferService:
    def __init__(self, account_repo: AccountRepository, transfer_repo, session: Session):
        self.account_repo = account_repo
        self.transfer_repo = transfer_repo
        self.session = session

    def execute_transfer(self, transfer_payload) -> Transfer:
        try:
            # get account with account_id using account_repo to check it exists
            account = self.account_repo.get(transfer_payload.account_id)

            # call deposit or withdraw depending on transfer type with the account
            if transfer_payload.transfer_type == TransferType.DEPOSIT.value:
                account.deposit(amount=transfer_payload.amount)
            elif transfer_payload.transfer_type == TransferType.WITHDRAWAL.value:
                account.withdraw(amount=transfer_payload.amount)

            # map DTO to SQLAlchemy model
            transfer = Transfer(
                amount=transfer_payload.amount,
                transfer_type=transfer_payload.transfer_type,
                account_id=transfer_payload.account_id
            )

            saved_transfer = self.transfer_repo.save(transfer)

            # services commits entire unit of work.
            self.session.commit()
            return saved_transfer
        
        except Exception:
            self.session.rollback()
            raise   