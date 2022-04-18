"""empty message

Revision ID: e65ffbc90def
Revises: 605a688d0cd2
Create Date: 2022-04-18 11:29:29.984378

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e65ffbc90def'
down_revision = '77fdc857c94f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('systems', sa.Column('cpu_state', sa.ARRAY(sa.String()), nullable=True))
    op.add_column('systems', sa.Column('io_state', sa.ARRAY(sa.String()), nullable=True))
    op.add_column('systems', sa.Column('memory_state', sa.ARRAY(sa.String()), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('systems', 'memory_state')
    op.drop_column('systems', 'io_state')
    op.drop_column('systems', 'cpu_state')
    # ### end Alembic commands ###
