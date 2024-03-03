from typing import Union

from fastapi import APIRouter, Depends, Request

from src.api.dependencies.auth import Auth
from src.api.responses.api_response import ApiResponse
from src.database import models
from src.database.models import Address, AdStatus
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.schemas.entities import create_address_create, AddressCreate
from src.schemas.entities.advertisement import AdvertisementPost, AdvertisementCreate, create_advertisement_create, \
    Advertisement, create_advertisement
from src.utils.validator import Validator
from src.utils.validator.validator import Rules

router = APIRouter(
    prefix="/advertisements",
    tags=["advertisements"],
)


@router.post("/advertisement", response_model=Union[Advertisement, ApiResponse])
async def create_advertisement_route(request: Request, auth: Auth = Depends()):
    await auth.check_access_token(request)

    validator = Validator(await request.json(), {
        'title': [Rules.REQUIRED, Rules.STRING],
        'user_description': [Rules.REQUIRED, Rules.STRING],
        'address_id': [Rules.NULLABLE, Rules.INTEGER, f'{Rules.FIELDS_OR}address_id,address'],
        'address': [Rules.NULLABLE, f'{Rules.FIELDS_OR}address_id,address'],
        'ad_type_id': [Rules.REQUIRED, Rules.INTEGER],
        "price": [Rules.REQUIRED, Rules.FLOAT],
        "categories": [Rules.REQUIRED, Rules.LIST],
        "ad_tags": [Rules.NULLABLE, Rules.LIST],
        "ad_photos": [Rules.NULLABLE, Rules.LIST],
        "filters": [Rules.NULLABLE]
    }, {}, AdvertisementPost())

    payload: AdvertisementPost = validator.validated()

    if not payload.address_id:
        validator = Validator(payload.address, {
            'address': [Rules.REQUIRED, Rules.STRING],
            'city_id': [Rules.INTEGER],
            'country_id': [Rules.INTEGER],
            'street': [Rules.STRING],
            'house': [Rules.STRING],
            'flat': [Rules.STRING],
            'longitude': [Rules.FLOAT],
            'latitude': [Rules.FLOAT]
        }, {}, AddressCreate())

        address: AddressCreate = validator.validated()

        address_db: Address = await SqlAlchemyRepository(db_manager.get_session,
                                                         Address).create(address)
        payload.address_id = address_db.id

    advertisement: AdvertisementCreate = create_advertisement_create(payload)

    advertisement.user_id = request.state.user.id
    advertisement.ad_status_id = AdStatus.NOT_PAID

    try:

        ad: models.Advertisement = await SqlAlchemyRepository(db_manager.get_session, models.Advertisement).create(
            advertisement)

        result: Advertisement = create_advertisement(ad)
        return result
    except Exception as e:
        return ApiResponse.error(str(e))


"""
@router.post("/")
async def create_advertisement(request: Request,
                               auth: Auth = Depends()):
    await auth.check_access_token(request)

    validator = Validator(await request.json(), {
        'title': [Rules.REQUIRED, Rules.STRING],
        'user_description': [Rules.REQUIRED, Rules.STRING],
        'address_id': [Rules.NULLABLE, Rules.INTEGER, f'{Rules.FIELDS_OR}address_id,address'],
        'address': [Rules.NULLABLE, f'{Rules.FIELDS_OR}address_id,address'],
        'ad_type_id': [Rules.REQUIRED, Rules.INTEGER],
        "price": [Rules.REQUIRED, Rules.FLOAT],
        "categories": [Rules.REQUIRED, Rules.LIST],
        "filters": [Rules.NULLABLE]
    }, {}, AdvertisementPost())

    payload: AdvertisementPost = validator.validated()

    if not payload.address_id:
        # address_db: Address = await address_repository.create(payload.address)
        # payload.address_id = address_db.id
        pass

    advertisement: AdvertisementCreate = AdvertisementCreate()
    advertisement.title = payload.title
    advertisement.user_description = payload.user_description
    advertisement.price = payload.price
    advertisement.ad_type_id = payload.ad_type_id
    advertisement.ad_status_id = AdStatus.NOT_PAID
    advertisement.user_id = request.state.user.id
    advertisement.address_id = payload.address_id

    db_advertisement: Advertisement = await SqlAlchemyRepository(db_manager.get_session, Advertisement).create(
        advertisement)

    if payload.categories:
        objects = []
        for category_id in payload.categories:
            ad_category = AdvertisementCategoryCreate()
            ad_category.category_id = category_id
            ad_category.advertisement_id = db_advertisement.id
            objects.append(ad_category)
        await  SqlAlchemyRepository(db_manager.get_session, AdvertisementCategory).bulk_create(objects)

    if payload.filters:
        pass

    return ApiResponse.payload({
        'id': db_advertisement.id
    })




@router.get("/{advertisement_id}")
async def get_advertisement(advertisement_id: int, short: Optional[bool] = None):
    try:
        advertisement: Advertisement = await advertisement_repository.get_single(id=advertisement_id)
        if not advertisement:
            raise Exception(f'Advertisement with id={advertisement_id} not found.')
    except Exception as e:
        return ApiResponse.error(str(e))
    return ApiResponse.payload({
        'advertisement': advertisement.title,
        'short': short,
    })
"""
