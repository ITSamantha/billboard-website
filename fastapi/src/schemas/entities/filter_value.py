from typing import Optional


from pydantic import BaseModel


class FilterValue(BaseModel):
    filter_id: int
    value: str
    hint_html: Optional[str]
    order: int


class FilterValueResponse(FilterValue, BaseResponseSchema):
    pass


class FilterValueCreate(FilterValue):
    pass


class FilterValueUpdate(FilterValue):
    pass
