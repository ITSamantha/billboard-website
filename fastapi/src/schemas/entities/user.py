from typing import ClassVar, Optional
import datetime

from pydantic import EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber

from src.schemas.entities.base import BaseEntity, BaseEntityTime


class User(BaseEntityTime):
    user_name: ClassVar[str]
    email: ClassVar[EmailStr]

    user_status_id: ClassVar[int]
    phone_number: ClassVar[PhoneNumber]

    avatar_id: ClassVar[int]  # photo_id

    # GOOGLE, FACEBOOK...

    phone_verified_at: Optional[ClassVar[datetime.datetime]]
    email_verified_at: Optional[ClassVar[datetime.datetime]]
