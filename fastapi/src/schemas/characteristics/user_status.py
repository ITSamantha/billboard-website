from typing import Optional
from src.api.payloads.base import BasePayload
from pydantic import BaseModel


class UserStatus(BaseModel):
    id: int
    title: str
    is_available: bool


def create_user_status(status):
    return UserStatus(id=status.id, title=status.title, is_available=status.is_available)


class UserStatusCreate(BasePayload):
    title: str
    is_available: bool


class UserStatusUpdate(BasePayload):
    title: Optional[str] = None
    is_available: Optional[bool] = None
