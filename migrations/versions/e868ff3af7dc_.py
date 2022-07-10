"""empty message

Revision ID: e868ff3af7dc
Revises: d9f6e9002cd7
Create Date: 2022-06-26 15:13:17.974153

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e868ff3af7dc'
down_revision = 'd9f6e9002cd7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('title', table_name='episode')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('title', 'episode', ['title'], unique=False)
    # ### end Alembic commands ###