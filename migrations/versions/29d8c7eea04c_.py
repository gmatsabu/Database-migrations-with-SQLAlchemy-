"""empty message

Revision ID: 29d8c7eea04c
Revises: ff7dbb42863e
Create Date: 2020-05-10 13:19:49.846486

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29d8c7eea04c'
down_revision = 'ff7dbb42863e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recruit', sa.Column('id_number', sa.VARCHAR(length=10), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('recruit', 'id_number')
    # ### end Alembic commands ###
