from pydantic import BaseModel

from src.schemas.base import BaseResponseSchema


class Priority(BaseModel):
    priority: int


class PriorityResponse(Priority, BaseResponseSchema):
    pass
