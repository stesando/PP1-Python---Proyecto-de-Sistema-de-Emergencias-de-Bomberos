
"""migracion inicial

Revision ID: 5cb750e07ce7
Revises:
Create Date: 2026-11-18 11:39:17.211927
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlmodel.sql.sqltypes import AutoString


# revision identifiers
revision: str = "5cb750e07ce7"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade() -> None:
    op.create_table(
        "bomberos",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("nombre", AutoString(length=50), nullable=False),
        sa.Column("apellido", AutoString(length=50), nullable=False),
        sa.Column("rango", AutoString(length=30), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )

    with op.batch_alter_table("emergencias") as batch_op:
        batch_op.add_column(
            sa.Column("bombero_id", sa.Integer(), nullable=True)
        )
        batch_op.create_foreign_key(
            "fk_emergencias_bomberos",
            "bomberos",
            ["bombero_id"],
            ["id"],
        )


def downgrade() -> None:
    with op.batch_alter_table("emergencias") as batch_op:
        batch_op.drop_constraint(
            "fk_emergencias_bomberos",
            type_="foreignkey",
        )
        batch_op.drop_column("bombero_id")

    op.drop_table("bomberos")
