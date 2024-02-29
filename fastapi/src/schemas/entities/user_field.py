

from pydantic import BaseModel


class UserField(BaseModel):
    type: str
    title: str

    order: int


class UserFieldResponse(UserField, BaseResponseSchema):
    pass


class UserFieldCreate(UserField):
    pass


class UserFieldUpdate(UserField):
    pass
