import datetime
from typing import Union, ClassVar

from src.schemas.entities.base import BaseEntityTime


class Booking(BaseEntityTime):
    advertisement_id: int
    user_id: int

    time_from: datetime.datetime
    time_end: datetime.datetime

    booking_status_id: int

    guest_count: Union[int, None]

    deadline_at: datetime.datetime

# [{
#   from: 12.01.2024 12:00,
#   to: 16.01.2024 15:00
# }, { ... }]
