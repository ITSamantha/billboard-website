from src.api.transformers.base_transformer import BaseTransformer


class TariffTransformer(BaseTransformer):
    def __init__(self):
        super().__init__()
        self.available_includes = []
        self.default_includes = []

    def transform(self, tariff):
        return {
            "id": tariff.id,
            "name": tariff.name,
            "description": tariff.description,
            "price": tariff.price,
        }
