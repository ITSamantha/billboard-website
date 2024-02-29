import datetime


from pydantic import BaseModel


class View(BaseModel):
    advertisement_id: int
    view_count: int
    date: datetime.date


class ViewResponse(View, BaseResponseSchema):
    pass


class ViewCreate(View):
    pass


class ViewUpdate(View):
    pass
