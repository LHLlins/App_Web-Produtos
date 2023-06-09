"""Inicial

Revision ID: 6bdac3d5a602
Revises: ac2fac619491
Create Date: 2023-06-06 23:55:56.991473

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6bdac3d5a602'
down_revision = 'ac2fac619491'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('produto', sa.Column('tamanho', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('produto', 'tamanho')
    # ### end Alembic commands ###
