from infrastructure.database import get_db_session
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import Depends

DBSession = Annotated[Session, Depends(get_db_session)]
