from typing import Union, Optional

from fastapi import APIRouter, Depends, Request

from src.api.dependencies.auth import Auth
from src.api.responses.api_response import ApiResponse
from src.database import models
from src.database.models import Address, AdStatus, AdvertisementCategory, AdTag, AdvertisementAdTag
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.schemas.entities.ad_tag import AdTagCreate
from src.schemas.entities.advertisement import Advertisement, create_advertisement
from src.schemas.many_to_many.advertisement__category import create_advertisement_category_create
from src.utils.validator import Validator

router = APIRouter(
    prefix="/advertisements",
    tags=["advertisements"],
)


@router.post("", response_model=Union[Advertisement, ApiResponse])
async def create_advertisement_route(request: Request, auth: Auth = Depends()):
    """Create advertisement."""

    await auth.check_access_token(request)

    validator = Validator(await request.json(), {
        "title": ["required", "string"],
        "user_description": ["required", "string"],
        "ad_type_id": ["required", "integer"],
        "price": ["required", "float"],
        "categories": ["required", "list"],
        "ad_tags": ["required", "list"],
        "ad_photos": ["required", "list"],
        "address_id": ["nullable", "integer"],
        "address": ["string", "required_without:address_id"],
        "city_id": ["nullable", "integer"],
        "country_id": ["nullable", "integer"],
        "street": ["nullable", "string"],
        "house": ["nullable", "string"],
        "flat": ["nullable", "string"],
        "longitude": ["nullable", "float"],
        "latitude": ["nullable", "float"],
    })

    payload = validator.validated()

    try:
        if not payload["address_id"]:
            address: Address = await SqlAlchemyRepository(db_manager.get_session, Address) \
                .create(payload.only(
                ["address", "city_id", "country_id", "street", "house", "flat", "longitude", "latitude"]))
            payload.address_id = address.id

        advertisement: models.Advertisement = await SqlAlchemyRepository(db_manager.get_session, models.Advertisement) \
            .create(
            payload.only(["title", "user_description", "ad_type_id", "price"]) |
            {"user_id": request.state.user.id, "ad_status_id": AdStatus.NOT_PAID,
             "address_id": payload.address_id})

        if len(payload["categories"]):
            categories = [{"category_id": category_id, "advertisement_id": advertisement.id} for category_id in
                          payload["categories"]]
            await SqlAlchemyRepository(db_manager.get_session, AdvertisementCategory).bulk_create(categories)

        if len(payload["ad_tags"]):
            tags = [{"advertisement_id": advertisement.id, "ad_tag_id": ad_tag_id} for ad_tag_id in payload["ad_tags"]]

            await SqlAlchemyRepository(db_manager.get_session, AdvertisementAdTag).bulk_create(tags)

        return ApiResponse.payload({
            "title": advertisement.title,
            "user_description": advertisement.user_description,
            "ad_type_id": advertisement.ad_type_id,
            "price": advertisement.price,
            "user_id": advertisement.user_id,
            "ad_status_id": advertisement.ad_status_id,
            "address_id": advertisement.address_id,
        })
    except Exception as e:
        return ApiResponse.error(e.with_traceback())


@router.get("/advertisement/{advertisement_id}", response_model=Union[Advertisement, ApiResponse])
async def get_advertisement(advertisement_id: int, short: bool = False):
    """Get exact advertisement information. """

    try:
        ad: models.Advertisement = await SqlAlchemyRepository(db_manager.get_session,
                                                              models.Advertisement).get_single(id=advertisement_id)
        if ad.deleted_at:
            raise Exception("This advertisement has been deleted.")
        result: Optional[Advertisement] = create_advertisement(ad)
        return result
    except Exception as e:
        return ApiResponse.error(str(e))
