from src.api.transformers.base_transformer import BaseTransformer
from src.api.transformers.country_transformer import CountryTransformer

from src.api.transformers.city_transformer import CityTransformer


class AddressTransformer(BaseTransformer):
    def __init__(self):
        BaseTransformer.__init__()
        self.available_includes = []
        self.default_includes = [
            'country', 'city'
        ]

    def transform(self, address):
        return {
            "id": address.id,
            "street": address.street,
            "house": address.house,
            "flat": address.flat,
            "longitude": address.longitude,
            "latitude": address.latitude
        }

    def include_country(self, address):
        return self.item(address.country, CountryTransformer())

    def include_city(self, address):
        return self.item(address.city, CityTransformer())
