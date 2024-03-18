from src.api.transformers.base_transformer import BaseTransformer


class CityTransformer(BaseTransformer):
    def __init__(self):
        super().__init__()
        self.available_includes = []
        self.default_includes = []

    def transform(self, city):
        return {
            "id": city.id,
            "title": city.title
        }
