"""empty message

Revision ID: 23fbe682bac0
Revises: 49c3f6c4da7f
Create Date: 2022-05-19 00:13:46.555878

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23fbe682bac0'
down_revision = '49c3f6c4da7f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pepe',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=120), nullable=False),
    sa.Column('poder', sa.String(length=120), nullable=False),
    sa.Column('tipo', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nombre'),
    sa.UniqueConstraint('nombre')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pepe')
    # ### end Alembic commands ###
