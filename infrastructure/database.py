from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from pathlib import Path

class Base(DeclarativeBase):
    pass

BASE_DIR = Path(__file__).resolve().parent.parent
db_path = BASE_DIR / "bank.db"
db_url = f"sqlite:///{db_path}"

engine = create_engine(db_url)

SessionLocal = sessionmaker(bind=engine)

def get_db_session():
    db = SessionLocal() # creates the session
    try:
        yield db
    finally:
        db.close()