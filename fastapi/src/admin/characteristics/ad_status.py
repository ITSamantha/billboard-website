from sqladmin import ModelView

from src.database.models import AdStatus


class AdStatusView(ModelView, model=AdStatus):
    fields = [AdStatus.id, AdStatus.title, AdStatus.is_shown]
    label = "Advertisement Statuses"
    name = "Advertisement Status"
    name_plural = "Advertisement Statuses"
    page_size = 10
    icon = "fa fa-check"
    column_searchable_list = [AdStatus.id, AdStatus.title, AdStatus.is_shown]
    column_sortable_list = [AdStatus.id, AdStatus.title, AdStatus.is_shown]
