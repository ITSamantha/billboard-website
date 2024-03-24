from typing import List

from fastapi import APIRouter, UploadFile, Request, Depends
from src.api.dependencies.auth import Auth
from src.api.responses.api_response import ApiResponse
from src.api.transformers.category_transformer import CategoryTransformer
from src.database import models
from src.database.session_manager import db_manager
from src.repository.crud.category_repository import CategoryRepository
from src.utils.transformer import transform

router = APIRouter(
    prefix="/categories",
    tags=["categories"],
)


@router.get("/{category_id}")
async def get_category_by_id(category_id: int, request: Request, auth: Auth = Depends()):
    await auth.check_access_token(request)
    """Get nested category. """

    try:
        category: models.Category = await CategoryRepository(db_manager.get_session,
                                                             models.Category).get_single(id=category_id)
        return ApiResponse.payload(transform(
            category,
            CategoryTransformer().include(['children'])
        ))
    except Exception as e:
        print(e.__traceback__)
        return ApiResponse.error(str(e))


@router.get("")
async def get_categories(request: Request, auth: Auth = Depends()):
    await auth.check_access_token(request)
    """Get all nested category. """

    try:
        categories: List[models.Category] = await CategoryRepository(db_manager.get_session,
                                                                     models.Category).get_multi(order="order")
        # TODO: ADD ORDER BY COLUMN
        return ApiResponse.payload(transform(
            categories,
            CategoryTransformer().include(['children'])
        ))
    except Exception as e:
        return ApiResponse.error(str(e))


@router.post("/uploadfile")
async def create_upload_file(file: UploadFile, request: Request, auth: Auth = Depends()):
    await auth.check_access_token(request)
    return {"filename": file.filename}
