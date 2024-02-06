from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

import src.schemas.characteristics.ad_status
from src.api.dependencies.router import IsAuthenticated
from src.database.models import AdStatus
from src.database.session_manager import db_manager
from src.repository.crud.characteristics.ad_status import ad_status_repository, AdStatusRepository

router = APIRouter(
    prefix="/ad_status",
    tags=["ad_status"],
)


@router.post("/")
async def create_ad_status(ad: src.schemas.characteristics.ad_status.AdStatus):
    res = await ad_status_repository.create(ad)
    return res
