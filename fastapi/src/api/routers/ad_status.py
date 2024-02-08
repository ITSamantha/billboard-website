from fastapi import APIRouter

import src.schemas.characteristics.ad_status
from src.repository.crud.characteristics.ad_status import ad_status_repository, AdStatusRepository
from src.schemas.characteristics.ad_status import AdStatusCreate

router = APIRouter(
    prefix="/ad_status",
    tags=["ad_status"],
)


@router.post("/")
async def create_ad_status(ad_status: AdStatusCreate):
    res = await ad_status_repository.create(ad_status)
    return res


@router.get("/{id}")
async def create_ad_status(id: int):
    res = await ad_status_repository.get_single(id=id)
    return res
