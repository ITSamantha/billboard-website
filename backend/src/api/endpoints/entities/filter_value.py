from pydantic import BaseModel
from typing import ClassVar, Union


class FilterValue(BaseModel):
    id: ClassVar[int]
    filter_id: ClassVar[int]
    value: ClassVar[str]
    hint_html: Union[ClassVar[str], None]
