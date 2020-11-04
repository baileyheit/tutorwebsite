"""empty message

Revision ID: dd51535c9f59
Revises: 400cf42356f5
Create Date: 2020-11-03 21:40:22.796756

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd51535c9f59'
down_revision = '400cf42356f5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('course',
    sa.Column('subject', sa.String(length=64), nullable=False),
    sa.Column('class_num', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('subject', 'class_num')
    )
    op.add_column('post', sa.Column('booked', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'booked')
    op.drop_table('course')
    # ### end Alembic commands ###
