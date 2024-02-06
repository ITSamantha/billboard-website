from pydantic import BaseModel


class BaseSchema(BaseModel):
    pass


class BaseResponseSchema:
    id: int
