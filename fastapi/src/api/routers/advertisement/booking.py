import datetime

from fastapi import APIRouter, Request, Depends

from src.api.dependencies.auth import Auth
from src.api.responses.api_response import ApiResponse
from src.api.transformers.booking.booking_transformer import BookingTransformer
from src.database.models import Booking, BookingStatus
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.utils.transformer import transform
from src.utils.validator import Validator

router = APIRouter(
    prefix="/booking"
)


@router.post("")
async def create_advertisement_booking(request: Request, auth: Auth = Depends()):
    await auth.check_access_token(request)

    validator = Validator(await request.json(), {
        'advertisement_id': ['required', 'integer'],
        'time_from': ['required', 'string'],
        'time_end': ['required', 'string'],
        # 'time_from': ['required', 'datetime'],
        # 'time_end': ['required', 'datetime'],
        # 'deadline_at': ['required', 'datetime']
        'deadline_at': ['required', 'string'],
        'guest_count': ['required', 'integer']
    })

    validator.validated()

    validator.validated_data["time_from"] = datetime.datetime.strptime(validator.validated_data["time_from"],
                                                                       '%Y-%m-%d %H:%M:%S')

    validator.validated_data["time_end"] = datetime.datetime.strptime(validator.validated_data["time_end"],
                                                                      '%Y-%m-%d %H:%M:%S')

    validator.validated_data["deadline_at"] = datetime.datetime.strptime(validator.validated_data["deadline_at"],
                                                                         '%Y-%m-%d %H:%M:%S')

    try:
        booking: Booking = await SqlAlchemyRepository(db_manager.get_session,
                                                      Booking) \
            .create(validator.all() | {"user_id": request.state.user.id, "booking_status_id": BookingStatus.NOT_PAID})

        # CHECK TYPE
        # DELETE FROM AD_BOOKING_AVAILABLE
        # TODO: ABLE TO RESTORE IF BOOKING IS CANCELLED
        # TODO: CALCULATE AVAILABLE DATES

        return ApiResponse.payload(
            transform(booking,
                      BookingTransformer()
                      )
        )
    except Exception as e:
        return ApiResponse.error(str(e))
