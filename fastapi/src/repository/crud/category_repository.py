from typing import Optional, Type

from select import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from src.repository.crud.base_crud_repository import SqlAlchemyRepository, ModelType
from src.schemas import Category


class CategoryRepository(SqlAlchemyRepository):

    def __init__(self, session: AsyncSession, model: Type[ModelType] = None):
        super().__init__(session, model)
        self.model = Category

    async def get_single(self, **filters) -> Optional[ModelType]:
        async with self._session_factory() as session:
            row = await session.execute(select(self.model).filter_by(**filters))
            return row.scalar_one_or_none()
