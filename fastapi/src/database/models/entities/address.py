from typing import Optional
from fastapi import Request

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.base import Base


class Address(Base):
    __tablename__ = "address"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)

    country_id: Mapped[int] = mapped_column(ForeignKey("country.id"), nullable=False)
    country: Mapped["Country"] = relationship(uselist=False, lazy="selectin")

    city_id: Mapped[int] = mapped_column(ForeignKey("city.id"), nullable=False)
    city: Mapped["City"] = relationship(uselist=False, lazy="selectin")

    street: Mapped[str] = mapped_column(String(64), nullable=False)
    house: Mapped[str] = mapped_column(String(32), nullable=False)
    flat: Mapped[Optional[str]] = mapped_column(String(16), nullable=True)

    longitude: Mapped[Optional[float]] = mapped_column(nullable=True)
    latitude: Mapped[Optional[float]] = mapped_column(nullable=True)

    def __repr__(self) -> str:
        return (f"Address(id={self.id}, address={self.address}, country_id={self.country},"
                f"city_id={self.city_id}, street={self.street}, house={self.house}, flat={self.flat},"
                f"longitude={self.longitude}, latitude={self.latitude})")
