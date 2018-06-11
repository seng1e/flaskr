"""about_me

Revision ID: 2722c2c4048c
Revises: c1a4cb28a4ee
Create Date: 2018-06-02 12:06:00.011047

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2722c2c4048c'
down_revision = 'c1a4cb28a4ee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###