from typing import List, Union

from fastapi import APIRouter
from starlette.responses import JSONResponse

from src import schemas
from src.api.responses.api_response import ApiResponse
from src.database import models
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.schemas import create_worktime_response

router = APIRouter(
    prefix="/worktime",
    tags=["worktime"]
)


@router.get("/{advertisement_id}", response_model=Union[List[schemas.WorktimeResponse], ApiResponse])
async def get_ad_worktime(advertisement_id: int):
    try:
        ad_worktime: List[models.Worktime] = await SqlAlchemyRepository(db_manager.get_session,
                                                                        models.Worktime).get_multi(
            advertisement_id=advertisement_id)

        worktime = [create_worktime_response(ad) for ad in ad_worktime]
        return worktime

    except Exception as e:
        return ApiResponse.error(str(e))
