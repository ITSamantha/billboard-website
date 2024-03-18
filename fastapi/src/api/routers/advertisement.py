from typing import Union, Optional

from fastapi import APIRouter, Depends, Request

from src.api.dependencies.auth import Auth
from src.api.responses.api_response import ApiResponse
from src.database import models
from src.database.models import Address, AdStatus, AdvertisementAdTag
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.utils.transformers.entities import transform_advertisement
from src.utils.validator import Validator

router = APIRouter(
    prefix="/advertisements",
    tags=["advertisements"],
)


@router.post("", response_model=ApiResponse)
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

        return ApiResponse.payload(transform_advertisement(advertisement))
    except Exception as e:
        return ApiResponse.error(str(e))
        # return ApiResponse.error(e.with_traceback())


@router.get("/{advertisement_id}", response_model=ApiResponse)
async def get_advertisement(advertisement_id: int, short: bool = False):
    """Get exact advertisement information. """
    # TODO: SHORT VERSION
    try:
        advertisement: models.Advertisement = await SqlAlchemyRepository(db_manager.get_session,
                                                                         models.Advertisement).get_single(
            id=advertisement_id)

        if not advertisement:
            raise Exception("There is no advertisement with this data.")

        return ApiResponse.payload(transform_advertisement(advertisement))
    except Exception as e:
        return ApiResponse.error(str(e))


@router.get("/at_type", response_model=ApiResponse)
async def get_advertisement():
    """Get exact ad_types information. """
    try:
        ad_types: models.AdType = await SqlAlchemyRepository(db_manager.get_session,
                                                             models.AdType).get_multi()

        return ApiResponse.payload(transform_ad_type(ad_types))
    except Exception as e:
        return ApiResponse.error(str(e))
