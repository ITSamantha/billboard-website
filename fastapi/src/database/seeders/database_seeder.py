from typing import List

from src.database.seeders.generic_seeder import GenericSeeder
from src.database.seeders.statuses_seeder import StatusesSeeder
from src.database.session_manager import db_manager


class DatabaseSeeder:

    def __init__(self):
        self.seeders: List[GenericSeeder] = [
            StatusesSeeder(db_manager.session_factory)
        ]

    async def run(self):
        if self.seeders:
            for seeder in self.seeders:
                await seeder.run()


async def main():
    db_s = DatabaseSeeder()
    await db_s.run()


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
