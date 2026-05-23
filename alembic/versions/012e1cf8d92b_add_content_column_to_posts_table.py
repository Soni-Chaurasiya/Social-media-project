"""add content column to posts table

Revision ID: 012e1cf8d92b
Revises: 81c912ad1d05
Create Date: 2026-05-21 13:09:09.223758

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '012e1cf8d92b'
down_revision: Union[str, Sequence[str], None] = '81c912ad1d05'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable = False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', "content")
    pass
