"""add column refresh_token for users table

Revision ID: 5ea9a83d88b4
Revises: 
Create Date: 2025-02-05 08:02:49.572478

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5ea9a83d88b4'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(table_name="users", column=sa.Column("refresh_token", sa.String, nullable=True))


def downgrade() -> None:
    op.drop_column(table_name="users", column_name="refresh_token")
