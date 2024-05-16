from fastapi import APIRouter, Request, Depends

from src.api.dependencies.auth import Auth
from src.api.responses.api_response import ApiResponse
from src.api.transformers.tariff_transformer import TariffTransformer
from src.database.models import Tariff
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.utils.transformer import transform

router = APIRouter(
    prefix="/tariffs",
)


@router.get("/")
async def send(request: Request, auth: Auth = Depends()):

    try:
        tariffs = await SqlAlchemyRepository(db_manager.get_session, Tariff)\
            .get_multi()

        return ApiResponse.payload(transform(tariffs, TariffTransformer()))
    except Exception as e:
        return ApiResponse.error(str(e))


@router.get("/{tariff_id}")
async def find(tariff_id: int, request: Request, auth: Auth = Depends()):
    # await auth.check_access_token(request)

    try:
        tariff: Tariff = await SqlAlchemyRepository(db_manager.get_session, Tariff) \
            .get_single(id=tariff_id)
        if not tariff:
            raise Exception("Address is not found.")

        return ApiResponse.payload(transform(tariff, TariffTransformer()))
    except Exception as e:
        return ApiResponse.error(str(e))

@router.post("/")
async def store(request: Request, auth: Auth = Depends()):
    return ApiResponse.success('not implemented')

@router.put("/{tariff_id}")
async def update(tariff_id: int, request: Request, auth: Auth = Depends()):
    return ApiResponse.success('not implemented')

@router.delete("/{tariff_id}")
async def destroy(tariff_id: int, request: Request, auth: Auth = Depends()):
    return ApiResponse.success('not implemented')
