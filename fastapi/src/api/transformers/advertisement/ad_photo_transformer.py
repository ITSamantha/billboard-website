from src.api.transformers.base_transformer import BaseTransformer


class AdPhotoTransformer(BaseTransformer):
    def __init__(self):
        super().__init__()
        self.available_includes = []
        self.default_includes = []

    def transform(self, ad_photo):
        return {
            "lol": "kek"
        }
