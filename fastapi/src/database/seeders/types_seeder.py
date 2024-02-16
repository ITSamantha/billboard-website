from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import AdType, BookingType, FilterType, TransactionType
from src.database.seeders.generic_seeder import GenericSeeder


class TypesSeeder(GenericSeeder):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
        self.initial_data = {
            AdType: {
                AdType.TYPE_1: {"title": "type1"},
                AdType.TYPE_2: {"title": "type2"},
                AdType.TYPE_3: {"title": "type3"},
            },
            BookingType: {
                BookingType.TYPE_1: {"title": "type1"},
                BookingType.TYPE_2: {"title": "type2"},
                BookingType.TYPE_3: {"title": "type3"},
            },
            FilterType: {},
            TransactionType: {}

        }
