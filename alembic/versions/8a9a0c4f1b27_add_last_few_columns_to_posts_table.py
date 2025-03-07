"""add last few columns to posts table

Revision ID: 8a9a0c4f1b27
Revises: 1053bae81102
Create Date: 2025-03-08 00:00:41.221827

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8a9a0c4f1b27'
down_revision: Union[str, None] = '1053bae81102'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    # op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')),)

    """Upgrade schema."""
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    """Downgrade schema."""
    pass
