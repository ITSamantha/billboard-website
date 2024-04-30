from src.database.seeders.generic_seeder import GenericSeeder
from src.database.models import AdStatus, BookingStatus, UserStatus


class StatusesSeeder(GenericSeeder):
    def __init__(self):
        super().__init__()
        self.initial_data = {
            AdStatus: {
                AdStatus.PAID: {"title": "paid", "is_shown": True},
                AdStatus.NOT_PAID: {"title": "not paid", "is_shown": False},
                AdStatus.ACTIVE: {"title": "active", "is_shown": True},
                AdStatus.BLOCKED: {"title": "blocked", "is_shown": False}
            },
            BookingStatus: {
                BookingStatus.PAID: {"title": "paid"},
                BookingStatus.NOT_PAID: {"title": "not paid"},
                BookingStatus.IN_PROCESS: {"title": "in progress"},
                BookingStatus.APPROVED: {"title": "approved"},
                BookingStatus.CANCELED: {"title": "canceled"}
            },
            UserStatus: {
                UserStatus.ACTIVE: {'title': 'active', 'is_available': True},
                UserStatus.BLOCKED: {'title': 'blocked', 'is_available': False}
            }
        }
