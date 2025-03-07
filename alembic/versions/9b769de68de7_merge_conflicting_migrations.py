"""merge conflicting migrations

Revision ID: 9b769de68de7
Revises: 108e0118b7f0
Create Date: 2025-03-08 00:43:33.445262

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9b769de68de7'
down_revision = ("108e0118b7f0", "ce909b0dbf1a")

branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    down_revision = ("108e0118b7f0", "ce909b0dbf1a")

    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
