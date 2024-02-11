from starlette_admin.contrib.sqla import ModelView

from src.database.models import AdType


class AdTypeView(ModelView):
    fields = [AdType.id, AdType.title]

    page_size = 10

    def __init__(self):
        super().__init__(model=AdType)

        self.label = "Advertisement Types"
        self.name = "Advertisement Type"
        self.name_plural = "Advertisement Types"

        self.icon = "fa fa-th-list"

        self.searchable_fields = [AdType.id, AdType.title]
        self.sortable_fields = [AdType.id, AdType.title]
