from fastapi.src.api.transformers.base_transformer import BaseTransformer


class CountryTransformer(BaseTransformer):
    def __init__(self):
        BaseTransformer.__init__()
        self.available_includes = []
        self.default_includes = []

    def transform(self, country):
        return {
            "id": country.id,
            "title": country.title
        }
