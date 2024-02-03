from typing import ClassVar, Optional

from src.schemas.characteristics.base import BaseCharacteristic


# checkbox (multiple_select)
# text
# radio (color, select)
# numerical_interval
# date_interval

# в скобках title, отдельная строка -- functional_title

class FilterType(BaseCharacteristic):
    functional_title: ClassVar[str]

    interval_placeholder_from: Optional[ClassVar[str]]
    interval_placeholder_to: Optional[ClassVar[str]]
