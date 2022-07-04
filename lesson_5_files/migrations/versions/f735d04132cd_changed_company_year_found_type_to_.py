"""Changed Company.year_found type to Integer

Revision ID: f735d04132cd
Revises: 086b67d89f47
Create Date: 2022-07-04 09:13:41.843870

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'f735d04132cd'
down_revision = '086b67d89f47'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('companies', 'year_founded',
                    existing_type=sa.VARCHAR(),
                    type_=sa.Integer(),
                    existing_nullable=True,
                    postgresql_using='year_founded::integer')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('companies', 'year_founded',
                    existing_type=sa.Integer(),
                    type_=sa.VARCHAR(),
                    existing_nullable=True)
    # ### end Alembic commands ###