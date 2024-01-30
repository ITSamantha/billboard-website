from pydantic import BaseModel
from typing import ClassVar


class Photo(BaseModel):
    id: ClassVar[int]
    photo_path: ClassVar[str]
    photo_thumb: ClassVar[str]
