from typing import Union

from fastapi import APIRouter, Request

from src import schemas
from src.api.responses.api_response import ApiResponse
from src.database import models
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.schemas.characteristics.city import City, create_city, CityUpdate
from src.utils.validator import Validator
from src.utils.validator.validator import Rules

city_router = APIRouter(
    prefix="/cities"
)


@city_router.get(path='/city/{city_id}', response_model=Union[City, ApiResponse])
async def get_city(city_id: int):
    """Get exact city. """

    try:
        city: models.City = await SqlAlchemyRepository(db_manager.get_session,
                                                       models.City).get_single(id=city_id)
        if not city:
            raise Exception(f"This city does not exist.")

        result: City = create_city(city)
        return result
    except Exception as e:
        return ApiResponse.error(str(e))


@city_router.put(path='/city/{city_id}', response_model=Union[City, ApiResponse])
async def update_city(city_id: int, request: Request):
    """Update exact city. """

    validator = Validator(await request.json(), {
        'title': [Rules.REQUIRED, Rules.STRING]
    }, {}, CityUpdate())

    payload: CityUpdate = validator.validated()

    try:
        # todo : check existence
        city: models.City = await SqlAlchemyRepository(db_manager.get_session,
                                                       models.City).update(payload, id=city_id)

        result: City = create_city(city)
        return result
    except Exception as e:
        return ApiResponse.error(str(e))
