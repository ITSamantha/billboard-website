from src.api.transformers.base_transformer import BaseTransformer


class WeekdayTransformer(BaseTransformer):
    def __init__(self):
        super().__init__()
        self.available_includes = []
        self.default_includes = []

    def transform(self, weekday):
        return {
            "id": weekday.id,
            "advertisement_id": weekday.title,
            "weekday": weekday.short_title,
            "start_time": weekday.order,
        }
