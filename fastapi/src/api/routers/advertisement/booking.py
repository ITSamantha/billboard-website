from fastapi import APIRouter, Request, Depends

from src.api.dependencies.auth import Auth
from src.api.responses.api_response import ApiResponse
from src.database.models import Booking
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.utils.validator import Validator

router = APIRouter(
    prefix="/booking"
)

"""
@router.post("/{advertisement_id}")
async def create_advertisement_booking(advertisement_id: int, request: Request, auth: Auth = Depends()):
    await auth.check_access_token(request)

    validator = Validator(await request.json(), {
        'ad_booking_available_id': ['required', 'integer']
    })

    validator.validated()

    try:
        ad_booking: Booking = await SqlAlchemyRepository(db_manager.get_session,
                                                         Booking) \
            .create(validator.all() | {"user_id": request.state.user.id})

        # CHECK TYPE
        # DELETE FROM AD_BOOKING_AVAILABLE
        # TODO: ABLE TO RESTORE IF BOOKING IS CANCELLED

        return ApiResponse.payload(
            {"ad_booking_available_id": ad_booking.id}
        )
    except Exception as e:
        return ApiResponse.error(str(e))
"""
