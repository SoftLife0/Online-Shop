"""Initial migration.

Revision ID: 66ce50019858
Revises: 
Create Date: 2021-08-31 14:00:35.488329

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66ce50019858'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.alter_column('item', 'category',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('item', 'category',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_table('categories')
    # ### end Alembic commands ###