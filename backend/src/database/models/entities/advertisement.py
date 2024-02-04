from typing import ClassVar, Optional

from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.entities.base import BaseEntityModelTime


class Advertisement(BaseEntityModelTime):
    __tablename__ = "advertisement"

    title: Mapped[ClassVar[str]] = mapped_column(String(128), nullable=False)
    user_description: Mapped[ClassVar[str]] = mapped_column(Text, nullable=False)

    address_id: Mapped[Optional[ClassVar[int]]] = mapped_column(ForeignKey('address.id'))

    user_id: Mapped[ClassVar[int]] = mapped_column(ForeignKey('user.id'), nullable=False)

    ad_status_id: Mapped[ClassVar[int]] = mapped_column(ForeignKey('ad_status.id'),
                                                        nullable=False)
    ad_type_id: Mapped[ClassVar[int]] = mapped_column(ForeignKey('ad_type.id'),
                                                      nullable=False)  # booking, sell

    price: Mapped[Optional[ClassVar[float]]] = mapped_column(nullable=False)
