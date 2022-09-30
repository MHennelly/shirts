"""Initial Migration

Revision ID: e7bb934b4f15
Revises:
Create Date: 2022-09-30 15:21:08.635466

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "e7bb934b4f15"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "item",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column(
            "size", sa.Enum("XS", "S", "M", "L", "XL", name="size"), nullable=False
        ),
        sa.Column("inventory", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
    )
    op.create_table(
        "order",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("first", sa.String(length=32), nullable=False),
        sa.Column("last", sa.String(length=32), nullable=False),
        sa.Column("email", sa.String(length=32), nullable=False),
        sa.Column("phone", sa.String(length=32), nullable=False),
        sa.Column("fulfilled", sa.Boolean(), nullable=False),
        sa.Column("item_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["item_id"],
            ["item.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
    )
    op.create_table(
        "hash",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("val", sa.String(length=64), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("order_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["order_id"],
            ["order.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("hash")
    op.drop_table("order")
    op.drop_table("item")
    # ### end Alembic commands ###