"""add a user table

Revision ID: 6ca2f661426e
Revises: eb2e547e4527
Create Date: 2022-01-10 12:49:29.128177

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.sqltypes import Integer, String


# revision identifiers, used by Alembic.
revision = '6ca2f661426e'
down_revision = 'eb2e547e4527'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("users", sa.Column("user_id", sa.Integer(), primary_key=True, nullable=False), sa.Column(
        'user_email', String(), nullable=False, unique=True), sa.Column("user_password", sa.String(), nullable=False),sa.Column("user_last_modified_date",sa.TIMESTAMP()))
    pass


def downgrade():
    op.drop_table("users")
    pass
