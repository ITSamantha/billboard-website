from pydantic import BaseModel
from typing import ClassVar


class Filter(BaseModel):
    id: ClassVar[int]
    title: ClassVar[str]
    filter_type_id: ClassVar[int]
    order: ClassVar[int]
