from typing import ClassVar, Union, Optional

from src.schemas.characteristics.base import BaseCharacteristic


class Weekday(BaseCharacteristic):
    short_title: Optional[ClassVar[str]]
    order: ClassVar[int]
