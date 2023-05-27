"""inicializando db

Revision ID: b89dba84bdaf
Revises: 
Create Date: 2023-05-25 22:18:58.450440

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b89dba84bdaf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('alunos',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=False),
    sa.Column('matricula', sa.String(length=100), nullable=False),
    sa.Column('av1', sa.Integer(), nullable=False),
    sa.Column('av2', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('alunos')
    # ### end Alembic commands ###