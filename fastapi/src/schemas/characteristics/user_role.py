from src.api.payloads.base import BasePayload
from src.database import models
from pydantic import BaseModel


class UserRole(BaseModel):
    id: int
    title: str


def create_user_role(type: models.UserRole) -> UserRole:
    return UserRole(id=type.id, title=type.title)


class UserRoleCreate(BasePayload):
    title: str


class UserRoleUpdate(BasePayload):
    title: str
