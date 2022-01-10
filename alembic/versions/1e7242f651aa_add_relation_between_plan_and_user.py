"""add relation between plan and user

Revision ID: 1e7242f651aa
Revises: 6ca2f661426e
Create Date: 2022-01-10 12:56:39.005463

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.elements import CollectionAggregate
from sqlalchemy.sql.schema import ForeignKeyConstraint


# revision identifiers, used by Alembic.
revision = '1e7242f651aa'
down_revision = '6ca2f661426e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("plans", sa.Column("user_id", sa.Integer(), nullable=False))
    op.create_foreign_key("fk_plan_user_id", source_table="plans",
                          referent_table="users", local_cols=["user_id"], remote_cols=["user_id"],ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint(constraint_name="fk_plan_user_id",table_name="plans")
    op.drop_column("plans","user_id")
    pass
