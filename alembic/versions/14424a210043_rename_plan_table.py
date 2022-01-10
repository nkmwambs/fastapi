"""Rename plan table

Revision ID: 14424a210043
Revises: 5e4dc86ceea9
Create Date: 2022-01-10 12:25:19.750464

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '14424a210043'
down_revision = '5e4dc86ceea9'
branch_labels = None
depends_on = None


def upgrade():
    op.rename_table("plan","plans")
    pass


def downgrade():
    op.rename_table("plans","plan")
    pass
