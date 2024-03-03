import datetime
from typing import Optional

from pydantic import BaseModel

from src.api.payloads.base import BasePayload
from src.database import models
from src.schemas.characteristics import BookingStatus, create_booking_status
from src.schemas.entities.advertisement import Advertisement, create_advertisement
from src.schemas.entities.user import User, create_user


#   TODO:
# [{
#   from: 12.01.2024 12:00,
#   to: 16.01.2024 15:00
# }, { ... }]


class Booking(BaseModel):
    id: int

    # advertisement_id: int
    advertisement: Advertisement
    # user_id: int
    user: User

    time_from: datetime.datetime
    time_end: datetime.datetime

    # booking_status_id: int
    booking_status: BookingStatus

    guest_count: Optional[int]

    deadline_at: datetime.datetime

    created_at: Optional[datetime.datetime] = None
    updated_at: Optional[datetime.datetime] = None
    deleted_at: Optional[datetime.datetime] = None


def create_booking(booking: models.Booking) -> Booking:
    return Booking(id=booking.id,
                   advertisement=create_advertisement(booking.advertisement) if booking.advertisement else None,
                   user=create_user(booking.user) if booking.user else None,
                   time_from=booking.time_from,
                   time_end=booking.time_end,
                   booking_status=create_booking_status(booking.booking_status) if booking.booking_status else None,
                   guest_count=booking.guest_count,
                   deadline_at=booking.deadline_at,
                   created_at=booking.created_at,
                   updated_at=booking.updated_at,
                   deleted_at=booking.deleted_at
                   )


class BookingCreate(BasePayload):
    advertisement_id: int
    user_id: Optional[int] = None

    time_from: datetime.datetime
    time_end: datetime.datetime

    booking_status_id: Optional[int] = None

    guest_count: Optional[int] = None

    deadline_at: datetime.datetime

    created_at: Optional[datetime.datetime] = None
    updated_at: Optional[datetime.datetime] = None
    deleted_at: Optional[datetime.datetime] = None
