from pydantic import BaseModel
from typing import ClassVar


# + not paid
class AdStatus(BaseModel):
    id: ClassVar[int]
    title: ClassVar[str]
    is_shown: ClassVar[bool]
