from src.api.transformers.base_transformer import BaseTransformer


class BookingStatusTransformer(BaseTransformer):
    def __init__(self):
        super().__init__()
        self.available_includes = []
        self.default_includes = []

    def transform(self, booking_status):
        return {
            "id": booking_status.id,
            "title": booking_status.title
        }
