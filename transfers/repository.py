from sqlalchemy.orm import Session
from .models import Transfer

class TransferRepository:
    def __init__(self, session: Session):
        self.session = session

    def save(self, transfer: Transfer):
        self.session.add(transfer)
        self.session.flush()
        self.session.refresh(transfer)

        return transfer