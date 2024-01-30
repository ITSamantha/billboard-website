from sqlalchemy import String, Boolean, Table, Column, Integer
from sqlalchemy.orm import Mapped, mapped_column

from backend.src.database.base import metadata

ad_status = Table(
    "ad_status",
    metadata,
    Column("id", Integer, autoincrement=True, primary_key=True),
    Column("title", String(64), unique=True, nullable=False, index=True),
    Column("is_shown", Boolean, nullable=False),
)
