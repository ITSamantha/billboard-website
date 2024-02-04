from typing import ClassVar

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database.database import Base


class AdvertisementCategory(Base):
    __tablename__ = "advertisement__category"

    advertisement_id: Mapped[ClassVar[int]] = mapped_column(ForeignKey('advertisement.id'), nullable=False)
    category_id: Mapped[ClassVar[int]] = mapped_column(ForeignKey('category.id'), nullable=False)
