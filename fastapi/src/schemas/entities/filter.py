

from pydantic import BaseModel


class Filter(BaseModel):
    title: str
    filter_type_id: int
    order: int


class FilterResponse(Filter, BaseResponseSchema):
    pass


class FilterCreate(Filter):
    pass


class FilterUpdate(Filter):
    pass
