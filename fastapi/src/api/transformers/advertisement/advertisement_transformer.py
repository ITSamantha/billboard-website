from src.api.transformers.base_transformer import BaseTransformer
from src.api.transformers.address_transformer import AddressTransformer
from src.api.transformers.advertisement import AdTagTransformer, AdTypeTransformer, AdPhotoTransformer, AdStatusTransformer
from src.api.transformers.category_transformer import CategoryTransformer
from src.api.transformers.review_transformer import ReviewTransformer
from src.api.transformers.user import UserTransformer
from src.utils.time import json_datetime, time_ago_in_words


class AdvertisementTransformer(BaseTransformer):
    def __init__(self):
        super().__init__()
        self.available_includes = [
            'address', 'user', 'ad_tags',
            'ad_photos', 'category', 'reviews',
        ]
        self.default_includes = [
            'ad_status', 'ad_type'
        ]

    def transform(self, ad):
        return {
            "id": ad.id,
            "title": ad.title,
            "user_description": ad.user_description,
            "price": ad.price,
            "bookable": ad.category.bookable,
            "created_at": json_datetime(ad.created_at),
            "created_at_str": time_ago_in_words(ad.created_at) if ad.created_at else None,
            "updated_at": json_datetime(ad.updated_at),
            "updated_at_str": time_ago_in_words(ad.updated_at) if ad.updated_at else None,
            "deleted_at": json_datetime(ad.deleted_at)
        }

    def include_address(self, ad):
        return self.item(ad.address, AddressTransformer())

    def include_user(self, ad):
        return self.item(ad.user, UserTransformer())

    def include_ad_tags(self, ad):
        return self.collection(ad.ad_tags, AdTagTransformer())

    def include_ad_photos(self, ad):
        return self.collection(ad.ad_photos, AdPhotoTransformer())

    def include_category(self, ad):
        return self.item(ad.category, CategoryTransformer())

    def include_reviews(self, ad):
        return self.collection(ad.reviews, ReviewTransformer())

    def include_ad_status(self, ad):
        return self.item(ad.ad_status, AdStatusTransformer())

    def include_ad_type(self, ad):
        return self.item(ad.ad_type, AdTypeTransformer())


