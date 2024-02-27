from typing import Optional
import datetime

from pydantic import EmailStr, BaseModel
from pydantic_extra_types.phone_numbers import PhoneNumber

from src.database import models
from src.schemas.entities.base import BaseEntityTime, BaseEntity
from src.schemas import BaseResponseSchema, Avatar, UserStatus, create_user_status


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


class UserShortResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    user_status: UserStatus


def create_user_short_response(user):
    return UserShortResponse(id=user.id, first_name=user.first_name, last_name=user.last_name,
                             user_status=create_user_status(user.user_status))


class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr


class UserShort(BaseModel):
    first_name: str
    last_name: str
    avatar: Optional[Avatar]  # todo: remove optional


class UserCreate(User):
    pass


class UserUpdate(User):
    pass


def create_user_short(user: User):
    user = UserShort(
        id=user.id,
        first_name=user.first_name,
        last_name=user.last_name,
        avatar=user.avatar,
    )
    return user
