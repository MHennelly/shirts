"""Making Hash Value Not Nullable

Revision ID: 7330f6d52cd5
Revises: 549503bbab1c
Create Date: 2022-10-09 21:04:20.858445

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "7330f6d52cd5"
down_revision = "549503bbab1c"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "hash", "value", existing_type=sa.VARCHAR(length=64), nullable=False
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("hash", "value", existing_type=sa.VARCHAR(length=64), nullable=True)
    # ### end Alembic commands ###
