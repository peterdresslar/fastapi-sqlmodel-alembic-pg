"""itemcreate id

Revision ID: a312ee780480
Revises: 848c0aaaabbc
Create Date: 2024-10-14 16:27:00.436929

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
# see https://stackoverflow.com/a/69063829
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'a312ee780480'
down_revision: Union[str, None] = '848c0aaaabbc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###