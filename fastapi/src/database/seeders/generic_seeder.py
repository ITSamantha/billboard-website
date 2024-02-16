from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import AdStatus


class GenericSeeder:

    def __init__(self, session: AsyncSession):
        self._session_factory = session
        self.initial_data = None

    async def run(self):
        if self.initial_data is None:
            return
        async with self._session_factory() as session:
            for cls, data in self.initial_data.items():
                for key, value in data.items():
                    model = (await session.execute(select(cls).filter_by(id=key))).scalar_one_or_none()
                    if model:
                        for attr_name, attr_value in value.items():
                            setattr(model, attr_name, attr_value)
                    else:
                        model: AdStatus = cls(**value, id=key)
                    session.add(model)
                    await session.commit()
