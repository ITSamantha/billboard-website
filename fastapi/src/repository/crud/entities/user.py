from fastapi import Depends

from src.database.models import User
from ..base_crud_repository import SqlAlchemyRepository
from src.database.session_manager import get_session

user_repo = SqlAlchemyRepository(model=User, db_session=Depends(get_session))
