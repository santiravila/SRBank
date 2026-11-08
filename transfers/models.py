from infrastructure.database import Base
from sqlalchemy import ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from common.enums import TransferType


class Transfer(Base):
    __tablename__ = "transfers"

    id: Mapped[int] = mapped_column(primary_key=True)
    amount: Mapped[float] = mapped_column(nullable=False)
    transfer_type: Mapped[TransferType] = mapped_column(
        SQLEnum(TransferType)
    )
    timestamp: Mapped[datetime] = mapped_column(default=datetime.now)

    account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id"), nullable=False)
    account: Mapped["Account"] = relationship()

    #wire_id: Mapped[int] = mapped_column(ForeignKey("wires.id"))
    #wire: Mapped["Wire"] = relationship()