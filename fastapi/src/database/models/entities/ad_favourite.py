from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.base import Base


class AdFavourite(Base):
    __tablename__ = "ad_favourite"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)

    advertisement_id: Mapped[int] = mapped_column(ForeignKey("advertisement.id"), nullable=False)
    advertisement: Mapped["Advertisement"] = relationship( uselist=False, lazy="selectin")

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    user: Mapped["User"] = relationship( uselist=False, lazy="selectin")

    def __repr__(self) -> str:
        return (
            f"AdFavourite(id={self.id}, advertisement_id={self.advertisement_id}, user_id={self.user_id})")

