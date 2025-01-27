"""adds planet and moon

Revision ID: ca4a40f798eb
Revises: 
Create Date: 2023-01-07 18:06:12.711798

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca4a40f798eb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planet',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('radius', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planet')
    # ### end Alembic commands ###
