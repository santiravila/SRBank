from datetime import datetime
from sqlalchemy import String, DateTime
from sqlalchemy.orm import mapped_column, Mapped, relationship
from infrastructure.database import Base


class Customer(Base):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(primary_key=True)
    fullname: Mapped[str] = mapped_column(String(64), nullable=False)
    email: Mapped[str] = mapped_column(String(64), unique=True, nullable=False)
    registered_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    accounts: Mapped[list["Account"]] = relationship(back_populates="customer")


