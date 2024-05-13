import json
from typing import List

from fastapi import APIRouter, UploadFile, Request, Depends
from sqlalchemy import select

from src.api.dependencies.auth import Auth
from src.api.responses.api_response import ApiResponse
from src.api.transformers.category_transformer import CategoryTransformer
from src.api.transformers.filter.filter_transformer import FilterTransformer
from src.database import models
from src.database.models import CategoryFilter, File, Category
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.repository.crud.category_repository import CategoryRepository
from src.utils.storage import storage
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
        'map_addressable': ['required', 'bool'],
        'image': ['nullable', 'string'],
    })

    data = validator.validated()

    try:
        file = None
        if 'image' in data:
            file = await File.save(data['image'])

        category: models.Category = await CategoryRepository(db_manager.get_session, models.Category) \
            .create(validator.all() | {'image_id': file.id if file else None})

        return ApiResponse.payload({"category_id": category.id})  # TODO: CHECK?
    except Exception as e:
        return ApiResponse.error(str(e))


@router.put("/{category_id}")
async def update_category(category_id: int, request: Request, auth: Auth = Depends()):
    await auth.check_access_token(request)

    validator = Validator(await request.json(), {
        'title': ['required', 'string'],
        'order': ['required', 'integer'],
        'meta_title': ['required', 'string'],
        'meta_description': ['required', 'string'],
        'url': ['required', 'string'],
        'parent_id': ['nullable', 'integer'],
        'bookable': ['required', 'bool'],
        'map_addressable': ['required', 'bool'],
        'image_id': ['nullable', 'integer'],
        'image': ['nullable', 'string'],
    })

    data = validator.validated()

    try:
        async with db_manager.get_session() as session:
            q = select(Category)\
                .where(Category.id == category_id)
            res = await session.execute(q)
            category = res.scalar()

        category.title = data['title']
        category.order = data['order']
        category.meta_title = data['meta_title']
        category.meta_description = data['meta_description']
        category.url = data['url']
        category.parent_id = data['parent_id']
        category.bookable = data['bookable']
        category.map_addressable = data['map_addressable']

        if data['image_id']:
            pass
        else:
            if data['image']:
                file = await File.save(data['image'])
                category.image_id = file.id
            else:
                if category.image:
                    storage.remove(category.image)
                category.image_id = None

        async with db_manager.get_session() as session:
            await session.commit()

        return ApiResponse.payload(transform(category, CategoryTransformer()))
    except Exception as e:
        return ApiResponse.error(str(e))


@router.get("")
async def get_categories():
    """Get all nested category. """

    # todo join all levels to make only one query
    # await auth.check_access_token(request)
    try:
        categories: List[models.Category] = await CategoryRepository(db_manager.get_session, models.Category) \
            .get_multi(order="order", parent_id=None)
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

        return ApiResponse.payload(
            transform([filter.filter for filter in filters], FilterTransformer().include(["filter_values"])))
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
