"""empty message

Revision ID: 766d430e7d89
Revises: 8a85586f5897
Create Date: 2023-07-31 14:41:09.537194

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '766d430e7d89'
down_revision = '8a85586f5897'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('game', sa.Column('current_player', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('game', 'current_player')
    # ### end Alembic commands ###