from pydantic import BaseModel
from typing import ClassVar


class AdFavourite(BaseModel):
    advertisement_id: ClassVar[int]
    user_id: ClassVar[int]
