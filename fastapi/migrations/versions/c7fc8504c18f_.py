"""empty message

Revision ID: c7fc8504c18f
Revises: c2edc61a9c98
Create Date: 2024-03-27 14:21:11.655277

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c7fc8504c18f'
down_revision: Union[str, None] = 'c2edc61a9c98'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
