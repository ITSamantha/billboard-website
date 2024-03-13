from typing import Optional, Type

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.database.models import Category
from src.repository.crud.base_crud_repository import SqlAlchemyRepository, ModelType


class CategoryRepository(SqlAlchemyRepository):

    def __init__(self, session: AsyncSession, model: Type[ModelType] = None):
        super().__init__(session, model)
        self.model = Category

    async def get_single(self, **filters) -> Optional[ModelType]:
        async with self._session_factory() as session:
            row = await session.execute(select(self.model).filter_by(**filters))
            return row.scalar_one_or_none()

    async def get_children_list(self, category_id):
        async with self._session_factory() as session:
            async with session.begin():
                children = await session.execute(select(Category).filter(Category.parent_id == category_id).options(
                    selectinload(Category.children)))
            return [child for child in children.scalars() if child]  # children.all()

    """
    async with session.begin():
        # cte_query = select(Category).filter_by(**filters).cte(name='children_for', recursive=True)
        recursive_query = select(Category).filter(Category.parent_id == category_id)

        final_query = select(Category).select_from(recursive_query)
        result = await session.execute(final_query)
        return result.scalars().all()
    """
