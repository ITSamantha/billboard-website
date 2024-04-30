from typing import List

from fastapi import APIRouter, Request, Depends

from src.api.dependencies.auth import Auth
from src.api.responses.api_response import ApiResponse
from src.api.transformers.filter.filter_transformer import FilterTransformer
from src.api.transformers.filter.filter_type_transformer import FilterTypeTransformer
from src.api.transformers.filter.filter_value_transformer import FilterValueTransformer
from src.database.models import Filter, FilterType, FilterValue
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.utils.transformer import transform

router = APIRouter(
    prefix="/filters",
    tags=["filters"],
)


@router.get("")
async def get_filters(request: Request, auth: Auth = Depends()):
    # await auth.check_access_token(request)

    try:
        filters: List[Filter] = await SqlAlchemyRepository(db_manager.get_session, Filter) \
            .get_multi()

        return ApiResponse.payload(transform(filters, FilterTransformer()))
    except Exception as e:
        return ApiResponse.error(str(e))


@router.get("/filter_types")
async def get_filter_types(request: Request, auth: Auth = Depends()):
    # await auth.check_access_token(request)

    try:
        filter_types: List[FilterType] = await SqlAlchemyRepository(db_manager.get_session, FilterType) \
            .get_multi()

        return ApiResponse.payload(transform(filter_types, FilterTypeTransformer()))
    except Exception as e:
        return ApiResponse.error(str(e))


@router.get("/{filter_id}/filter_values")
async def get_filter_values(filter_id: int, request: Request, auth: Auth = Depends()):
    # await auth.check_access_token(request)

    try:
        filter_values: List[FilterValue] = await SqlAlchemyRepository(db_manager.get_session, FilterValue) \
            .get_multi(filter_id=filter_id)

        return ApiResponse.payload(transform(filter_values, FilterValueTransformer()))
    except Exception as e:
        return ApiResponse.error(str(e))
