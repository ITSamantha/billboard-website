"""empty message

Revision ID: 8fa93214c740
Revises: 766c41de4802
Create Date: 2024-03-09 16:27:03.664898

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8fa93214c740'
down_revision: Union[str, None] = '766c41de4802'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
