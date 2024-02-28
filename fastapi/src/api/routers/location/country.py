from typing import Union

from fastapi import APIRouter, Request

from src import schemas
from src.api.responses.api_response import ApiResponse
from src.database import models
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.schemas import create_country_response
from src.utils.validator import Validator
from src.utils.validator.validator import Rules

country_router = APIRouter(
    prefix="/countries"
)


@country_router.get(path='/country/{country_id}', response_model=Union[schemas.CountryResponse, ApiResponse])
async def get_country(country_id: int):
    """Get exact country. """

    try:
        country: models.Country = await SqlAlchemyRepository(db_manager.get_session,
                                                             models.Country).get_single(id=country_id)
        if not country:
            raise Exception(f"This country does not exist.")

        result: schemas.CountryResponse = create_country_response(country)
        return result
    except Exception as e:
        return ApiResponse.error(str(e))


@country_router.put(path='/country/{country_id}', response_model=Union[schemas.CountryResponse, ApiResponse])
async def update_country(country_id: int, request: Request):
    """Update exact Country. """

    validator = Validator(await request.json(), {
        'title': [Rules.REQUIRED, Rules.STRING]
    }, {}, schemas.CountryUpdate())

    payload: schemas.CountryUpdate = validator.validated()

    try:
        # todo : check existance
        country: models.Country = await SqlAlchemyRepository(db_manager.get_session,
                                                             models.Country).update(payload, id=country_id)

        result: schemas.CountryResponse = create_country_response(country)
        return result
    except Exception as e:
        return ApiResponse.error(str(e))
