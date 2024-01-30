from pydantic import BaseModel
from typing import ClassVar, Union


class Weekday(BaseModel):
    id: ClassVar[int]
    short_title: Union[ClassVar[str], None]
    title: ClassVar[str]
