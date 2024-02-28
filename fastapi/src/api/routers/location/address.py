from typing import Union

from fastapi import APIRouter, Depends, Request

from src import schemas
from src.api.dependencies.auth import Auth
from src.api.responses.api_response import ApiResponse
from src.database import models
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.schemas import create_address, AddressCreate, Address
from src.utils.validator import Validator
from src.utils.validator.validator import Rules

address_router = APIRouter(
    prefix="/addresses"
)


@address_router.get(path='/address/{address_id}', response_model=Union[schemas.Address, ApiResponse])
async def get_address(address_id: int):
    """Get exact address. """

    try:
        address: models.Address = await SqlAlchemyRepository(db_manager.get_session,
                                                             models.Address).get_single(id=address_id)
        if not address:
            raise Exception(f"This address does not exist.")

        result: schemas.Address = create_address(address)
        return result
    except Exception as e:
        return ApiResponse.error(str(e))


@address_router.post(path='/address', response_model=Union[schemas.Address, ApiResponse])
async def create_ad_address(request: Request, auth: Auth = Depends()):
    """Create address. """

    await auth.check_access_token(request)

    validator = Validator(await request.json(), {
        'address': [Rules.REQUIRED, Rules.STRING],
        'city_id': [Rules.INTEGER],
        'country_id': [Rules.INTEGER],
        'street': [Rules.STRING],
        'house': [Rules.STRING],
        'flat': [Rules.STRING],
        'longitude': [Rules.FLOAT],
        'latitude': [Rules.FLOAT]
    }, {}, AddressCreate())

    payload: AddressCreate = validator.validated()

    try:

        address: models.Address = await SqlAlchemyRepository(db_manager.get_session,
                                                             models.Address).create(payload)
        result: schemas.Address = create_address(address)
        return result
    except Exception as e:
        return ApiResponse.error(str(e))
