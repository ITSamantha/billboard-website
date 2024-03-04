from typing import Union

from fastapi import APIRouter
from sqlalchemy.orm import selectinload

from src import schemas
from src.api.responses.api_response import ApiResponse
from src.database import models
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.schemas.entities.category import create_category, Category

router = APIRouter(
    prefix="/categories",
    tags=["categories"],
)


@router.get("/category/{category_id}", response_model=Union[Category, ApiResponse])
async def get_categories(category_id: int):
    """Get nested category. """

    # TODO: NESTED PARENT
    try:
        category: models.Category = await SqlAlchemyRepository(db_manager.get_session,
                                                               models.Category).get_single(id=category_id)
        result: Category = create_category(category)
        return result
    except Exception as e:
        return ApiResponse.error(str(e))
