from infrastructure.database import Base
from infrastructure import models
from sqlalchemy import DateTime, Enum as SQLEnum, ForeignKey, CheckConstraint
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship, validates
from enum import Enum

class AccountType(Enum):
    CURRENT="current"
    SAVINGS="savings"


class Account(Base):
    __tablename__ = "accounts"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    account_type: Mapped[AccountType] = mapped_column(
        SQLEnum(AccountType)
    )
    balance: Mapped[float] = mapped_column(CheckConstraint("balance >= 0"))
    password: Mapped[str] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.id"))

    customer: Mapped["Customer"] = relationship(back_populates="accounts")
    transfers: Mapped[list["Transfer"]] = relationship(back_populates="account")


    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self.balance < amount:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    def __repr__(self):
        return f"id:{self.id}, accounttype:{self.account_type}, balance: {self.balance}, password: {self.password}, created_at: {self.created_at}, customer_id:{self.customer_id}"