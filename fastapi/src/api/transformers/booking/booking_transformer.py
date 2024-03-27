from src.api.transformers.advertisement import AdvertisementTransformer
from src.api.transformers.base_transformer import BaseTransformer
from src.api.transformers.booking.booking_status_transformer import BookingStatusTransformer
from src.api.transformers.user import UserTransformer
from src.database.models import Booking
from src.utils.time import json_datetime, time_ago_in_words


class BookingTransformer(BaseTransformer):
    def __init__(self):
        super().__init__()
        self.available_includes = [
            'advertisement',
            'user'
        ]
        self.default_includes = [
            "booking_status",
        ]

    def transform(self, booking: Booking):
        return {
            "id": booking.id,
            "user_id": booking.user_id,
            "guest_count": booking.guest_count,
            "advertisement_id": booking.advertisement_id,
            "time_from": json_datetime(booking.time_from),
            "time_end": json_datetime(booking.time_end),
            "deadline_at": json_datetime(booking.deadline_at),
            "created_at": json_datetime(booking.created_at),
            "created_at_str": time_ago_in_words(booking.created_at),
            "updated_at": json_datetime(booking.updated_at),
            "updated_at_str": time_ago_in_words(booking.updated_at),
            "deleted_at": json_datetime(booking.deleted_at)
        }

    def include_user(self, booking):
        return self.item(booking.user, UserTransformer())

    def include_booking_status(self, booking):
        return self.item(booking.booking_status, BookingStatusTransformer())

    def include_advertisement(self, booking):
        return self.item(booking.advertisement, AdvertisementTransformer())
