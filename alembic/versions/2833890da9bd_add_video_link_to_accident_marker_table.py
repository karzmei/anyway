"""add video_link to AccidentMarker table

Revision ID: 2833890da9bd
Revises: 3741581c7fc4
Create Date: 2017-12-30 20:47:49.566429

"""

# revision identifiers, used by Alembic.
revision = '2833890da9bd'
down_revision = '3741581c7fc4'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('markers', sa.Column('video_link', sa.Text(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('markers', 'video_link')
    ### end Alembic commands ###
