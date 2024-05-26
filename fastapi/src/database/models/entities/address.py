from typing import Optional

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.base import Base


class Address(Base):
    __tablename__ = "address"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)

    address: Mapped[str] = mapped_column(String(254), nullable=True)

    country_id: Mapped[int] = mapped_column(ForeignKey("country.id"), nullable=True)
    country: Mapped["Country"] = relationship(uselist=False, lazy="selectin")

    city_id: Mapped[int] = mapped_column(ForeignKey("city.id"), nullable=True)
    city: Mapped["City"] = relationship(uselist=False, lazy="selectin")

    street: Mapped[str] = mapped_column(String(64), nullable=True)
    house: Mapped[str] = mapped_column(String(32), nullable=True)
    flat: Mapped[Optional[str]] = mapped_column(String(16), nullable=True)

    longitude: Mapped[Optional[float]] = mapped_column(nullable=True)
    latitude: Mapped[Optional[float]] = mapped_column(nullable=True)
