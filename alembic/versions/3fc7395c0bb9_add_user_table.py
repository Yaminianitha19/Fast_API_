"""add user table

Revision ID: 3fc7395c0bb9
Revises: 494ad62d21d3
Create Date: 2025-03-07 23:32:29.127350

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3fc7395c0bb9'
down_revision: Union[str, None] = '494ad62d21d3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None: 
    sa.Column('id', sa.Integer(), nullable=False)
    sa.Column('email', sa.String(), nullable=False)
    sa.Column('password', sa.String(), nullable=False)
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False)
    sa.PrimaryKeyConstraint('id')
    sa.UniqueConstraint('email')

    """Upgrade schema."""
    pass


def downgrade() -> None:
    op.drop_table('users')
    """Downgrade schema."""
    pass
