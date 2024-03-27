from src.api.transformers.advertisement import AdvertisementTransformer
from src.api.transformers.base_transformer import BaseTransformer
from src.database.models import AdBookingAvailable
from src.utils.time import json_datetime, time_ago_in_words


class AdBookingAvailableTransformer(BaseTransformer):
    def __init__(self):
        super().__init__()
        self.available_includes = [
            'advertisement'
        ]
        self.default_includes = [
        ]

    def transform(self, booking: AdBookingAvailable):
        return {
            "id": booking.id,
            "price": booking.price,
            "advertisement_id": booking.advertisement_id,
            "time_from": json_datetime(booking.time_from),
            "time_end": json_datetime(booking.time_end),
            "min_booking_time": str(booking.min_booking_time),
            "max_booking_time": str(booking.max_booking_time),
            "created_at": json_datetime(booking.created_at),
            "created_at_str": time_ago_in_words(booking.created_at),
            "updated_at": json_datetime(booking.updated_at),
            "updated_at_str": time_ago_in_words(booking.updated_at),
            "deleted_at": json_datetime(booking.deleted_at)
        }

    def include_advertisement(self, booking):
        return self.item(booking.advertisement, AdvertisementTransformer())
