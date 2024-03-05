from typing import Union, Optional

from fastapi import APIRouter, Depends, Request

from src.api.dependencies.auth import Auth
from src.api.responses.api_response import ApiResponse
from src.database import models
from src.database.models import Address, AdStatus, AdvertisementCategory, AdTag
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.schemas.entities import validate_address_create
from src.schemas.entities.ad_tag import create_ad_tag, AdTagCreate
from src.schemas.entities.advertisement import AdvertisementPost, AdvertisementCreate, create_advertisement_create, \
    Advertisement, create_advertisement, validate_advertisement_post
from src.schemas.many_to_many.advertisement__ad_tag import AdvertisementAdTag
from src.schemas.many_to_many.advertisement__category import create_advertisement_category_create

router = APIRouter(
    prefix="/advertisements",
    tags=["advertisements"],
)


@router.post("/", response_model=Union[Advertisement, ApiResponse])
async def create_advertisement_route(request: Request, auth: Auth = Depends()):
    """Create advertisement."""

    await auth.check_access_token(request)

    payload: AdvertisementPost = validate_advertisement_post(await request.json())

    try:

        if not payload.address_id:
            address = validate_address_create(payload.address)

            address_db: Address = await SqlAlchemyRepository(db_manager.get_session,
                                                             Address).create(address)
            payload.address_id = address_db.id

        advertisement: AdvertisementCreate = create_advertisement_create(payload)

        advertisement.user_id = request.state.user.id
        advertisement.ad_status_id = AdStatus.NOT_PAID

        ad: models.Advertisement = await SqlAlchemyRepository(db_manager.get_session, models.Advertisement).create(
            advertisement)

        ad: Advertisement = create_advertisement(ad)

        advertisement_id = ad.id

        if len(payload.categories):
            categories = [create_advertisement_category_create(category_id, advertisement_id) for category_id in
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
                advertisement__ad_tag.advertisement_id = advertisement_id
                advertisement__ad_tag.ad_tag_id = ad_tag.id
                tags.append(advertisement__ad_tag)

            await SqlAlchemyRepository(db_manager.get_session, models.AdvertisementAdTag).bulk_create(tags)

        return ad
    except Exception as e:
        return ApiResponse.error(str(e))


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
