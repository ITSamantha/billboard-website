from src.api.transformers.base_transformer import BaseTransformer


class FilterValueTransformer(BaseTransformer):
    def __init__(self):
        super().__init__()
        self.available_includes = ["filter"]
        self.default_includes = []

    def transform(self, filter_value):
        return {
            "id": filter_value.id,
            "value": filter_value.value,
            "order": filter_value.order,
            "hint_html": filter_value.hint_html,
            "filter_id": filter_value.filter_id
        }

    def include_filter(self, filter_value):
        return self.item(filter_value.filter, "FilterTransformer()")
