from typing import Union, List

from fastapi import APIRouter, Depends, Request

from src.api.dependencies.auth import Auth
from src.api.responses.api_response import ApiResponse
from src.api.transformers.address_transformer import AddressTransformer
from src.utils.transformer import transform
from src.database import models
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.utils.validator import Validator

address_router = APIRouter(
    prefix="/addresses"
)


@address_router.get(path='/{address_id}')
async def get_address(address_id: int, request: Request, auth: Auth = Depends()):
    """Get exact address. """

    await auth.check_access_token(request)

    try:
        address: models.Address = await SqlAlchemyRepository(db_manager.get_session, models.Address) \
            .get_single(id=address_id)
        if not address:
            raise Exception("Address is not found.")

        return ApiResponse.payload(transform(address, AddressTransformer()))
    except Exception as e:
        return ApiResponse.error(str(e))


@address_router.get(path='')
async def get_user_addresses(user_id: int, request: Request, auth: Auth = Depends()):
    """Get user addresses. """

    await auth.check_access_token(request)

    try:
        advertisements: List[models.Advertisement] = await SqlAlchemyRepository(db_manager.get_session,
                                                                                models.Advertisement) \
            .get_multi(user_id=user_id)

        addresses: List[models.Address] = list(set([ad.address for ad in advertisements]))

        return ApiResponse.payload(transform(addresses, AddressTransformer()))
    except Exception as e:
        return ApiResponse.error(str(e))


@address_router.post(path='')
async def create_ad_address(request: Request, auth: Auth = Depends()):
    """Create address. """

    await auth.check_access_token(request)

    validator = Validator(await request.json(), {
        'address': ['required', 'string'],
        'city_id': ['nullable', 'integer'],
        'country_id': ['nullable', 'integer'],
        'street': ['nullable', 'string'],
        'house': ['nullable', 'string'],
        'flat': ['nullable', 'string'],
        'longitude': ['nullable', 'float'],
        'latitude': ['nullable', 'float'],
    })

    validator.validated()

    try:
        address: models.Address = await SqlAlchemyRepository(db_manager.get_session, models.Address) \
            .create(validator.all())

        return ApiResponse.payload(transform(address, AddressTransformer()))
    except Exception as e:
        return ApiResponse.error(str(e))
