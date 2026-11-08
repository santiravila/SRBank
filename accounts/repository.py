from sqlalchemy.orm import Session
from .schema import AccountUpdate
from .models import Account


class AccountRepository:
    def __init__(self, session: Session):
        self.session = session

    def save(self, account: Account) -> Account:
        self.session.add(account)
        self.session.flush()
        self.session.refresh(account)
        return account  


    def get(self, account_id: int):
        account = self.session.get(Account, account_id)

        if not account:
            raise ValueError("No account persisted with id {account_id}")

        return account
