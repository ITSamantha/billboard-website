from fastapi.src.api.transformers.base_transformer import BaseTransformer
from fastapi.src.api.transformers.address_transformer import AddressTransformer


class AdvertisementTransformer(BaseTransformer):
    def __init__(self):
        BaseTransformer.__init__()
        self.available_includes = [
            'address',
        ]
        self.default_includes = [

        ]

    def transform(self, ad):
        return {
            "id": ad.id,
            "title": ad.title,
            "user_description": ad.user_description,
            # "user": transform_user(ad.user) if ad.user else None,
            # "ad_status": transform_ad_status(ad.ad_status) if ad.ad_status else None,
            # "ad_type": transform_ad_type(ad.ad_type) if ad.ad_type else None,
            # "ad_tags": [transform_ad_tag(tag) for tag in ad.ad_tags] if ad.ad_tags else None,
            # "ad_photos": [transform_ad_photo(photo) for photo in
            #               ad.ad_photos] if ad.ad_photos else None,
            # "category": transform_category(ad.category),
            # "reviews": [transform_review(review) for review in ad.reviews if
            #             not review.deleted_at] if ad.reviews else None,
            "price": ad.price,
            "bookable": ad.category.bookable,
            # "created_at": json_datetime(ad.created_at),
            # "created_at_str": time_ago_in_words(ad.created_at) if ad.created_at else None,
            # "updated_at": json_datetime(ad.updated_at),
            # "updated_at_str": time_ago_in_words(ad.updated_at) if ad.updated_at else None,
            # "deleted_at": json_datetime(ad.deleted_at)
        }

    def include_address(self, ad):
        return self.item(ad.address, AddressTransformer())

