from pydantic import BaseModel

from src.schemas.base import BaseResponseSchema


class AdType(BaseModel):
    id: int
    title: str


def create_ad_type(type):
    return AdType(id=type.id, title=type.title)


class AdTypeResponse(AdType, BaseResponseSchema):
    pass


class AdTypeCreate(AdType):
    pass


class AdTypeUpdate(AdType):
    pass
