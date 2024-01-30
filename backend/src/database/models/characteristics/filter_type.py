from sqlalchemy import  Column, Integer, String

from backend.src.database.base import engine, AbstractModel


class FilterType(AbstractModel):
    __tablename__ = "filter_type"
    id = Column(Integer, autoincrement=True, primary_key=True),
    title = Column(String(256), unique=True, nullable=False, index=True),
    functional_title = Column(String(256),  unique=True, nullable=False, index=True),

    interval_placeholder_from: Union[ClassVar[str], None]
    interval_placeholder_to: Union[ClassVar[str], None]
    interval_placeholder_to: Union[ClassVar[str], None]
