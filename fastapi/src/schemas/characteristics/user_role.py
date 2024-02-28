from src.schemas.base import BaseResponseSchema
from pydantic import BaseModel


class UserRole(BaseModel):
    pass


class UserRoleResponse(UserRole, BaseResponseSchema):
    pass


class UserRoleCreate(UserRole):
    pass


class UserRoleUpdate(UserRole):
    pass
