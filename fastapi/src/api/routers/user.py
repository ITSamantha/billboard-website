from typing import List

from fastapi import APIRouter, Request, Depends

from src.api.dependencies.auth import Auth
from src.api.responses.api_response import ApiResponse

from src.api.transformers.account.account_transformer import AccountTransformer
from src.api.transformers.user import UserTransformer
from src.database import models

from src.api.transformers.advertisement import AdvertisementTransformer
from src.api.transformers.booking.booking_transformer import BookingTransformer
from src.api.transformers.user import UserTransformer
from src.database import models
from src.database.models import Booking, AdFavourite, Advertisement

from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.utils.transformer import transform

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get("/me")
async def get_my(request: Request, auth: Auth = Depends()):
    await auth.check_access_token(request)
    return ApiResponse.payload(
        transform(
            request.state.user,
            UserTransformer()
        )
    )


@router.get('/me/account')
async def me_account(request: Request, auth: Auth = Depends()):
    await auth.check_access_token(request)
    account = await request.state.user.get_account()
    return ApiResponse.payload(transform(
        account,
        AccountTransformer().include(['transactions'])
    ))


@router.post('/me/account/test')
async def me_account(request: Request, auth: Auth = Depends()):
    await auth.check_access_token(request)
    account = await request.state.user.get_account()
    data = await request.json()
    type_id = data['type_id']
    amount = data['amount']
    await account.add_transaction(type_id, amount)

    return 'good'


@router.post('/me/account/testo')
async def me_account(request: Request, auth: Auth = Depends()):
    await auth.check_access_token(request)
    from src.utils.storage import storage
    from src.database.models.entities.file import File, Disk
    from src.api.transformers.file_transformer import FileTransformer
    data = await request.json()
    try:
        path, ext = storage.save_from_base64(data.image, Disk.IMAGES)
    except Exception as e:
        return ApiResponse.error(str(e))
    file = await SqlAlchemyRepository(db_manager.get_session, model=File) \
        .create({
            'path': path,
            'extension': ext,
            'disk': Disk.IMAGES,
        })

    return ApiResponse.payload(transform(file, FileTransformer()))


@router.get("/me")
async def get_my(request: Request, auth: Auth = Depends()):
    await auth.check_access_token(request)
    return ApiResponse.payload(transform(
        request.state.user,
        UserTransformer()
    ))


@router.get("/{user_id}")
async def get_user(user_id: int):
    try:
        user: models.User = await SqlAlchemyRepository(db_manager.get_session, models.User) \
            .get_single(id=user_id)

        if not user:
            raise Exception("There is no user with this data.")

        return ApiResponse.payload(
            transform(
                user,
                UserTransformer())
        )

    except Exception as e:
        return ApiResponse.error(str(e))


@router.get("/me/bookings")
async def get_my_bookings(request: Request, auth: Auth = Depends()):
    await auth.check_access_token(request)

    try:

        bookings: List[Booking] = await SqlAlchemyRepository(db_manager.get_session, Booking).get_multi(
            user_id=request.state.user.id)

        return ApiResponse.payload(transform(bookings,
                                             BookingTransformer().include(["advertisement"])
                                             ))
    except Exception as e:
        return ApiResponse.error(str(e))


@router.get("/me/favourites")
async def get_my_favourites(request: Request, auth: Auth = Depends()):
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


@router.get("/me/advertisements")
async def get_my_advertisements(request: Request, auth: Auth = Depends()):
    await auth.check_access_token(request)

    try:
        advertisements: List[Advertisement] = await SqlAlchemyRepository(db_manager.get_session,
                                                                         Advertisement) \
            .get_multi(user_id=request.state.user.id)

        return ApiResponse.payload(
            transform(
                advertisements,
                AdvertisementTransformer()
            )
        )
    except Exception as e:
        return ApiResponse.error(str(e))


@router.get("/me/reviews")
async def get_my_reviews(request: Request, auth: Auth = Depends()):
    await auth.check_access_token(request)

    try:
        advertisements: List[Advertisement] = await SqlAlchemyRepository(db_manager.get_session,
                                                                         Advertisement) \
            .get_multi(user_id=request.state.user.id)

        return ApiResponse.payload(
            transform(
                advertisements,
                AdvertisementTransformer()
            )
        )
    except Exception as e:
        return ApiResponse.error(str(e))
