from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.base import Base


class AdPhoto(Base):
    __tablename__ = "ad_photo"

    advertisement_id: Mapped[int] = mapped_column(ForeignKey("advertisement.id"), nullable=False, primary_key=True)
    photo_id: Mapped[int] = mapped_column(ForeignKey("files.id"), nullable=False, primary_key=True)
