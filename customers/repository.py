from .schema import CustomerCreate, CustomerUpdate
from .models import Customer
from sqlalchemy.orm import Session

class CustomerRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def save_customer(self, customer_payload: CustomerCreate) -> Customer:
        # transient (nothing to do with the db yet)
        db_customer = Customer(
            fullname=customer_payload.fullname,
            email=customer_payload.email
        )

        # pending (associated with a session, part of a transaction ready to be flushed and persisted in a connection)
        self.session.add(db_customer)
        self.session.commit()
        self.session.refresh(db_customer)

        return db_customer
    
    def get_customer(self, customer_id: int) -> Customer:
        db_customer = self.session.get(Customer, customer_id)

        if not db_customer:
            raise ValueError(f"No saved customer with id {customer_id}")

        return db_customer

    def update_customer(self, customer_id: int, customer_payload: CustomerUpdate) -> Customer:
        customer = self.get_customer(customer_id)
        customer_update_fields = customer_payload.model_dump(exclude_unset=True)

        for key, value in customer_update_fields.items():
            setattr(customer, key, value)

        self.session.add(customer)
        self.session.commit()
        self.session.refresh(customer)

        return customer

    def delete_customer(self, customer_id: int) -> Customer:
        customer = self.get_customer(customer_id)
        self.session.delete(customer)
        self.session.commit()
        return customer