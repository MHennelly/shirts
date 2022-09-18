"""Initial Migration

Revision ID: 84ce5e55b294
Revises:
Create Date: 2022-09-17 23:20:10.305848

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "84ce5e55b294"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "item",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column(
            "size", sa.Enum("XS", "S", "M", "L", "XL", name="size"), nullable=True
        ),
        sa.Column("inventory", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
    )
    op.create_table(
        "order",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("address1", sa.String(length=32), nullable=False),
        sa.Column("address2", sa.String(length=32), nullable=True),
        sa.Column("city", sa.String(length=32), nullable=False),
        sa.Column("state", sa.Enum("CA", name="state"), nullable=False),
        sa.Column("postal_code", sa.String(length=16), nullable=False),
        sa.Column("item_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["item_id"],
            ["item.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("order")
    op.drop_table("item")
    # ### end Alembic commands ###
