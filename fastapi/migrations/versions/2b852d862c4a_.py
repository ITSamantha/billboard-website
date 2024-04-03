
"""empty message

Revision ID: 2b852d862c4a
Revises: 89ff2b6933c1, 97eab3b10728, c7fc8504c18f, fd56ff9e5cc8
Create Date: 2024-03-29 20:38:03.023840

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2b852d862c4a'
down_revision: Union[str, None] = ('89ff2b6933c1', '97eab3b10728', 'c7fc8504c18f', 'fd56ff9e5cc8')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
