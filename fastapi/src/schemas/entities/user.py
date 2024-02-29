from typing import Optional, List
import datetime

from pydantic import EmailStr, BaseModel
from pydantic_extra_types.phone_numbers import PhoneNumber

from src.database import models
from src.schemas import UserStatus, Avatar, create_user_status, create_avatar, UserField


class User(BaseModel):
    id: int
    first_name: str
    last_name: str

    email: EmailStr

    # user_status_id: int
    user_status: UserStatus
    phone_number: PhoneNumber

    # avatar_id: int  # photo_id
    avatar: Avatar

    # user_fields: List[UserField]

    # GOOGLE, FACEBOOK...

    phone_verified_at: Optional[datetime.datetime] = None
    email_verified_at: Optional[datetime.datetime] = None

    created_at: Optional[datetime.datetime] = None
    updated_at: Optional[datetime.datetime] = None
    deleted_at: Optional[datetime.datetime] = None


def create_user(user: models.User) -> User:
    return User(id=user.id,
                first_name=user.first_name,
                last_name=user.last_name,
                email=user.email,
                user_status=create_user_status(user.user_status) if user.user_status else None,
                phone_number=user.phone_number,
                avatar=create_avatar(user.avatar) if user.avatar else None,
                phone_verified_at=user.phone_verified_at,
                email_verified_at=user.email_verified_at,
                created_at=user.created_at,
                updated_at=user.updated_at,
                # user_fields
                deleted_at=user.deleted_at
                )


class UserShort(BaseModel):
    id: int
    first_name: str
    last_name: str
    user_status: UserStatus


def create_user_short(user):
    return UserShort(id=user.id,
                     first_name=user.first_name,
                     last_name=user.last_name,
                     user_status=create_user_status(user.user_status) if user.user_status else None)
