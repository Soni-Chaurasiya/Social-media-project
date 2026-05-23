"""add last few columns to posts table

Revision ID: 9dcb6ed4193e
Revises: 74130b51e971
Create Date: 2026-05-21 15:01:58.770013

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9dcb6ed4193e'
down_revision: Union[str, Sequence[str], None] = '74130b51e971'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column('created_at',sa.TIMESTAMP(timezone=True), nullable= False, server_default=sa.text('NOW()')),)
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'published')
    op.drop_column('posts','created_at')
    pass
