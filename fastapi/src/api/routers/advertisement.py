from fastapi import Request, Depends
from typing import Optional

from fastapi import APIRouter

from src.api.dependencies.auth import Auth
from src.api.responses.api_response import ApiResponse
from src.repository.crud.entities.address import address_repository
from src.repository.crud.many_to_many.advertisement__category import advertisement_category_repository
from src.repository.crud.many_to_many.advertisement__filter_value import advertisement_filter_value_repository
from src.schemas import FilterValueCreate
from src.schemas.entities.advertisement import AdvertisementCreate, AdvertisementPost
from src.repository.crud.entities.advertisement import advertisement_repository
from src.schemas.many_to_many.advertisement__category import AdvertisementCategoryCreate

router = APIRouter(
    prefix="/advertisement",
    tags=["advertisement"],
)


@router.post("/")
async def create_advertisement(data: AdvertisementPost, request: Request, auth: Auth = Depends()):
    try:
        await auth.check_access_token(request)

        if not data.address and not data.address_id:
            raise Exception('Neither address nor address_id was specified.')

        if data.address:
            address = await address_repository.create(data.address)

        advertisement: AdvertisementCreate = AdvertisementCreate(
            title=data.title,
            user_description=data.user_description,
            address_id=data.address_id if data.address_id else address.id,
            user_id=request.state.user.id,
            ad_status_id=18,
            ad_type_id=data.ad_type_id,
            price=data.price
        )

        advertisement = await advertisement_repository.create(advertisement)

        if data.categories:
            objects = [AdvertisementCategoryCreate(category_id=category_id, advertisement_id=advertisement.id) for
                       category_id in data.categories]
            await advertisement_category_repository.bulk_create(objects)

        """if data.filters:
            objects = [FilterValueCreate(filter_id=filter_id,  value=) for filter_id, value in data.filters.items()]
            await advertisement_filter_value_repository.bulk_create(objects)"""

    except Exception as e:
        return ApiResponse.error(str(e))
    return ApiResponse.payload({
        'id': advertisement.id,
        'title': advertisement.title,
    })


@router.get("/{advertisement_id}")
async def get_advertisement(advertisement_id: int, short: Optional[bool] = None):
    try:
        advertisement = await advertisement_repository.get_single(id=advertisement_id)
    except Exception as e:
        return ApiResponse.error(str(e))
    return ApiResponse.payload({
        'advertisement': advertisement.title,
        'short': short,
    })
