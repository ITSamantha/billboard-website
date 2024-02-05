from typing import ClassVar, Optional

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.entities.base import AbstractBaseEntityModel


class Address(AbstractBaseEntityModel):
    __tablename__ = "address"

    address: Mapped[ClassVar[str]] = mapped_column(String(256), nullable=False)

    country_id: Mapped[Optional[ClassVar[int]]] = mapped_column(ForeignKey("country.id"))
    country: Mapped[Optional["Country"]] = relationship(back_populates="addresses", uselist=False)

    city_id: Mapped[Optional[ClassVar[int]]] = mapped_column(ForeignKey("city.id"))
    city: Mapped[Optional["City"]] = relationship(back_populates="addresses", uselist=False)

    street: Mapped[Optional[ClassVar[str]]] = mapped_column(String(64))
    house: Mapped[Optional[ClassVar[str]]] = mapped_column(String(32))
    flat: Mapped[Optional[ClassVar[str]]] = mapped_column(String(16))

    longitude: Mapped[Optional[ClassVar[float]]] = mapped_column()
    latitude: Mapped[Optional[ClassVar[float]]] = mapped_column()

    advertisement: Mapped["Advertisement"] = relationship(back_populates="address", uselist=False)

    def __repr__(self) -> str:
        return (f"Address(id={self.id}, address={self.address}, country_id={self.country},"
                f"city_id={self.city_id}, street={self.street}, house={self.house}, flat={self.flat},"
                f"longitude={self.longitude}, latitude={self.latitude})")
