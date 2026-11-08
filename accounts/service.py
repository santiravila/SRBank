from .schema import AccountCreate, AccountResponse
from .models import Account
from customers.repository import CustomerRepository
from .repository import AccountRepository


class AccountService:
    def __init__(
        self,
        customer_repo: CustomerRepository,
        account_repo: AccountRepository    
    ):
        self.customer_repo = customer_repo
        self.account_repo = account_repo

    def add_account(self, account_payload: AccountCreate) -> Account:
        # check a customer with customer_id exists. get_customer validates automatically
        customer = self.customer_repo.get_customer(account_payload.customer_id)
        
        new_account = Account(
            account_type=account_payload.account_type,
            balance=account_payload.balance,
            password=account_payload.password,

            # backpopulates makes it so customer knows new account has been appended to its list
            customer=customer
        )

        db_account = self.account_repo.save_account(new_account)
        print(db_account.__repr__())
        return db_account

    def find_account(self, account_id: int):
        db_account = self.account_repo.load_account(account_id)
        return db_account


        
        