import datetime
from typing import Union, ClassVar, Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

from src.database.models.entities.base import BaseEntityModelTime
from src.schemas.entities.base import BaseEntityTime


class Booking(BaseEntityModelTime):
    __tablename__ = "booking"

    advertisement_id: Mapped[ClassVar[int]] = mapped_column(ForeignKey('advertisement.id'), nullable=False)
    user_id: Mapped[ClassVar[int]] = mapped_column(ForeignKey('user.id'), nullable=False)

    time_from: Mapped[ClassVar[datetime.datetime]] = mapped_column(nullable=False)
    time_end: Mapped[ClassVar[datetime.datetime]] = mapped_column(nullable=False)

    booking_status_id: Mapped[ClassVar[int]] = mapped_column(ForeignKey('booking_status.id'),
                                                             nullable=False)

    guest_count: Mapped[Optional[ClassVar[int]]] = mapped_column()

    deadline_at: Mapped[ClassVar[datetime.datetime]] = mapped_column(nullable=False)

    # [{
    #   from: 12.01.2024 12:00,
    #   to: 16.01.2024 15:00
    # }, { ... }]
