from src.api.transformers.base_transformer import BaseTransformer
from src.api.transformers.weekday_transformer import WeekdayTransformer


class WorktimeTransformer(BaseTransformer):
    def __init__(self):
        super().__init__()
        self.available_includes = []
        self.default_includes = [
            'weekday'
        ]

    def transform(self, worktime):
        return {
            "id": worktime.id,
            "advertisement_id": worktime.advertisement_id,
            "weekday": worktime.weekday,
            "start_time": worktime.start_time,
            "end_time": worktime.end_time,
        }

    def include_weekday(self, worktime):
        return self.item(worktime.weekday, WeekdayTransformer())
