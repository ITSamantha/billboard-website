from typing import Optional, Type

from pydantic import BaseModel
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.database import models
from src.database.models import Category
from src.repository.crud.base_crud_repository import SqlAlchemyRepository, ModelType, UpdateSchemaType

RECURSION_DEPTH = 100


class CategoryRepository(SqlAlchemyRepository):

    def __init__(self, session: AsyncSession, model: Type[ModelType] = None):
        super().__init__(session, model)
        self.model = Category

    async def get_single(self, **filters) -> Optional[ModelType]:
        async with self._session_factory() as session:
            stmt = (
                select(self.model)
                .filter_by(**filters)
                .options(selectinload(self.model.children, recursion_depth=RECURSION_DEPTH))
            )
            row = await session.execute(stmt)
            result = row.scalars().first()
            return result

    async def update(self, data: UpdateSchemaType, **filters) -> ModelType:
        async with self._session_factory() as session:
            if isinstance(data, BaseModel):
                data = {**data.__dict__}  # todo test
            stmt = update(self.model) \
                .values(**data) \
                .filter_by(**filters) \
                .returning(self.model)
            res = await session.execute(stmt)
            await session.commit()
            return res.scalars().first()

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
                .options(selectinload(self.model.children, recursion_depth=RECURSION_DEPTH))
            )
            print(stmt)
            row = await session.execute(stmt)
            return row.scalars().all()
