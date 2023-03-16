"""empty message

Revision ID: a6bdd574a2da
Revises: 53b48adc938e
Create Date: 2023-03-16 08:15:55.118278

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6bdd574a2da'
down_revision = '53b48adc938e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('farm_request', schema=None) as batch_op:
        batch_op.alter_column('sessionId',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.alter_column('typeOfRequest',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.alter_column('phone',
               existing_type=sa.VARCHAR(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('farm_request', schema=None) as batch_op:
        batch_op.alter_column('phone',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('typeOfRequest',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('sessionId',
               existing_type=sa.VARCHAR(),
               nullable=False)

    # ### end Alembic commands ###