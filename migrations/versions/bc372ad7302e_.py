"""empty message

Revision ID: bc372ad7302e
Revises: 
Create Date: 2020-11-07 13:44:13.302445

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc372ad7302e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('course',
    sa.Column('subject', sa.String(length=64), nullable=False),
    sa.Column('class_num', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('subject', 'class_num')
    )
    op.create_table('session',
    sa.Column('zoom_link', sa.String(length=120), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('tutor', sa.Integer(), nullable=True),
    sa.Column('tutee', sa.Integer(), nullable=True),
    sa.Column('subject', sa.String(length=64), nullable=True),
    sa.Column('class_num', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('zoom_link')
    )
    op.create_index(op.f('ix_session_date'), 'session', ['date'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('about_me', sa.String(length=140), nullable=True),
    sa.Column('last_seen', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=140), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('booked', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_post_timestamp'), 'post', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_post_timestamp'), table_name='post')
    op.drop_table('post')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_session_date'), table_name='session')
    op.drop_table('session')
    op.drop_table('course')
    # ### end Alembic commands ###
