from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
import datetime
from src.config.app.config import settings_app

from src.database.models.base import Base


class Disk:
    IMAGES: str = 'images'


class File(Base):
    __tablename__ = "files"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)

    disk: Mapped[str] = mapped_column(String, nullable=False)
    path: Mapped[str] = mapped_column(String, nullable=False)
    extension:  Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(nullable=False, default=datetime.datetime.now())

    @property
    def link(self):
        return settings_app.APP_URL + '/files/' + self.disk + '/' + self.path
