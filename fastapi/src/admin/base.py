from starlette_admin import DropDown, CustomView
from starlette_admin.contrib.sqla import Admin, ModelView
from starlette_admin.views import Link

from src.database.models import AdStatus, User
from src.database.session_manager import db_manager

admin = Admin(db_manager.engine, title="Example: SQLAlchemy")

admin.add_view(ModelView(AdStatus))
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
