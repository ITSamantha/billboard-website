import datetime
from pydantic import BaseModel
from typing import ClassVar, Union


class Advertisement(BaseModel):
    id: ClassVar[int]
    title: ClassVar[str]
    user_description: ClassVar[str]

    address_id: Union[ClassVar[int], None]
    user_id: ClassVar[int]
    advertisement_status_id: ClassVar[int]

    created_at: ClassVar[datetime.datetime]
    updated_at: ClassVar[datetime.datetime]
    deleted_at: ClassVar[datetime.datetime]
