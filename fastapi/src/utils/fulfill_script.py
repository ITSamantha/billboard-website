from src.database.models import AdTag, Country, City
from faker import Faker
import asyncio  # Import asyncio module

from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository


async def foo():
    fake = Faker()
    ad_tags = []
    cities = []
    countries = []
    addresses = []
    for i in range(1, 801):
        ad_tags.append({"title": fake.unique.word()})
        cities.append({"title": fake.unique.city()})
        countries.append({"title": fake.unique.country()})
        addresses.append({"country_id": i,  })
    await SqlAlchemyRepository(db_manager.get_session, AdTag).bulk_create(ad_tags)
    await SqlAlchemyRepository(db_manager.get_session, City).bulk_create(cities)
    await SqlAlchemyRepository(db_manager.get_session, Country).bulk_create(countries)


# Define an asynchronous main function
async def main():
    await foo()  # Await foo() inside an asynchronous context


# Run the main function inside an event loop
if __name__ == "__main__":
    asyncio.run(main())
