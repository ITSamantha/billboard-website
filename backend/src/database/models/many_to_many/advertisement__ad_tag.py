from typing import ClassVar

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

from src.database.database import Base


class AdvertisementAdTag(Base):
    __tablename__ = "advertisement__ad_tag"

    advertisement_id: Mapped[ClassVar[int]] = mapped_column(ForeignKey('advertisement.id'), nullable=False)
    tag_id: Mapped[ClassVar[int]] = mapped_column(ForeignKey('ad_tag.id'), nullable=False)
