from src.api.transformers.base_transformer import BaseTransformer


class AdStatusTransformer(BaseTransformer):
    def __init__(self):
        super().__init__()
        self.available_includes = []
        self.default_includes = []

    def transform(self, ad_status):
        return {
            "id": ad_status.id,
            "title": ad_status.title,
            "is_shown": ad_status.is_shown
        }
