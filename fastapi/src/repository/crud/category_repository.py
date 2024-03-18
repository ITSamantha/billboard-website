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
            category = await session.execute(
                select(self.model).filter_by(**filters).options(
                    selectinload(self.model.children)
                )
            )
            return category.scalar_one_or_none()

    async def get_children_list(self, category_id):
        async with self._session_factory() as session:
            async with session.begin():
                children = await session.execute(select(Category).filter(Category.parent_id == category_id).options(
                    selectinload(Category.children)))
            return [child for child in children.scalars() if child]  # children.all()


    async def get_multi(
            self,
            order: str = "id",
            limit: int = 100,
            offset: int = 0,
            **filters
    ) -> list[ModelType]:
        async with self._session_factory() as session:
            order_column = getattr(self.model, order, None)

            if order_column is None:
                raise ValueError(f"Invalid order column: {order}")

            stmt = (
                select(self.model)
                .filter_by(**filters)
                .order_by(order_column)
                .limit(limit)
                .offset(offset)
                .options(selectinload(self.model.children))
            )
            row = await session.execute(stmt)
            return row.scalars().all()