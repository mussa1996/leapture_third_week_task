"""create user table

Revision ID: 0956b2c2cdc0
Revises: 
Create Date: 2022-02-28 09:20:47.723668

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0956b2c2cdc0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
   op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True,unique=True),
        sa.Column('username', sa.String(100), nullable=False,unique=True),
        sa.Column('email', sa.String(200), nullable=False),
        sa.Column('hash_password',sa.String(100)),
        sa.Column('createdAt',sa.DateTime),
        sa.Column('is_active',sa.Boolean)
    )

def downgrade():
    pass
