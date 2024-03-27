from src.api.transformers.base_transformer import BaseTransformer


class AccountTransactionTypeTransformer(BaseTransformer):
    def __init__(self):
        super().__init__()
        self.available_includes = []
        self.default_includes = []

    def transform(self, type):
        return {
            "id": type.id,
            "name": type.name,
            "sign": type.sign,
        }
