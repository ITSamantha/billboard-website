from src.api.transformers.base_transformer import BaseTransformer


class AdTypeTransformer(BaseTransformer):
    def __init__(self):
        super().__init__()
        self.available_includes = []
        self.default_includes = []

    def transform(self, ad_type):
        return {
            "id": ad_type.id,
            "title": ad_type.title
        }
