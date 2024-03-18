from typing import List

from fastapi import APIRouter, Depends, Request
from src.api.dependencies.auth import Auth
from src.api.responses.api_response import ApiResponse
from src.api.transformers.category_transformer import CategoryTransformer
from src.database import models
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.repository.crud.category_repository import CategoryRepository
from src.utils.transformer import transform

router = APIRouter(
    prefix="/categories",
    tags=["categories"],
)


@router.get("/{category_id}")
async def get_category_by_id(category_id: int, request: Request, auth: Auth = Depends()):
    """Get nested category. """

    try:
        category: models.Category = await CategoryRepository(db_manager.get_session,
                                                             models.Category).get_single(id=category_id)

        return ApiResponse.payload(transform(
            category,
            CategoryTransformer()
        ))
    except Exception as e:
        return ApiResponse.error(str(e))


@router.get("")
async def get_categories():
    try:
        categories: List[models.Category] = await CategoryRepository(db_manager.get_session,
                                                                     models.Category).get_multi()

        return ApiResponse.payload(transform(
            categories,
            CategoryTransformer()
        ))
    except Exception as e:
        return ApiResponse.error(str(e))
