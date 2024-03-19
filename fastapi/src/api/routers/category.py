import json
from typing import List
from fastapi import APIRouter, UploadFile, Request
from src.api.responses.api_response import ApiResponse
from src.api.transformers.category_transformer import CategoryTransformer
from src.database import models
from src.database.session_manager import db_manager
from src.repository.crud.category_repository import CategoryRepository
from src.utils.transformer import transform
from src.utils.validator import Validator

router = APIRouter(
    prefix="/categories",
    tags=["categories"],
)


@router.get("/{category_id}")
async def get_category_by_id(category_id: int):
    """Get nested category. """

    try:
        category: models.Category = await CategoryRepository(db_manager.get_session,
                                                             models.Category).get_single(id=category_id)
        return ApiResponse.payload(transform(
            category,
            CategoryTransformer().include(["children"])
        ))
    except Exception as e:
        print(e.__traceback__)
        return ApiResponse.error(str(e))


@router.post("")
async def create_category(request: Request):
    """Create category."""
    # await auth.check_access_token(request)

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
async def update_category(category_id: int, request: Request):
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
        review: models.Review = await CategoryRepository(db_manager.get_session, models.Review) \
            .update(validator.not_null(), id=category_id)

        return ApiResponse.payload(transform(review, CategoryTransformer()))
    except Exception as e:
        return ApiResponse.error(str(e))





@router.get("")
async def get_categories():
    """Get all nested category. """

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


@router.post("/uploadfile")
async def create_upload_file(file: UploadFile):
    try:
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
