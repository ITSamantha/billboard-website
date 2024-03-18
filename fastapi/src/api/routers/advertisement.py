from typing import List, Union

from fastapi import APIRouter, Depends, Request

from src.api.dependencies.auth import Auth
from src.api.responses.api_response import ApiResponse
from src.api.transformers.advertisement import AdTypeTransformer
from src.api.transformers.review_transformer import ReviewTransformer
from src.api.transformers.worktime_transformer import WorktimeTransformer
from src.database import models
from src.database.models import Address, AdStatus, AdvertisementAdTag
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.utils.validator import Validator
from src.utils.transformer import transform
from src.api.transformers.advertisement.advertisement_transformer import AdvertisementTransformer
from src.schemas.entities.worktime import create_worktime, Worktime

router = APIRouter(
    prefix="/advertisements",
    tags=["advertisements"],
)


@router.post("")
async def create_advertisement_route(request: Request, auth: Auth = Depends()):
    """Create advertisement."""

    await auth.check_access_token(request)

    validator = Validator(await request.json(), {
        "title": ["required", "string"],
        "user_description": ["required", "string"],
        "ad_type_id": ["required", "integer"],
        "price": ["required", "float"],
        "category_id": ["required", "integer"],
        "ad_tags": ["required", "list"],
        "ad_photos": ["required", "list"],
        "address_id": ["nullable", "integer"],
        "city_id": ["required_without:address_id", "integer"],
        "country_id": ["required_without:address_id", "integer"],
        "street": ["required_without:address_id", "string"],
        "house": ["required_without:address_id", "string"],
        "flat": ["nullable", "string"],
        "longitude": ["nullable", "float"],
        "latitude": ["nullable", "float"]
    })

    payload = validator.validated()

    try:
        if not payload["address_id"]:
            address: Address = await SqlAlchemyRepository(db_manager.get_session, Address) \
                .create(validator.only(
                ["city_id", "country_id", "street", "house", "flat", "longitude", "latitude"]))
            payload["address_id"] = address.id

        advertisement: models.Advertisement = await SqlAlchemyRepository(db_manager.get_session, models.Advertisement) \
            .create(
            validator.only(["title", "user_description", "ad_type_id", "price", "category_id"]) |
            {"user_id": request.state.user.id, "ad_status_id": AdStatus.NOT_PAID,
             "address_id": payload["address_id"]})

        if len(payload["ad_tags"]):
            tags = [{"advertisement_id": advertisement.id, "ad_tag_id": ad_tag_id} for ad_tag_id in payload["ad_tags"]]

            await SqlAlchemyRepository(db_manager.get_session, AdvertisementAdTag).bulk_create(tags)

        return ApiResponse.payload(
            transform(
                advertisement,
                AdvertisementTransformer()
                .include([
                    'address', 'user', 'ad_tags',
                    'ad_photos', 'category', 'reviews',
                ])
            )
        )
    except Exception as e:
        return ApiResponse.error(str(e))


@router.get("/{advertisement_id}")
async def get_advertisement(advertisement_id: int, request: Request, short: bool = False, auth: Auth = Depends()):
    """Get exact advertisement information. """

    await auth.check_access_token(request)
    # TODO: SHORT VERSION
    try:
        advertisement: models.Advertisement = await SqlAlchemyRepository(db_manager.get_session, models.Advertisement) \
            .get_single(id=advertisement_id)

        if not advertisement:
            raise Exception("There is no advertisement with this data.")

        return ApiResponse.payload(
            transform(
                advertisement,
                AdvertisementTransformer()
                .include([
                    'address', 'user', 'ad_tags',
                    'ad_photos', 'category', 'reviews',
                ])
            )
        )
    except Exception as e:
        return ApiResponse.error(str(e))


@router.get(path='/{advertisement_id}/reviews')
async def get_advertisement_reviews(advertisement_id: int, request: Request, auth: Auth = Depends()):
    """Get all reviews for exact advertisement. """
    await auth.check_access_token(request)
    try:
        reviews: List[models.Review] = await SqlAlchemyRepository(db_manager.get_session, models.Review) \
            .get_multi(advertisement_id=advertisement_id)

        return ApiResponse.payload(transform(
            [review for review in reviews if not review.deleted_at],
            ReviewTransformer()
        ))
    except Exception as e:
        return ApiResponse.error(str(e))


@router.get("/{advertisement_id}/worktimes")
async def get_advertisement_worktime(advertisement_id: int, request: Request, auth: Auth = Depends()):
    await auth.check_access_token(request)
    try:
        worktimes: List[models.Worktime] = await SqlAlchemyRepository(db_manager.get_session, models.Worktime) \
            .get_multi(advertisement_id=advertisement_id)

        return ApiResponse.payload(transform(
            worktimes,
            WorktimeTransformer()
        ))

    except Exception as e:
        return ApiResponse.error(str(e))


@router.get("/ad_type")
async def get_ad_types():
    try:
        ad_types: List[models.AdType] = await SqlAlchemyRepository(db_manager.get_session, models.AdType).get_multi()

        return ApiResponse.payload(transform(
            ad_types,
            AdTypeTransformer()
        ))

    except Exception as e:
        return ApiResponse.error(str(e))
