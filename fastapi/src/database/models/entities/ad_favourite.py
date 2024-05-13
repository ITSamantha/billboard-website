from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.base import Base


class AdFavourite(Base):
    __tablename__ = "ad_favourite"

    advertisement_id: Mapped[int] = mapped_column(ForeignKey("advertisement.id"), nullable=False, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False, primary_key=True)
