from sqlalchemy import select

from src.repository.crud.base_crud_repository import SqlAlchemyRepository, ModelType


class AdvertisementRepository(SqlAlchemyRepository):
    async def get_multi(
            self,
            order: str = "id",
            order_type=0,
            limit: int = 100,
            offset: int = 0,
            **filters
    ) -> list[ModelType]:
        async with self._session_factory() as session:
            order_column = getattr(self.model, order, None)

            if order_column is None:
                raise ValueError(f"Invalid order column: {order}")

            stmt = select(self.model).filter_by(**filters).order_by(
                order_column.asc() if not order_type else order_column.desc()).limit(limit).offset(offset)
            row = await session.execute(stmt)
            return row.scalars().all()


    async def get