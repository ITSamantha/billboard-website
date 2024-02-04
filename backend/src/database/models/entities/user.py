from typing import ClassVar, Optional
import datetime

from pydantic import EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.entities.base import BaseEntityModelTime


class User(BaseEntityModelTime):
    __tablename__ = "user"

    user_name: Mapped[ClassVar[str]] = mapped_column(nullable=False)
    email: Mapped[ClassVar[EmailStr]] = mapped_column(nullable=False, unique=True)

    user_status_id: Mapped[ClassVar[int]] = mapped_column(ForeignKey('user_status.id'), nullable=False)
    phone_number: Mapped[ClassVar[PhoneNumber]] = mapped_column()  # TODO: nullable= False?, unique = True?

    avatar_id: Mapped[ClassVar[int]] = mapped_column(ForeignKey('avatar.id'))  # TODO: default avatar? Optional?

    # TODO: GOOGLE, FACEBOOK...

    phone_verified_at: Mapped[Optional[ClassVar[datetime.datetime]]] = mapped_column()
    email_verified_at: Mapped[Optional[ClassVar[datetime.datetime]]] = mapped_column()
