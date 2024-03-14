from src.api.transformers.base_transformer import BaseTransformer


class AdTagTransformer(BaseTransformer):
    def __init__(self):
        super().__init__()
        self.available_includes = []
        self.default_includes = []

    def transform(self, ad_tag):
        return {
            "id": ad_tag.id,
            "title": ad_tag.title
        }
