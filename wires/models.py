from infrastructure.database import Base
from sqlalchemy import ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

class Wire(Base):
    __tablename__ = "wires"

    id: Mapped[int] = mapped_column(primary_key=True)
    amount: Mapped[float] = mapped_column(CheckConstraint("amount > 0"))
    timestamp: Mapped[datetime] = mapped_column(default=datetime.now)

    sender_account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id"), nullable=False)
    receiver_account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id"), nullable=False) 

    #transfers: Mapped[list["Transfer"]] = relationship(overlaps="wire")