from pydantic import BaseModel
from typing import ClassVar
import datetime


class Review(BaseModel):
    id: ClassVar[int]

    advertisement_id: ClassVar[int]
    user_id: ClassVar[int]

    text: ClassVar[str]
    rating: ClassVar[int]

    created_at: ClassVar[datetime.datetime]
    updated_at: ClassVar[datetime.datetime]
    deleted_at: ClassVar[datetime.datetime]
