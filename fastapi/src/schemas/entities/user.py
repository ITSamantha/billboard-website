from typing import ClassVar, Optional
import datetime

from pydantic import EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber

from src.schemas.entities.base import BaseEntity, BaseEntityTime


class User(BaseEntityTime):
    user_name: str
    email: EmailStr

    user_status_id: int
    phone_number: PhoneNumber

    avatar_id: int  # photo_id

    # GOOGLE, FACEBOOK...

    phone_verified_at: Optional[datetime.datetime]
    email_verified_at: Optional[datetime.datetime]
