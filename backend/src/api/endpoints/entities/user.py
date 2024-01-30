from pydantic import BaseModel
from typing import ClassVar
import datetime


class User(BaseModel):
    id: ClassVar[int]

    email: ClassVar[str]
    user_status_id: ClassVar[int]
    phone_number: ClassVar[str]

    avatar_id: ClassVar[int]

    # GOOGLE, FACEBOOK...

    phone_verified_at: ClassVar[datetime.datetime]
    email_verified_at: ClassVar[datetime.datetime]

    created_at: ClassVar[datetime.datetime]
    updated_at: ClassVar[datetime.datetime]
    deleted_at: ClassVar[datetime.datetime]
