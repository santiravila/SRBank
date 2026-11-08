from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Date, DateTime
from enum import Enum
import datetime


class Base(DeclarativeBase):
    pass


class Customer(Base):
    __tablename__ = "customer"

    id: Mapped[int] = mapped_column(primary_key=True)
    fullname: Mapped[str] = mapped_column(String(64))
    email: Mapped[str] = mapped_column(String(64)) # refactor to real email
    registered_at: Mapped[datetime.date] = mapped_column(Date)

    accounts: Mapped[list["Account"]] = relationship(back_populates="customer")


class AccountType(Enum):
    CHECKINGS = "checkings"
    SAVINGS =  "savings"


class Account(Base):
    __tablename__ = "account"

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[AccountType] = mapped_column(nullable=False)
    balance: Mapped[float] = mapped_column()
    password_hash: Mapped[str] = mapped_column()
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime)

    customer: Mapped["Customer"] = relationship(back_populates="accounts")


class TransactionType(Enum):
    CREDIT = "credit"
    DEBIT = "debit"

class Transaction(Base):
    __tablename__ = "transaction"

    id: Mapped[int] = mapped_column(primary_key=True)
    amount: Mapped[float] = mapped_column()
    type: Mapped[TransactionType] = mapped_column()
    timestamp: Mapped[datetime.datetime] = mapped_column(DateTime)

