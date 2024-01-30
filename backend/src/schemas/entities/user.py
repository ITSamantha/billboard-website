from typing import ClassVar
import datetime

from pydantic import EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber

from src.schemas.entities.base import BaseEntity


class User(BaseEntity):
    user_name: ClassVar[str]
    email: ClassVar[EmailStr]

    user_status_id: ClassVar[int]
    phone_number: ClassVar[PhoneNumber]

    avatar_id: ClassVar[int]  # photo_id

    # GOOGLE, FACEBOOK...

    phone_verified_at: ClassVar[datetime.datetime]
    email_verified_at: ClassVar[datetime.datetime]

    created_at: ClassVar[datetime.datetime]
    updated_at: ClassVar[datetime.datetime]
    deleted_at: ClassVar[datetime.datetime]
