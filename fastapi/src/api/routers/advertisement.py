from typing import Union, Optional

from fastapi import APIRouter, Depends, Request

from src.api.dependencies.auth import Auth
from src.api.responses.api_response import ApiResponse
from src.database import models
from src.database.models import Address, AdStatus, AdvertisementCategory, AdTag
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.schemas.entities.ad_tag import create_ad_tag, AdTagCreate
from src.schemas.entities.advertisement import AdvertisementPost, AdvertisementCreate, create_advertisement_create, \
    Advertisement, create_advertisement, validate_advertisement_post
from src.schemas.many_to_many.advertisement__ad_tag import AdvertisementAdTag
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
        "title": ['required', 'string'],
        "user_description": ['required', 'string'],
        "ad_type_id": ['required', 'integer'],
        "price": ['required', 'float'],
        "categories": ['required', 'list'],
        "ad_tags": ['required', 'list'],
        "ad_photos": ['required', 'list'],
        "address_id": ['nullable', 'integer'],
        "address": ['string', "required_without:address_id"],
        'city_id': ["nullable", 'integer'],
        'country_id': ["nullable", 'integer'],
        'street': ["nullable", 'string'],
        'house': ["nullable", 'string'],
        'flat': ["nullable", 'string'],
        'longitude': ["nullable", 'float'],
        'latitude': ["nullable", 'float'],
    }, {}, AdvertisementPost())

    payload: AdvertisementPost = validator.validated()
    try:
        if not payload.address_id:
            address: Address = await SqlAlchemyRepository(db_manager.get_session, Address) \
                .create(validator.only(
                ['address', 'city_id', 'country_id', 'street', 'house', 'flat', 'longitude', 'latitude']))

        advertisement: models.Advertisement = await SqlAlchemyRepository(db_manager.get_session, models.Advertisement) \
            .create(
            validator.only(['title', 'user_description', 'ad_type_id', 'price']) |
            {'user_id': request.state.user.id, 'ad_status_id': AdStatus.NOT_PAID,
             'address_id': payload.address_id if payload.address_id else address.id})

        if len(payload.categories):
            categories = [create_advertisement_category_create(category_id, advertisement.id) for category_id in
                          payload.categories]
            await SqlAlchemyRepository(db_manager.get_session, AdvertisementCategory).bulk_create(categories)

        if len(payload.ad_tags):
            ad_tags_repo = SqlAlchemyRepository(db_manager.get_session, AdTag)

            tags = []
            for tag in payload.ad_tags:
                ad_tag = await ad_tags_repo.get_single(title=tag)
                if not ad_tag:
                    tag_schema = AdTagCreate()
                    tag_schema.title = tag
                    ad_tag = await ad_tags_repo.create(tag_schema)
                advertisement__ad_tag = AdvertisementAdTag()
                advertisement__ad_tag.advertisement_id = advertisement.id
                advertisement__ad_tag.ad_tag_id = ad_tag.id
                tags.append(advertisement__ad_tag)

            await SqlAlchemyRepository(db_manager.get_session, models.AdvertisementAdTag).bulk_create(tags)

        return ApiResponse.payload({
            'title': advertisement.title,
            'user_description': advertisement.user_description,
            'ad_type_id': advertisement.ad_type_id,
            'price': advertisement.price,
            'user_id': advertisement.user_id,
            'ad_status_id': advertisement.ad_status_id,
            'address_id': advertisement.address_id,
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
