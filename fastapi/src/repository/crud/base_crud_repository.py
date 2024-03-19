from typing import Type, TypeVar, Optional, Generic, List, Union, Literal

from pydantic import BaseModel
from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.database.models.base import Base

from src.repository.crud.base_repository import AbstractRepository

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=Union[BaseModel, dict])
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=Union[BaseModel, dict])


class SqlAlchemyRepository(AbstractRepository, Generic[ModelType, CreateSchemaType, UpdateSchemaType]):

    def __init__(self, session: AsyncSession, model: Type[ModelType] = None):
        self.model = model
        self._session_factory = session

    async def create(self, data: CreateSchemaType) -> ModelType:
        async with self._session_factory() as session:
            instance = self.model(**data.__dict__) if isinstance(data, BaseModel) else self.model(**data)
            session.add(instance)
            await session.commit()
            await session.refresh(instance)
            return instance

    async def bulk_create(self, data: List[CreateSchemaType]) -> ModelType:
        async with self._session_factory() as session:
            objects = [self.model(**d) for d in data]
            session.add_all(objects)
            await session.commit()
            return objects

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
            return res.scalar_one()

    async def delete(self, **filters) -> None:
        async with self._session_factory() as session:
            await session.execute(delete(self.model).filter_by(**filters))
            await session.commit()

    async def get_single(self, **filters) -> Optional[ModelType]:
        async with self._session_factory() as session:
            row = await session.execute(select(self.model).filter_by(**filters))
            return row.scalar_one_or_none()

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

            stmt = select(self.model).filter_by(**filters).order_by(order_column).limit(limit).offset(offset)
            row = await session.execute(stmt)
            return row.scalars().all()
