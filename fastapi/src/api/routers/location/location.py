from fastapi import APIRouter

from src.api.routers.location.address import address_router
from src.api.routers.location.city import city_router
from src.api.routers.location.country import country_router

router = APIRouter()

router.include_router(city_router)
router.include_router(country_router)
router.include_router(address_router)
