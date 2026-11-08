from infrastructure.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Wire(Base):
    __tablename__ = "wires"

    id: Mapped[int] = mapped_column(primary_key=True)
    amount: Mapped[float] #redundant? think about it

    #transfers: Mapped[list["Transfer"]] = relationship(overlaps="wire")