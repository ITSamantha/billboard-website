import random

from src.database.models import AdTag, Country, City, Address, Advertisement, Category
from faker import Faker
import asyncio

from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository


async def foo():
    fake = Faker()
    ad_tags = []
    cities = []
    countries = []
    addresses = []
    advertisements = []
    categories = []
    for i in range(1, 201):
        ad_tags.append({"id": i, "title": fake.unique.word()})
        cities.append({"id": i, "title": fake.unique.city()})
        countries.append({"id": i, "title": fake.unique.country()})
        addresses.append({"id": i, "country_id": i, "city_id": i, "street": fake.street_address(),
                          "house": str(i), "flat": str(i + 33)})
        advertisements.append({"id": i, "title": fake.sentence(), "user_description": fake.sentence(),
                               "address_id": i, "user_id": random.Random().randint(1, 2),
                               "ad_status_id": random.Random().randint(1, 5),
                               "ad_type_id": random.Random().randint(1, 3),
                               "price": random.Random().randint(100, 100000),
                               "category_id": random.Random().randint(1, 200),
                               "auto_booking": False})
        categories.append({"id": i + 7, "title": fake.word(), "order": random.Random().randint(1, 200),
                           "meta_title": fake.word(), "meta_description": fake.sentence(), "url": fake.url(),
                           "parent_id": random.Random().randint(7, i + 7) if random.Random().randint(0, 20) else None,
                           "bookable": True if random.Random().randint(0, 1) else False,
                           "map_addressable": True if random.Random().randint(0, 1) else False
                           })
    # await SqlAlchemyRepository(db_manager.get_session, AdTag).bulk_create(ad_tags)
    # await SqlAlchemyRepository(db_manager.get_session, City).bulk_create(cities)
    # await SqlAlchemyRepository(db_manager.get_session, Country).bulk_create(countries)
    # await SqlAlchemyRepository(db_manager.get_session, Address).bulk_create(addresses)
    await SqlAlchemyRepository(db_manager.get_session, Category).bulk_create(categories)
    await SqlAlchemyRepository(db_manager.get_session, Advertisement).bulk_create(advertisements)


async def main():
    await foo()


if __name__ == "__main__":
    asyncio.run(main())
