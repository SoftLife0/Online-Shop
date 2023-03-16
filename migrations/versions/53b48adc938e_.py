"""empty message

Revision ID: 53b48adc938e
Revises: 552b0b050812
Create Date: 2023-03-16 08:06:16.336770

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53b48adc938e'
down_revision = '552b0b050812'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('farm',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('owner', sa.String(), nullable=True),
    sa.Column('size', sa.String(), nullable=True),
    sa.Column('crop', sa.String(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('price', sa.String(), nullable=True),
    sa.Column('link', sa.String(), nullable=True),
    sa.Column('otherPictures', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('picture', sa.String(), nullable=True),
    sa.Column('trending', sa.Boolean(), nullable=True),
    sa.Column('category', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('farm_request',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sessionId', sa.String(), nullable=False),
    sa.Column('typeOfRequest', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('phone', sa.String(), nullable=False),
    sa.Column('sent', sa.String(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('farm_request')
    op.drop_table('farm')
    # ### end Alembic commands ###
