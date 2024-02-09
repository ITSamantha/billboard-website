import datetime
from typing import Optional

from fastapi import APIRouter

from src.api.responses.api_response import ApiResponse
from src.schemas.entities.advertisement import AdvertisementCreate
from src.repository.crud.entities.advertisement import advertisement_repository

router = APIRouter(
    prefix="/advertisement",
    tags=["advertisement"],
)


@router.post("/")
async def create_advertisement(advertisement: AdvertisementCreate):
    try:
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
