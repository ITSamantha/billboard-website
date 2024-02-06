from fastapi import Depends

from src.database.models import AdStatus
from ..base_crud_repository import SqlAlchemyRepository
from src.database.session_manager import get_session

ad_status_repository = SqlAlchemyRepository(model=AdStatus, db_session=Depends(get_session))
