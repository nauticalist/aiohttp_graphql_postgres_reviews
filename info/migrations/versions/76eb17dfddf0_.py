"""empty message

Revision ID: 76eb17dfddf0
Revises: 
Create Date: 2019-09-10 03:33:52.078980

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76eb17dfddf0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('review',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_review_id'), 'review', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_review_id'), table_name='review')
    op.drop_table('review')
    # ### end Alembic commands ###