from __future__ import annotations

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
    advertisement_type_id: ClassVar[int]  # booking, sell

    price: float | None

    created_at: ClassVar[datetime.datetime]
    updated_at: ClassVar[datetime.datetime]
    deleted_at: ClassVar[datetime.datetime]
