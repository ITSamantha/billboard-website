from pydantic import BaseModel
from typing import ClassVar


class BaseCharacteristic(BaseModel):
    id: ClassVar[int]
    title: ClassVar[str]
