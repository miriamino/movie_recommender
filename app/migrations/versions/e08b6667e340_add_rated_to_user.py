"""add rated to user

Revision ID: e08b6667e340
Revises: 
Create Date: 2020-12-07 20:26:41.210750

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'e08b6667e340'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_user_email', table_name='user')
    op.drop_index('ix_user_username', table_name='user')
    op.drop_table('user')
    op.drop_table('ratings')
    op.drop_table('movies')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movies',
    sa.Column('id', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('title', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('genres', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('imdb_id', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('year', sa.TEXT(), autoincrement=False, nullable=True)
    )
    op.create_table('ratings',
    sa.Column('id', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('movie_id', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('rating', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('timestamp', postgresql.TIMESTAMP(), autoincrement=False, nullable=True)
    )
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('username', sa.VARCHAR(length=64), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('password_hash', sa.VARCHAR(length=128), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='user_pkey')
    )
    op.create_index('ix_user_username', 'user', ['username'], unique=True)
    op.create_index('ix_user_email', 'user', ['email'], unique=True)
    # ### end Alembic commands ###
