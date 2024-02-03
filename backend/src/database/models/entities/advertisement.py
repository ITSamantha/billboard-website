from typing import ClassVar, Union, Optional

from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.entities.base import BaseEntityModelTime


class Advertisement(BaseEntityModelTime):
    __tablename__ = "advertisement"

    title: Mapped[ClassVar[str]] = mapped_column(String(128), nullable=False)
    user_description: Mapped[ClassVar[str]] = mapped_column(Text, nullable=False)

    address_id: Mapped[Optional[ClassVar[int]]] = mapped_column(ForeignKey('address.id'))

    user_id: Mapped[ClassVar[int]] = mapped_column(ForeignKey('user.id'), nullable=False)

    advertisement_status_id: ClassVar[int]
    advertisement_type_id: ClassVar[int]  # booking, sell

    price: Union[ClassVar[float], None]
