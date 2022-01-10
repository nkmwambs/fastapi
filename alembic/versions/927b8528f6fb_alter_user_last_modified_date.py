"""alter user last modified date

Revision ID: 927b8528f6fb
Revises: 1e7242f651aa
Create Date: 2022-01-10 13:13:25.007380

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '927b8528f6fb'
down_revision = '1e7242f651aa'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column(table_name="users",column_name="user_last_modified_date",nullable=False,type_=sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'))
    pass


def downgrade():
    op.alter_column(table_name="users",column_name="user_last_modified_date",nullable=False,type_=sa.TIMESTAMP())
    pass
