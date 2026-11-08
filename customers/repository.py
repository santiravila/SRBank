from .models import Customer
from sqlalchemy.orm import Session

class CustomerRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def save(self, customer: Customer) -> Customer:
        self.session.add(customer)
        self.session.flush()
        self.session.refresh(customer)

        return customer
    
    def get(self, customer_id: int) -> Customer:
        db_customer = self.session.get(Customer, customer_id)

        if not db_customer:
            raise ValueError(f"No saved customer with id {customer_id}")

        return db_customer


    def delete(self, customer: Customer) -> None:
        self.session.delete(customer)
        self.session.flush()