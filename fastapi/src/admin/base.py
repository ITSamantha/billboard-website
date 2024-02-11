from starlette_admin.contrib.sqla import Admin

from src.admin.characteristics.ad_status import AdStatusView
from src.database.models import AdStatus
from src.database.session_manager import db_manager

admin = Admin(db_manager.engine, title="Otiva Billboard")

admin.add_view(AdStatusView)

"""
admin.add_view(
    DropDown(
        "Resources",
        icon="fa fa-list",
        views=[
            ModelView(User),
            Link(label="Home Page", url="/"),
            CustomView(label="Dashboard", path="/dashboard", template_path="dashboard.html"),
        ],
    )
)
"""
