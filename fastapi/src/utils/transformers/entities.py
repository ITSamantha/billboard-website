from src.database.models import Advertisement, Address, City, Country, AdTag, Category
from src.utils.time import time_ago_in_words
from src.utils.transformers.characteristics import transform_country, transform_city, transform_ad_type, \
    transform_ad_status


def transform_ad_tag(ad_tag: AdTag) -> dict:
    return {
        "id": ad_tag.id,
        "title": ad_tag.title
    }


def transform_category(category: Category) -> dict:
    return {
        "id": category.id,
        "title": category.title,
        "order": category.order,
        "bookable": category.bookable,
        "url": category.url,
        "map_addressable": category.map_addressable,
        "meta_title": category.meta_title,
        "meta_description": category.meta_description,
        "parent_id": category

    }


def transform_advertisement(advertisement: Advertisement) -> dict:
    # TODO:  CREATE RELATION ATTRS HERE AS IN MODEL

    return {"id": advertisement.id,
            "title": advertisement.title,
            "user_description": advertisement.user_description,
            "address": transform_address(advertisement.address) if advertisement.address else None,
            "user": create_user_short(advertisement.user) if advertisement.user else None,
            "ad_status": transform_ad_status(advertisement.ad_status) if advertisement.ad_status else None,
            "ad_type": transform_ad_type(advertisement.ad_type) if advertisement.ad_type else None,
            "ad_tags": [transform_ad_tag(tag) for tag in advertisement.ad_tags] if advertisement.ad_tags else None,
            "ad_photos": [create_ad_photo(photo) for photo in
                          advertisement.ad_photos] if advertisement.ad_photos else None,
            "categories": [create_category_short(category) for category in
                           advertisement.categories] if advertisement.categories else None,
            "reviews": [create_review(review) for review in advertisement.reviews if
                        not review.deleted_at] if advertisement.reviews else None,
            "price": advertisement.price,
            "bookable": any(
                [category.bookable for category in advertisement.categories]) if advertisement.categories else False,
            "created_at": advertisement.created_at,
            "created_at_str": time_ago_in_words(advertisement.created_at) if advertisement.created_at else None,
            "updated_at": advertisement.updated_at,
            "updated_at_str": time_ago_in_words(advertisement.updated_at) if advertisement.updated_at else None,
            "deleted_at": advertisement.deleted_at}


def transform_address(address: Address) -> dict:
    return {
        "id": address.id,
        "address": address.address,
        "country": transform_country(address.country) if address.country else None,
        "city": transform_city(address.city) if address.city else None,
        "street": address.street,
        "house": address.house,
        "flat": address.flat,
        "longitude": address.longitude,
        "latitude": address.latitude
    }
