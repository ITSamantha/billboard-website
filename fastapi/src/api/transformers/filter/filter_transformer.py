from src.api.transformers.base_transformer import BaseTransformer
from src.api.transformers.filter.filter_type_transformer import FilterTypeTransformer
from src.api.transformers.filter.filter_value_transformer import FilterValueTransformer


class FilterTransformer(BaseTransformer):
    def __init__(self):
        super().__init__()
        self.available_includes = ["filter_values"]
        self.default_includes = ["filter_type"]

    def transform(self, filter):
        return {
            "id": filter.id,
            "title": filter.title,
            "order": filter.order
        }

    def include_filter_type(self, filter):
        return self.item(filter.filter_type, FilterTypeTransformer())

    def include_filter_values(self, filter):
        return self.collection(filter.filter_values, FilterValueTransformer())
