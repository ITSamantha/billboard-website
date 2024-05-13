import datetime
from typing import Optional, List
from fastapi import Request

from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models import AdPhoto
from src.database.models.base import Base


# TODO: ADD TO ADMIN, VIEW
class Advertisement(Base):
    __tablename__ = "advertisement"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)

    title: Mapped[str] = mapped_column(String(128), nullable=False)
    user_description: Mapped[str] = mapped_column(Text, nullable=False)

    address_id: Mapped[Optional[int]] = mapped_column(ForeignKey("address.id"))
    address: Mapped["Address"] = relationship(uselist=False, lazy="selectin")

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    user: Mapped["User"] = relationship(uselist=False, lazy="selectin")

    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"), nullable=False)
    category: Mapped["Category"] = relationship(uselist=False, lazy="selectin")

    ad_status_id: Mapped[int] = mapped_column(ForeignKey("ad_status.id"),
                                              nullable=False)
    ad_status: Mapped["AdStatus"] = relationship(uselist=False, lazy="selectin")

    ad_type_id: Mapped[int] = mapped_column(ForeignKey("ad_type.id"),
                                            nullable=False)  # booking, sell
    ad_type: Mapped["AdType"] = relationship(uselist=False, lazy="selectin")

    price: Mapped[Optional[float]] = mapped_column(nullable=False)

    auto_booking: Mapped[bool] = mapped_column(nullable=False, default=True)

    ad_bookings_available: Mapped[List["AdBookingAvailable"]] = relationship(uselist=True, lazy="selectin")

    # ad_favourites: Mapped[List["AdFavourite"]] = relationship(uselist=True, lazy="selectin")

    # ad_photos: Mapped[List["AdPhoto"]] = relationship(uselist=True, lazy="selectin")
    ad_photos: Mapped[List["File"]] = relationship('File', secondary='ad_photo', foreign_keys=[AdPhoto.advertisement_id], uselist=True, lazy="selectin")

    ad_priorities: Mapped[List["AdPriority"]] = relationship(uselist=True,
                                                             lazy="selectin")

    ad_tags: Mapped[List["AdTag"]] = relationship(
        uselist=True, lazy="selectin", secondary="advertisement__ad_tag")

    bookings: Mapped[List["Booking"]] = relationship(uselist=True, lazy="selectin")

    reviews: Mapped[List["Review"]] = relationship(uselist=True, lazy="selectin")

    views: Mapped[List["View"]] = relationship(uselist=True, lazy="selectin")

    worktimes: Mapped[List["Worktime"]] = relationship(uselist=True, lazy="selectin")

    filter_values: Mapped[List["FilterValue"]] = relationship(
        uselist=True, lazy="selectin",
        secondary="advertisement__filter_value")

    created_at: Mapped[datetime.datetime] = mapped_column(nullable=False, default=datetime.datetime.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(nullable=False, default=datetime.datetime.now())
    deleted_at: Mapped[Optional[datetime.datetime]] = mapped_column(nullable=True)

    def __repr__(self) -> str:
        return (f"Advertisement(id={self.id}, title={self.title}, user_description={self.user_description},"
                f"address_id={self.address_id}, user_id={self.user_id}, ad_status_id={self.ad_status_id},"
                f"ad_type_id={self.ad_type_id}, price={self.price})")
