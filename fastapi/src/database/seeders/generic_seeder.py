from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession

from src.repository.crud.base_crud_repository import ModelType


class GenericSeeder:

    def __init__(self, session: AsyncSession):
        self._session_factory = session
        self.initial_data = None

    async def run(self):
        if self.initial_data is None:
            return
        async with self._session_factory() as session:
            for cls, data in self.initial_data.items():
                objects = [cls(**value, id=key) for key, value in data.items()]
                session.add_all(objects)
                await session.commit()
                return objects
