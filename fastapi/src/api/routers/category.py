from fastapi import APIRouter, Depends, Request
from src.api.dependencies.auth import Auth
from src.api.responses.api_response import ApiResponse
from src.api.transformers.category_transformer import CategoryTransformer
from src.database import models
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.utils.transformer import transform

router = APIRouter(
    prefix="/categories",
    tags=["categories"],
)


@router.get("/{category_id}")
async def get_categories(category_id: int, request: Request, auth: Auth = Depends()):
    """Get nested category. """
    await auth.check_access_token(request)

    # TODO: NESTED PARENT
    try:
        #cat_rep = await CategoryRepository(db_manager.get_session).get_children_list(1)
        category: models.Category = await SqlAlchemyRepository(db_manager.get_session, models.Category)\
            .get_single(id=category_id)

        return ApiResponse.payload(transform(
            category,
            CategoryTransformer()
        ))
    except Exception as e:
        return ApiResponse.error(str(e))
