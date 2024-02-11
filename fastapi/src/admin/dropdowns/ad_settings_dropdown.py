from starlette_admin import DropDown

from src.admin.ad_settings.ad_type import AdTypeView
from src.admin.ad_settings.ad_status import AdStatusView

advertisement_dropdown = DropDown(
    "Advertisements Settings",
    icon="fa fa-table",
    views=[
        AdStatusView,
        AdTypeView
    ],
)
