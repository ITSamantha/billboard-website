import json
from typing import List

from fastapi import APIRouter, UploadFile, Request, Depends
from src.api.dependencies.auth import Auth
from src.api.responses.api_response import ApiResponse
from src.api.transformers.category_transformer import CategoryTransformer
from src.api.transformers.filter.filter_transformer import FilterTransformer
from src.database import models
from src.database.models import CategoryFilter
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.repository.crud.category_repository import CategoryRepository
from src.utils.transformer import transform
from src.utils.validator import Validator

router = APIRouter(
    prefix="/categories",
    tags=["categories"],
)


@router.get("/{category_id}")
async def get_category_by_id(category_id: int, request: Request, auth: Auth = Depends()):
    # await auth.check_access_token(request)
    """Get nested category. """

    try:
        category: models.Category = await CategoryRepository(db_manager.get_session,
                                                             models.Category).get_single(id=category_id)
        return ApiResponse.payload(transform(
            category,
            CategoryTransformer().include(["children"]))
        )
    except Exception as e:
        return ApiResponse.error(str(e))


@router.post("")
async def create_category(request: Request, auth: Auth = Depends()):
    """Create category."""
    await auth.check_access_token(request)

    validator = Validator(await request.json(), {
        'id': ['nullable', 'integer'],
        'title': ['required', 'string'],
        'order': ['required', 'integer'],
        'meta_title': ['required', 'string'],
        'meta_description': ['required', 'string'],
        'url': ['required', 'string'],
        'parent_id': ['nullable', 'integer'],
        'bookable': ['required', 'bool'],
        'map_addressable': ['required', 'bool']
    })

    validator.validated()

    try:

        category: models.Category = await CategoryRepository(db_manager.get_session, models.Category) \
            .create(validator.all())

        return ApiResponse.payload({"category_id": category.id})  # TODO: CHECK?
    except Exception as e:
        return ApiResponse.error(str(e))


@router.put("/{category_id}")
async def update_category(category_id: int, request: Request, auth: Auth = Depends()):
    await auth.check_access_token(request)

    validator = Validator(await request.json(), {
        'title': ['nullable', 'string'],
        'order': ['nullable', 'integer'],
        'meta_title': ['nullable', 'string'],
        'meta_description': ['nullable', 'string'],
        'url': ['nullable', 'string'],
        'parent_id': ['nullable', 'integer'],
        'bookable': ['nullable', 'bool'],
        'map_addressable': ['nullable', 'bool']
    })

    validator.validated()

    try:
        category: models.Category = await CategoryRepository(db_manager.get_session, models.Category) \
            .update(validator.not_null(), id=category_id)

        return ApiResponse.payload(transform(category, CategoryTransformer()))
    except Exception as e:
        return ApiResponse.error(str(e))


@router.get("")
async def get_categories(request: Request, auth: Auth = Depends()):
    """Get all nested category. """

    # await auth.check_access_token(request)

    try:
        categories: List[models.Category] = await CategoryRepository(db_manager.get_session,
                                                                     models.Category).get_multi(order="order")
        # TODO: ADD ORDER BY COLUMN
        return ApiResponse.payload(transform(
            categories,
            CategoryTransformer().include(["children"])
        ))

    except Exception as e:
        return ApiResponse.error(str(e))


@router.get("/{category_id}/filters")
async def get_filters_by_category_id(category_id: int, request: Request, auth: Auth = Depends()):
    # await auth.check_access_token(request)

    try:
        filters: List[CategoryFilter] = await SqlAlchemyRepository(db_manager.get_session, CategoryFilter) \
            .get_multi(order="filter_id", category_id=category_id)

        return ApiResponse.payload(transform([filter.filter for filter in filters], FilterTransformer().include(["filter_values"])))
    except Exception as e:
        return ApiResponse.error(str(e))


@router.post("/upload_file")
async def upload_categories_file(file: UploadFile, request: Request, auth: Auth = Depends()):
    await auth.check_access_token(request)

    try:

        if "json" not in file.content_type:
            raise Exception("The file me be a correct json file.")

        json_data = json.load(file.file)

        for i, data in enumerate(json_data):
            validator = Validator(data, {
                'id': ['nullable', 'integer'],
                'title': ['required', 'string'],
                'order': ['required', 'integer'],
                'meta_title': ['required', 'string'],
                'meta_description': ['required', 'string'],
                'url': ['required', 'string'],
                'parent_id': ['nullable', 'integer'],
                'bookable': ['required', 'bool'],
                'map_addressable': ['required', 'bool']
            })

            validator.validated()
            json_data[i] = validator.all()

        categories: List[models.Category] = await CategoryRepository(db_manager.get_session, models.Category) \
            .bulk_create(json_data)

        return {"categories": [category.id for category in categories]}  # TODO: CHECK?
    except Exception as e:
        return ApiResponse.error(str(e))
