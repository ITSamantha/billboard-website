from typing import List

from fastapi import APIRouter, Request, Depends

from src.api.dependencies.auth import Auth
from src.api.responses.api_response import ApiResponse
from src.api.transformers.advertisement import AdvertisementTransformer
from src.database.models import AdFavourite
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.utils.transformer import transform
from src.utils.validator import Validator

router = APIRouter(
    prefix="/favourites",
)


@router.get("")
async def get_favourites(request: Request, auth: Auth = Depends()):
    await auth.check_access_token(request)

    try:
        advertisements: List[AdFavourite] = await SqlAlchemyRepository(db_manager.get_session,
                                                                       AdFavourite) \
            .get_multi(user_id=request.state.user.id)

        return ApiResponse.payload(
            transform(
                [ad.advertisement for ad in advertisements],
                AdvertisementTransformer()
            )
        )
    except Exception as e:
        return ApiResponse.error(str(e))


@router.post("")
async def create_favourite(request: Request, auth: Auth = Depends()):
    """Add favourite advertisement. """

    await auth.check_access_token(request)

    validator = Validator(await request.json(), {
        'advertisement_id': ['required', 'integer']
    })

    validator.validated()

    try:

        ad_fav: AdFavourite = await SqlAlchemyRepository(db_manager.get_session, AdFavourite) \
            .create(validator.all() | {"user_id": request.state.user.id})

        return ApiResponse.payload(transform(ad_fav.advertisement, AdvertisementTransformer()))
    except Exception as e:
        return ApiResponse.error(str(e))


@router.delete("/{advertisement_id}")
async def delete_favourite(advertisement_id: int, request: Request, auth: Auth = Depends()):
    """Delete favourite advertisement by id. """

    await auth.check_access_token(request)

    try:
        await SqlAlchemyRepository(db_manager.get_session, AdFavourite) \
            .delete(advertisement_id=advertisement_id, user_id=request.state.user.id)

        return ApiResponse.payload({"advertisement_id": advertisement_id})
    except Exception as e:
        return ApiResponse.error(str(e))
