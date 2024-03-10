from typing import Optional, List
import datetime
from sqlalchemy_utils import EmailType, PhoneNumberType
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.base import Base


# TODO: ADD TO ADMIN
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)

    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)

    email: Mapped[str] = mapped_column(EmailType, nullable=False, unique=True)

    user_status_id: Mapped[int] = mapped_column(ForeignKey("user_status.id"), nullable=False)
    user_status: Mapped["UserStatus"] = relationship(uselist=False, lazy="selectin")

    phone_number: Mapped[str] = mapped_column(PhoneNumberType)  # TODO: nullable= False?, unique = True?

    avatar_id: Mapped[Optional[int]] = mapped_column(ForeignKey("avatar.id"),
                                                     nullable=True)  # TODO: default avatar? Optional?
    avatar: Mapped["Avatar"] = relationship(uselist=False, lazy="selectin")

    password: Mapped[str] = mapped_column(nullable=True)

    # TODO: GOOGLE, FACEBOOK...

    phone_verified_at: Mapped[Optional[datetime.datetime]] = mapped_column()
    email_verified_at: Mapped[Optional[datetime.datetime]] = mapped_column()

    ad_favourites: Mapped[List["AdFavourite"]] = relationship(uselist=True, lazy="selectin")

    advertisements: Mapped[List["Advertisement"]] = relationship(uselist=True, lazy="selectin")

    bookings: Mapped[List["Booking"]] = relationship(uselist=True, lazy="selectin")

    reviews: Mapped[List["Review"]] = relationship(uselist=True, lazy="selectin")

    notifications: Mapped[List["UserNotification"]] = relationship(uselist=True, lazy="selectin")

    chats_users: Mapped[List["ChatUser"]] = relationship(uselist=True, lazy="selectin")

    @property
    def chats(self):
        return [cu.chat for cu in self.chats_users]

    # TODO: RELATED MANY TO MANY
    # user_fields: Mapped[List["UserField"]] = relationship(uselist=True, lazy="selectin", secondary="user__user_field")

    created_at: Mapped[datetime.datetime] = mapped_column(nullable=False, default=datetime.datetime.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(nullable=False, default=datetime.datetime.now())
    deleted_at: Mapped[Optional[datetime.datetime]] = mapped_column(nullable=True)

    def __repr__(self) -> str:
        return (
            f"User(id={self.id}, first_name={self.first_name}, last_name={self.last_name}, email={self.email}, user_status_id={self.user_status_id})")
