from .schema import AccountCreate
from .models import Account
from customers.repository import CustomerRepository
from .repository import AccountRepository
from sqlalchemy.orm import Session


class AccountService:
    def __init__(
        self,
        customer_repo: CustomerRepository,
        account_repo: AccountRepository,
        session: Session
    ):
        self.customer_repo = customer_repo
        self.account_repo = account_repo
        self.session = session

    def create_account(self, account_payload: AccountCreate) -> Account:
        try:
            # check a customer with customer_id exists. get_customer validates automatically
            customer = self.customer_repo.get(account_payload.customer_id)
            
            new_account = Account(
                account_type=account_payload.account_type,
                balance=account_payload.balance,
                password=account_payload.password,

                # backpopulates makes it so customer knows new account has been appended to its list
                customer=customer
            )

            saved_account = self.account_repo.save(new_account)
            self.session.commit()
            return saved_account
        except Exception:
            self.session.rollback()
            raise

    def get_account(self, account_id: int):
        saved_account = self.account_repo.get(account_id)
        return saved_account


        
        