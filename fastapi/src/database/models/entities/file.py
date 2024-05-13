from sqlalchemy import String, event
from sqlalchemy.orm import Mapped, mapped_column
import datetime
from src.config.app.config import settings_app

from src.database.models.base import Base
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.utils.storage import storage


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

    @staticmethod
    async def save(file):
        path, ext = storage.save_from_base64(file, Disk.IMAGES)
        return await SqlAlchemyRepository(db_manager.get_session, model=File) \
            .create({
                'path': path,
                'extension': ext,
                'disk': Disk.IMAGES,
        })


@event.listens_for(File, 'before_delete')
def rm_from_fs(mapper, connect, target):
    storage.remove(target)