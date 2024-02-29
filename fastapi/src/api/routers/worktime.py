from typing import List, Union

from fastapi import APIRouter

from src import schemas
from src.api.responses.api_response import ApiResponse
from src.database import models
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.schemas import create_worktime

router = APIRouter(
    prefix="/worktime",
    tags=["worktime"]
)


@router.get("/{advertisement_id}", response_model=Union[List[schemas.Worktime], ApiResponse])
async def get_advertisement_worktime(advertisement_id: int):
    try:
        ad_worktime: List[models.Worktime] = await SqlAlchemyRepository(db_manager.get_session,
                                                                        models.Worktime).get_multi(
            advertisement_id=advertisement_id)

        worktime: List[schemas.Worktime] = [create_worktime(ad) for ad in ad_worktime]
        return worktime

    except Exception as e:
        return ApiResponse.error(str(e))
