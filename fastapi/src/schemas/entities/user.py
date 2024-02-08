from typing import Optional
import datetime

from pydantic import EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber

from src.schemas.entities.base import BaseEntityTime
from src.schemas import BaseResponseSchema


class User(BaseEntityTime):
    first_name: str
    last_name: str

    email: EmailStr

    user_status_id: int
    phone_number: PhoneNumber

    avatar_id: int  # photo_id

    # GOOGLE, FACEBOOK...

    phone_verified_at: Optional[datetime.datetime]
    email_verified_at: Optional[datetime.datetime]


class UserResponse(User, BaseResponseSchema):
    pass


class UserCreate(User):
    pass


class UserUpdate(User):
    pass
