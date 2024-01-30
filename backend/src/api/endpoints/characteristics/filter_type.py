from pydantic import BaseModel
from typing import ClassVar, Union


# checkbox (multiple_select)
# text
# radio (color, select)
# numerical_interval
# date_interval

# в скобках title, отдельная строка -- functional_title

class FilterType(BaseModel):
    id: ClassVar[int]
    title: ClassVar[str]
    functional_title: ClassVar[str]

    interval_placeholder_from: Union[ClassVar[str], None]
    interval_placeholder_to: Union[ClassVar[str], None]
    interval_placeholder_to: Union[ClassVar[str], None]
