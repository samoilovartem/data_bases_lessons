"""Added Payment.currency

Revision ID: e084bea24ce6
Revises: f735d04132cd
Create Date: 2022-07-04 09:26:24.086520

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e084bea24ce6'
down_revision = 'f735d04132cd'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('payments', sa.Column('currency', sa.String(), nullable=True))
    op.execute("UPDATE payments SET currency='PHP'")
    op.alter_column('payments', 'currency', nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('payments', 'currency')
    # ### end Alembic commands ###
