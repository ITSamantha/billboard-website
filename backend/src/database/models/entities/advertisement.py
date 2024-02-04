from typing import ClassVar, Optional, List

from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.entities.base import BaseEntityModelTime


class Advertisement(BaseEntityModelTime):
    __tablename__ = "advertisement"

    title: Mapped[ClassVar[str]] = mapped_column(String(128), nullable=False)
    user_description: Mapped[ClassVar[str]] = mapped_column(Text, nullable=False)

    address_id: Mapped[Optional[ClassVar[int]]] = mapped_column(ForeignKey("address.id"))
    address: Mapped["Address"] = relationship(back_populates="advertisement", uselist=False)

    user_id: Mapped[ClassVar[int]] = mapped_column(ForeignKey("user.id"), nullable=False)
    user: Mapped["User"] = relationship(back_populates="advertisements", uselist=False)

    ad_status_id: Mapped[ClassVar[int]] = mapped_column(ForeignKey("ad_status.id"),
                                                        nullable=False)
    ad_status: Mapped["AdStatus"] = relationship(back_populates="advertisements", uselist=False)

    ad_type_id: Mapped[ClassVar[int]] = mapped_column(ForeignKey("ad_type.id"),
                                                      nullable=False)  # booking, sell
    ad_type: Mapped["AdType"] = relationship(back_populates="advertisements", uselist=False)

    price: Mapped[Optional[ClassVar[float]]] = mapped_column(nullable=False)

    ad_bookings_available: Mapped[List["AdBookingAvailable"]] = relationship(back_populates="advertisement",
                                                                             uselist=True)
    ad_favourites: Mapped[List["AdFavourite"]] = relationship(back_populates="advertisement",
                                                              uselist=True)

    ad_photos: Mapped[List["AdPhoto"]] = relationship(back_populates="advertisement", uselist=True)

    ad_priorities: Mapped[List["AdPriority"]] = relationship(back_populates="advertisement", uselist=True)

    ad_tags: Mapped[List["AdTag"]] = relationship(back_populates="advertisements",
                                                  uselist=True, secondary="advertisement__ad_tag")
    bookings: Mapped[List["Booking"]] = relationship(back_populates="advertisement", uselist=True)

    categories: Mapped[List["Category"]] = relationship(back_populates="advertisements",
                                                        uselist=True, secondary="advertisement__category")
    reviews: Mapped[List["Review"]] = relationship(back_populates="advertisement", uselist=True)

    views: Mapped[List["View"]] = relationship(back_populates="advertisement", uselist=True)

    worktimes: Mapped[List["Worktime"]] = relationship(back_populates="advertisement", uselist=True)

    filter_values: Mapped[List["FilterValue"]] = relationship(back_populates="advertisements",
                                                              uselist=True, secondary="advertisement__filter_value")

    def __repr__(self) -> str:
        return (f"Advertisement(id={self.id}, title={self.title}, user_description={self.user_description},"
                f"address_id={self.address_id}, user_id={self.user_id}, ad_status_id={self.ad_status_id},"
                f"ad_type_id={self.ad_type_id}, price={self.price})")
