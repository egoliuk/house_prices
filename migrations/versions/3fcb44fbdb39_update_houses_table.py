"""update houses table

Revision ID: 3fcb44fbdb39
Revises: cc1433e9f775
Create Date: 2019-06-21 16:39:41.229132

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3fcb44fbdb39'
down_revision = 'cc1433e9f775'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('house', sa.Column('MSZoning', sa.String(length=32), nullable=True))
    op.drop_column('house', 'MSSubClass')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('house', sa.Column('MSSubClass', sa.VARCHAR(length=2), nullable=True))
    op.drop_column('house', 'MSZoning')
    # ### end Alembic commands ###
