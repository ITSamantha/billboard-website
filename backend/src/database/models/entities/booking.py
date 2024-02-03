import datetime
from typing import Union, ClassVar

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

from src.database.models.entities.base import BaseEntityModelTime
from src.schemas.entities.base import BaseEntityTime


class Booking(BaseEntityModelTime):
    advertisement_id: Mapped[ClassVar[int]] = mapped_column(ForeignKey('advertisement.id'), nullable=False)
    user_id: ClassVar[int]

    time_from: ClassVar[datetime.datetime]
    time_end: ClassVar[datetime.datetime]

    booking_status_id: ClassVar[int]

    guest_count: Union[ClassVar[int], None]

    deadline_at: ClassVar[datetime.datetime]

# [{
#   from: 12.01.2024 12:00,
#   to: 16.01.2024 15:00
# }, { ... }]
