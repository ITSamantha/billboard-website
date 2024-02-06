from typing import Type, TypeVar, Optional, Generic

from pydantic import BaseModel
from sqlalchemy import delete, select, update, exc
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models.base import Base

from src.repository.crud.base_repository import AbstractRepository

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class SqlAlchemyRepository(AbstractRepository, Generic[ModelType, CreateSchemaType, UpdateSchemaType]):

    def __init__(self, session: AsyncSession, model: Type[ModelType] = None):
        self.model = model
        self._session_factory = session

    async def create(self, data: CreateSchemaType) -> ModelType:
        try:
            async with self._session_factory() as session:
                obj_create_data = data.model_dump(exclude_none=True, exclude_unset=True)
                instance = self.model(**obj_create_data)
                session.add(instance)
                await session.commit()
                await session.refresh(instance)
                return instance.id
        except (exc.SQLAlchemyError, Exception) as error:
            pass

    async def update(self, data: UpdateSchemaType, **filters) -> ModelType:
        try:
            async with self._session_factory() as session:
                stmt = update(self.model).values(**data).filter_by(**filters).returning(self.model)
                res = await session.execute(stmt)
                await session.commit()
                return res.scalar_one()
        except (exc.SQLAlchemyError, Exception) as error:
            pass

    async def delete(self, **filters) -> None:
        try:
            async with self._session_factory() as session:
                await session.execute(delete(self.model).filter_by(**filters))
                await session.commit()
        except (exc.SQLAlchemyError, Exception) as error:
            pass

    async def get_single(self, **filters) -> Optional[ModelType]:
        try:
            async with self._session_factory() as session:
                row = await session.execute(select(self.model).filter_by(**filters))
                return row.scalar_one_or_none()
        except (exc.SQLAlchemyError, Exception) as error:
            pass

    async def get_multi(
            self,
            order: str = "id",
            limit: int = 100,
            offset: int = 0
    ) -> list[ModelType]:
        try:
            async with self._session_factory() as session:
                stmt = select(self.model).order_by(*order).limit(limit).offset(offset)
                row = await session.execute(stmt)
                return row.scalars().all()
        except (exc.SQLAlchemyError, Exception) as error:
            pass
