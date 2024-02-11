import datetime
from typing import Optional

from fastapi import APIRouter, Depends
from starlette.requests import Request

from src.api.responses.api_response import ApiResponse
from src.schemas.entities.advertisement import AdvertisementCreate, AdvertisementPost
from src.repository.crud.entities.advertisement import advertisement_repository

router = APIRouter(
    prefix="/advertisement",
    tags=["advertisement"],
)


@router.post("/")
async def create_advertisement(data: AdvertisementPost, request: Request):
    try:
        # todo: create address
        advertisement: AdvertisementCreate = AdvertisementCreate(
            title=data.title,
            user_description=data.user_description,
            address_id=data.address_id,  # todo: one to one?
            user_id=6,  # todo: get_current_user
            ad_status_id=18,
            ad_type_id=data.ad_type_id,
            price=data.price
        )
        advertisement = await advertisement_repository.create(advertisement)
    except Exception as e:
        print(e)
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
        print(e)
        return ApiResponse.error(str(e))
    return ApiResponse.payload({
        'advertisement': advertisement.title,
        'short': short,
    })
