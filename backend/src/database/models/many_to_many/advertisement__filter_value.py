from typing import ClassVar

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database.database import Base


class AdvertisementFilterValue(Base):
    __tablename__ = "advertisement__filter_value"

    advertisement_id: Mapped[ClassVar[int]] = mapped_column(ForeignKey('advertisement.id'), nullable=False)
    filter_value_id: Mapped[ClassVar[int]] = mapped_column(ForeignKey('filter_value.id'), nullable=False)
