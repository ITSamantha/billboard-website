from sqlalchemy import select, or_

from src.repository.crud.base_crud_repository import SqlAlchemyRepository, ModelType


class AdvertisementRepository(SqlAlchemyRepository):
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

            stmt = select(self.model).filter_by(**filters).order_by(
                order_column.asc()).limit(limit).offset(offset)
            row = await session.execute(stmt)
            return row.scalars().all()

    async def search_multi(self, limit: int = 100,
                           offset: int = 0, *filters):
        async with self._session_factory() as session:
            stmt = select(self.model).filter(or_(*filters)).limit(limit).offset(offset)
            row = await session.execute(stmt)
            return row.scalars().all()
