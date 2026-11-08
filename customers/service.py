from .repository import CustomerRepository
from sqlalchemy.orm import Session
from .schema import CustomerCreate, CustomerUpdate
from .models import Customer


class CustomerService:
    def __init__(self, repo: CustomerRepository, session: Session) -> None:
        self.repo = repo
        self.session = session

    def create_customer(self, payload: CustomerCreate) -> Customer:
        try:
            new_customer = Customer(
                fullname=payload.fullname,
                email=payload.email
            )

            saved_customer = self.repo.save(new_customer)
            self.session.commit()
            return saved_customer
        except Exception:
            self.session.rollback()
            raise


    def get_customer(self, customer_id: int) -> Customer:
        return self.repo.get(customer_id)


    def update_customer(self, customer_id: int, payload: CustomerUpdate) -> Customer:
        try:
            customer = self.repo.get(customer_id)
            update_data = payload.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(customer, key, value)

            self.session.commit()
            self.session.refresh(customer)
            return customer
        except Exception:
            self.session.rollback()
            raise


    def delete_customer(self, customer_id: int) -> Customer:
        try:
            customer = self.repo.get(customer_id)
            self.repo.delete(customer)
            self.session.commit()
            return customer
        except Exception:
            self.session.rollback()
            raise