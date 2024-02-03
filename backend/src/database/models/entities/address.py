from typing import ClassVar, Union, Optional

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.entities.base import BaseEntityModel


class Address(BaseEntityModel):
    __tablename__ = 'address'

    address: Mapped[ClassVar[str]] = mapped_column(String(256), nullable=False)
    country_id: Mapped[Optional[ClassVar[int]]] = mapped_column(ForeignKey('country.id'))
    city_id: Mapped[Optional[ClassVar[int]]] = mapped_column(ForeignKey('city.id'))
    street: Mapped[Optional[ClassVar[str]]] = mapped_column(String(64))
    house: Mapped[Optional[ClassVar[str]]] = mapped_column(String(32))
    flat: Mapped[Optional[ClassVar[str]]] = mapped_column(String(16))

    longitude: Mapped[Optional[ClassVar[float]]] = mapped_column()
    latitude: Mapped[Optional[ClassVar[float]]] = mapped_column()
