from sqladmin import ModelView

from src.database.models import Advertisement


class AdvertisementView(ModelView):
    fields = [Advertisement.id, Advertisement.title, Advertisement.user_description,
              Advertisement.user, Advertisement.ad_status, Advertisement.ad_type, Advertisement.price,
              Advertisement.categories,
              Advertisement.created_at, Advertisement.updated_at, Advertisement.deleted_at]

    page_size = 10

    def __init__(self):
        super().__init__(model=Advertisement)

        self.label = "Advertisements"
        self.name = "Advertisement"
        self.name_plural = "Advertisements"

        self.search_builder = True

        self.icon = "fa fa-th-list"

        self.searchable_fields = [Advertisement.id, Advertisement.title, Advertisement.user_description]
        self.sortable_fields = [Advertisement.id, Advertisement.title, Advertisement.user_description,
                                Advertisement.price,
                                Advertisement.created_at, Advertisement.updated_at, Advertisement.deleted_at]
