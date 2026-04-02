
"""Add uuid column to decisions for stable cross-workspace identity

Revision ID: 20260306
Revises: 20260220
Create Date: 2026-03-06 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

revision = '20260306'
down_revision = '20260220'
branch_labels = None
depends_on = None


def _column_exists(table_name: str, column_name: str) -> bool:
    bind = op.get_bind()
    result = bind.execute(sa.text(f"PRAGMA table_info({table_name})"))
    columns = [row[1] for row in result]
    return column_name in columns


def upgrade() -> None:
    if not _column_exists('decisions', 'uuid'):
        op.add_column('decisions', sa.Column('uuid', sa.Text(), nullable=True))
        op.create_index('ix_decisions_uuid', 'decisions', ['uuid'], unique=True)


def downgrade() -> None:
    op.drop_index('ix_decisions_uuid', table_name='decisions')
    op.drop_column('decisions', 'uuid')
