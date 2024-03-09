from typing import Optional

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.base import Base


class Address(Base):
    __tablename__ = "address"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)

    address: Mapped[str] = mapped_column(String(256), nullable=False)

    country_id: Mapped[Optional[int]] = mapped_column(ForeignKey("country.id"))
    country: Mapped[Optional["Country"]] = relationship(uselist=False, lazy="selectin")

    city_id: Mapped[Optional[int]] = mapped_column(ForeignKey("city.id"))
    city: Mapped[Optional["City"]] = relationship(uselist=False, lazy="selectin")

    street: Mapped[Optional[str]] = mapped_column(String(64))
    house: Mapped[Optional[str]] = mapped_column(String(32))
    flat: Mapped[Optional[str]] = mapped_column(String(16))

    longitude: Mapped[Optional[float]] = mapped_column()
    latitude: Mapped[Optional[float]] = mapped_column()


    def __repr__(self) -> str:
        return (f"Address(id={self.id}, address={self.address}, country_id={self.country},"
                f"city_id={self.city_id}, street={self.street}, house={self.house}, flat={self.flat},"
                f"longitude={self.longitude}, latitude={self.latitude})")
