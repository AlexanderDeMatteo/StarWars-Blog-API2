"""empty message

Revision ID: 7e433b08a175
Revises: 0e8a2005e86d
Create Date: 2022-05-19 01:27:56.653823

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e433b08a175'
down_revision = '0e8a2005e86d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planetas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=120), nullable=False),
    sa.Column('region', sa.String(length=120), nullable=False),
    sa.Column('sistema', sa.String(length=200), nullable=False),
    sa.Column('especie_nativa', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nombre'),
    sa.UniqueConstraint('nombre')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planetas')
    # ### end Alembic commands ###
