from fastapi import APIRouter, Request, Depends

from src.api.dependencies.auth import Auth
from src.api.responses.api_response import ApiResponse
from src.api.transformers.country_transformer import CountryTransformer
from src.utils.transformer import transform
from src.database import models
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.schemas.characteristics.country import CountryUpdate
from src.utils.validator import Validator

country_router = APIRouter(
    prefix="/countries"
)


@country_router.get(path='/{country_id}')
async def get_country(country_id: int, request: Request, auth: Auth = Depends()):
    """Get exact country. """

    await auth.check_access_token(request)

    try:
        country: models.Country = await SqlAlchemyRepository(db_manager.get_session, models.Country)\
            .get_single(id=country_id)
        if not country:
            raise Exception("Country is not found.")

        return ApiResponse.payload(transform(country, CountryTransformer()))
    except Exception as e:
        return ApiResponse.error(str(e))


@country_router.put(path='/{country_id}')
async def update_country(country_id: int, request: Request, auth: Auth = Depends()):
    """Update exact Country. """

    await auth.check_access_token(request)

    validator = Validator(await request.json(), {
        'title': ['required', 'string']
    }, {}, CountryUpdate())

    payload: CountryUpdate = validator.validated()

    try:
        # todo : check existence
        country: models.Country = await SqlAlchemyRepository(db_manager.get_session, models.Country)\
            .update(payload.all(), id=country_id)

        return ApiResponse.payload(transform(country, CountryTransformer()))
    except Exception as e:
        return ApiResponse.error(str(e))
