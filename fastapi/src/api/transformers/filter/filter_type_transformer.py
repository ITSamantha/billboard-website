from src.api.transformers.base_transformer import BaseTransformer


class FilterTypeTransformer(BaseTransformer):
    def __init__(self):
        super().__init__()
        self.available_includes = []
        self.default_includes = []

    def transform(self, filter_type):
        return {
            "id": filter_type.id,
            "title": filter_type.title,
            "functional_title": filter_type.functional_title,
            "interval_placeholder_from": filter_type.interval_placeholder_from,
            "interval_placeholder_to": filter_type.interval_placeholder_to
        }
