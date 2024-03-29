from src.api.transformers.base_transformer import BaseTransformer


class FileTransformer(BaseTransformer):
    def __init__(self):
        super().__init__()
        self.available_includes = []
        self.default_includes = []

    def transform(self, file):
        return {
            "id": file.id,
            "link": file.link,
        }
