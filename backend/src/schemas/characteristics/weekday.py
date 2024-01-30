from typing import ClassVar, Union

from src.schemas.characteristics.base import BaseCharacteristic


class Weekday(BaseCharacteristic):
    short_title: Union[ClassVar[str], None]
    order: ClassVar[int]
