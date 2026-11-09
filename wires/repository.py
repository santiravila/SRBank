from sqlalchemy.orm import Session
from .models import Wire

class WireRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def save(self, wire: Wire) -> Wire:
        self.session.add(wire)
        self.session.flush()
        self.session.refresh(wire)
        return wire