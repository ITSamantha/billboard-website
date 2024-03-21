from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.base import Base


class AdBooking(Base):
    __tablename__ = "advertisement__ad_booking_available"

    user_id: Mapped[int] = mapped_column(ForeignKey("advertisement.id"), nullable=False, primary_key=True)

    ad_booking_available_id: Mapped[int] = mapped_column(ForeignKey("ad_booking_available.id"), nullable=False,
                                                         primary_key=True)
