"""add foreign-key to posts table

Revision ID: 1053bae81102
Revises: 3fc7395c0bb9
Create Date: 2025-03-07 23:44:35.273622

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1053bae81102'
down_revision: Union[str, None] = '3fc7395c0bb9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table='posts', referent_table='users', local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")

    """Upgrade schema."""
    pass


def downgrade() -> None:
    op.drop_constraint('posts_owner_id_fkey', table_name='posts', type_='foreignkey')

    op.drop_column('posts', 'owner_id') 
    """Downgrade schema."""
    pass
