from starlette_admin.contrib.sqla import Admin, ModelView

from src.database.models import AdStatus


class AdStatusView(ModelView):

    fields = [AdStatus.id, AdStatus.title]

    def __init__(self):
        super().__init__(model=AdStatus)
        self.label = "Advertisement Status"
        self.name = "Advertisement Status"
        self.name_plural = "Advertisement Statuses"
        self.icon = "fa fa-check"
