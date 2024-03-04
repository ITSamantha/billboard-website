from typing import Union

from fastapi import APIRouter, Depends, Request

from src.api.dependencies.auth import Auth
from src.api.responses.api_response import ApiResponse
from src.database import models
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.schemas.entities import create_address, Address, AddressCreate, validate_address_create

address_router = APIRouter(
    prefix="/addresses"
)


@address_router.get(path='/address/{address_id}', response_model=Union[Address, ApiResponse])
async def get_address(address_id: int):
    """Get exact address. """

    try:
        address: models.Address = await SqlAlchemyRepository(db_manager.get_session,
                                                             models.Address).get_single(id=address_id)
        if not address:
            raise Exception(f"This address does not exist.")

        result: Address = create_address(address)
        return result
    except Exception as e:
        return ApiResponse.error(str(e))


@address_router.post(path='/address', response_model=Union[Address, ApiResponse])
async def create_ad_address(request: Request, auth: Auth = Depends()):
    """Create address. """

    await auth.check_access_token(request)

    payload: AddressCreate = validate_address_create(await request.json())

    try:
        address: models.Address = await SqlAlchemyRepository(db_manager.get_session,
                                                             models.Address).create(payload)
        result: Address = create_address(address)
        return result
    except Exception as e:
        return ApiResponse.error(str(e))
