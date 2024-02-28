from pydantic import BaseModel

from src.schemas.base import BaseResponseSchema
from pydantic import BaseModel


class UserStatus(BaseModel):
    id: int
    title: str
    is_available: bool


def create_user_status(status):
    return UserStatus(id=status.id, title=status.title, is_available=status.is_available)


class UserStatusResponse(UserStatus, BaseResponseSchema):
    pass


class UserStatusCreate(UserStatus):
    pass


class UserStatusUpdate(UserStatus):
    pass
