from sqlalchemy.orm import mapped_column, Mapped

from src.database.database import Base


class AbstractModel(Base):
    __abstract__ = True

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
