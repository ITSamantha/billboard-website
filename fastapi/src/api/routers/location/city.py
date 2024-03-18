from typing import Union

from fastapi import APIRouter, Request, Depends

from src.api.dependencies.auth import Auth
from src.api.responses.api_response import ApiResponse
from src.api.transformers.city_transformer import CityTransformer
from src.utils.transformer import transform
from src.database import models
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.schemas.characteristics.city import City, CityUpdate
from src.utils.validator import Validator

city_router = APIRouter(
    prefix="/cities"
)


@city_router.get(path='/{city_id}')
async def get_city(city_id: int, request: Request, auth: Auth = Depends()):
    """Get exact city. """

    await auth.check_access_token(request)

    try:
        city: models.City = await SqlAlchemyRepository(db_manager.get_session, models.City)\
            .get_single(id=city_id)
        if not city:
            raise Exception("City is not found.")

        return ApiResponse.payload(transform(city, CityTransformer()))
    except Exception as e:
        return ApiResponse.error(str(e))


@city_router.put(path='/{city_id}', response_model=Union[City, ApiResponse])
async def update_city(city_id: int, request: Request, auth: Auth = Depends()):
    """Update exact city. """

    await auth.check_access_token(request)

    validator = Validator(await request.json(), {
        'title': ['required', 'string']
    }, {}, CityUpdate())

    payload: CityUpdate = validator.validated()

    try:
        # todo : check existence
        city: models.City = await SqlAlchemyRepository(db_manager.get_session, models.City)\
            .update(payload.all(), id=city_id)

        return ApiResponse.payload(transform(city, CityTransformer()))
    except Exception as e:
        return ApiResponse.error(str(e))
