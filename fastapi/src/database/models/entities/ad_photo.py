from fastapi import Request

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.base import Base


class AdPhoto(Base):
    __tablename__ = "ad_photo"

    advertisement_id: Mapped[int] = mapped_column(ForeignKey("advertisement.id"), nullable=False, primary_key=True)
    photo_id: Mapped[int] = mapped_column(ForeignKey("files.id"), nullable=False, primary_key=True)

    # photo: Mapped["Photo"] = relationship(uselist=False, lazy="selectin")

    # advertisement_id: Mapped[int] = mapped_column(ForeignKey("advertisement.id"), nullable=False)
    # advertisement: Mapped["Advertisement"] = relationship(uselist=False, lazy="selectin")

    # is_main: Mapped[bool] = mapped_column(default=False, nullable=False)

    # def __repr__(self) -> str:
    #     return (
    #         f"AdPhoto(id={self.id}, photo_id={self.photo_id}, "
    #         f"advertisement_id={self.advertisement_id}, is_main={self.is_main})")

    # async def __admin_repr__(self, request: Request):
    #     return f"{self.last_name} {self.first_name}, {self.email}"
    #
    # async def __admin_select2_repr__(self, request: Request) -> str:
    #     return f'<div><span>{self.last_name} {self.first_name}, <i>{self.email}</i></span></div>'
