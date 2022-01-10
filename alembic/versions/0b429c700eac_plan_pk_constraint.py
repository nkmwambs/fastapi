"""Plan PK constraint

Revision ID: 0b429c700eac
Revises: 7f4a5c0188f4
Create Date: 2022-01-10 16:34:05.862432

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.elements import Null
from sqlalchemy.schema import Sequence, CreateSequence


# revision identifiers, used by Alembic.
revision = '0b429c700eac'
down_revision = '7f4a5c0188f4'
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
