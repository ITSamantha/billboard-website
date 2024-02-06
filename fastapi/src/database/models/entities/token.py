from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.entities.base import AbstractBaseEntityModelTime


class Token(AbstractBaseEntityModelTime):
    __tablename__ = "token"

    access_token: Mapped[str] = mapped_column(nullable=False)
    token_type: Mapped[str] = mapped_column(nullable=False)
