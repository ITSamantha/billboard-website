from fastapi import APIRouter, Depends
from src.api.dependencies.router import IsAuthenticated
from src.repository.crud.characteristics.ad_status import ad_status_repository

router = APIRouter(
    prefix="/ad_status",
    tags=["ad_status"],
)


@router.post()
def create_ad_status():
    ad_status_repository.create()
