"""Add plan start date column

Revision ID: eb2e547e4527
Revises: 14424a210043
Create Date: 2022-01-10 12:29:14.198754

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.sqltypes import Date


# revision identifiers, used by Alembic.
revision = 'eb2e547e4527'
down_revision = '14424a210043'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("plans",sa.Column("plan_start_date",Date,nullable=False))
    pass


def downgrade():
    op.drop_column("plans","plan_start_date")
    pass
