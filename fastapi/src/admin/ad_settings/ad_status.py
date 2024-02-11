from starlette_admin.contrib.sqla import ModelView

from src.database.models import AdStatus


class AdStatusView(ModelView):
    fields = [AdStatus.id, AdStatus.title, AdStatus.is_shown]

    page_size = 10

    def __init__(self):
        super().__init__(model=AdStatus)

        self.label = "Advertisement Statuses"
        self.name = "Advertisement Status"
        self.name_plural = "Advertisement Statuses"

        self.icon = "fa fa-check"

        self.searchable_fields = [AdStatus.id, AdStatus.title, AdStatus.is_shown]
        self.sortable_fields = [AdStatus.id, AdStatus.title, AdStatus.is_shown]
