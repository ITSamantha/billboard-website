from typing import Union

from fastapi import APIRouter

from src import schemas
from src.api.responses.api_response import ApiResponse
from src.database import models
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.schemas import create_country_response, create_address_response

address_router = APIRouter(
    prefix="/addresses"
)


@address_router.get(path='/address/{address_id}', response_model=Union[schemas.AddressResponse, ApiResponse])
async def get_address(address_id: int):
    """Get exact address. """

    try:
        address: models.Address = await SqlAlchemyRepository(db_manager.get_session,
                                                             models.Address).get_single(id=address_id)
        if not address:
            raise Exception(f"This address does not exist.")

        result: schemas.AddressResponse = create_address_response(address)
        return result
    except Exception as e:
        return ApiResponse.error(str(e))
