from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.base import Base


class AdFavourite(Base):
    __tablename__ = "ad_favourite"

    advertisement_id: Mapped[int] = mapped_column(ForeignKey("advertisement.id"), nullable=False, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False, primary_key=True)

    advertisement: Mapped["Advertisement"] = relationship( uselist=False, lazy="selectin")
    user: Mapped["User"] = relationship( uselist=False, lazy="selectin")

