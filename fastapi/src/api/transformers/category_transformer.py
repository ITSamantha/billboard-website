from src.api.transformers.base_transformer import BaseTransformer


class CategoryTransformer(BaseTransformer):
    def __init__(self):
        super().__init__()
        self.available_includes = []
        self.default_includes = []

    def transform(self, category):
        return {
            "id": category.id,
            "title": category.title,
            "order": category.order,
            "bookable": category.bookable,
            "url": category.url,
            "map_addressable": category.map_addressable,
            "meta_title": category.meta_title,
            "meta_description": category.meta_description,
            "parent_id": category.parent_id,
        }
