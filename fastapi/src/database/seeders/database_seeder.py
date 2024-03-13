import asyncio
from typing import List, Any

from sqlalchemy.ext.asyncio import AsyncSession

from database.seeders.generic_seeder import GenericSeeder
from database.seeders.permissions_seeder import PermissionsSeeder
from database.seeders.statuses_seeder import StatusesSeeder
from database.seeders.types_seeder import TypesSeeder
from database.seeders.utils_seeder import UtilsSeeder
from database.session_manager import db_manager




class DatabaseSeeder:

    def __init__(self):
        self.session_factory: AsyncSession = db_manager.session_factory
        self.seeders: List[Any[GenericSeeder]] = [
            StatusesSeeder,
            TypesSeeder,
            PermissionsSeeder,
            UtilsSeeder
        ]

    async def run(self):
        try:
            if self.seeders:
                for seeder in self.seeders:
                    await seeder().run(self.session_factory)
        except Exception as e:
            print(e)


async def run_seeders(*args, **kwargs):
    db_s = DatabaseSeeder()
    await db_s.run()


if __name__ == "__main__":
    asyncio.run(run_seeders())
