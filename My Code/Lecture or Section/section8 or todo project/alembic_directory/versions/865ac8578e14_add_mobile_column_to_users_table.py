"""add mobile column to users table

Revision ID: 865ac8578e14
Revises: 
Create Date: 2024-11-19 16:50:20.641814

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '865ac8578e14'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
  op.add_column('users', sa.Column('mobile', sa.String(length=15), nullable=True))



def downgrade() -> None:
    op.drop_column('users', 'mobile')
