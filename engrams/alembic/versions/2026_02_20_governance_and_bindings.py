
"""Governance, Code Bindings, and lifecycle columns

Revision ID: 20260220
Revises: 20250617
Create Date: 2026-02-20 19:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

revision = '20260220'
down_revision = '20250617'
branch_labels = None
depends_on = None


def _column_exists(table_name: str, column_name: str) -> bool:
    bind = op.get_bind()
    result = bind.execute(sa.text(f"PRAGMA table_info({table_name})"))
    columns = [row[1] for row in result]
    return column_name in columns


def _table_exists(table_name: str) -> bool:
    bind = op.get_bind()
    result = bind.execute(
        sa.text("SELECT name FROM sqlite_master WHERE type='table' AND name=:name"),
        {"name": table_name}
    )
    return result.fetchone() is not None


def upgrade() -> None:
    # Feature 1: Governance
    if not _table_exists('context_scopes'):
        op.create_table('context_scopes',
            sa.Column('id', sa.Integer(), nullable=False, autoincrement=True),
            sa.Column('scope_type', sa.Text(), nullable=False),
            sa.Column('scope_name', sa.Text(), nullable=False),
            sa.Column('parent_scope_id', sa.Integer(), nullable=True),
            sa.Column('created_by', sa.Text(), nullable=False),
            sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
            sa.ForeignKeyConstraint(['parent_scope_id'], ['context_scopes.id'], ondelete='SET NULL'),
            sa.PrimaryKeyConstraint('id')
        )
        op.create_index('ix_context_scopes_scope_type', 'context_scopes', ['scope_type'])
        op.create_index('ix_context_scopes_parent_scope_id', 'context_scopes', ['parent_scope_id'])

    if not _table_exists('governance_rules'):
        op.create_table('governance_rules',
            sa.Column('id', sa.Integer(), nullable=False, autoincrement=True),
            sa.Column('scope_id', sa.Integer(), nullable=False),
            sa.Column('rule_type', sa.Text(), nullable=False),
            sa.Column('entity_type', sa.Text(), nullable=False),
            sa.Column('rule_definition', sa.Text(), nullable=False),
            sa.Column('description', sa.Text(), nullable=True),
            sa.Column('is_active', sa.Boolean(), nullable=False, server_default=sa.text('1')),
            sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
            sa.Column('updated_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
            sa.ForeignKeyConstraint(['scope_id'], ['context_scopes.id'], ondelete='CASCADE'),
            sa.PrimaryKeyConstraint('id')
        )
        op.create_index('ix_governance_rules_scope_id', 'governance_rules', ['scope_id'])
        op.create_index('ix_governance_rules_entity_type', 'governance_rules', ['entity_type'])

    if not _table_exists('scope_amendments'):
        op.create_table('scope_amendments',
            sa.Column('id', sa.Integer(), nullable=False, autoincrement=True),
            sa.Column('source_item_type', sa.Text(), nullable=False),
            sa.Column('source_item_id', sa.Integer(), nullable=False),
            sa.Column('target_item_type', sa.Text(), nullable=False),
            sa.Column('target_item_id', sa.Integer(), nullable=False),
            sa.Column('status', sa.Text(), nullable=False),
            sa.Column('rationale', sa.Text(), nullable=True),
            sa.Column('reviewed_by', sa.Text(), nullable=True),
            sa.Column('reviewed_at', sa.DateTime(), nullable=True),
            sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
            sa.PrimaryKeyConstraint('id')
        )
        op.create_index('ix_scope_amendments_status', 'scope_amendments', ['status'])

    # Add governance columns to existing tables
    for tbl in ['decisions', 'system_patterns', 'progress_entries', 'custom_data']:
        if not _column_exists(tbl, 'scope_id'):
            op.add_column(tbl, sa.Column('scope_id', sa.Integer(), nullable=True))
        if not _column_exists(tbl, 'visibility'):
            op.add_column(tbl, sa.Column('visibility', sa.Text(), server_default=sa.text("'workspace'"), nullable=True))
        if not _column_exists(tbl, 'override_status'):
            op.add_column(tbl, sa.Column('override_status', sa.Text(), nullable=True))

    if not _column_exists('decisions', 'lifecycle_status'):
        op.add_column('decisions', sa.Column('lifecycle_status', sa.Text(), server_default=sa.text("'accepted'"), nullable=True))

    # Feature 2: Code Bindings
    if not _table_exists('code_bindings'):
        op.create_table('code_bindings',
            sa.Column('id', sa.Integer(), nullable=False, autoincrement=True),
            sa.Column('item_type', sa.Text(), nullable=False),
            sa.Column('item_id', sa.Integer(), nullable=False),
            sa.Column('file_pattern', sa.Text(), nullable=False),
            sa.Column('symbol_pattern', sa.Text(), nullable=True),
            sa.Column('binding_type', sa.Text(), nullable=False),
            sa.Column('confidence', sa.Text(), server_default=sa.text("'manual'"), nullable=False),
            sa.Column('last_verified_at', sa.DateTime(), nullable=True),
            sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
            sa.Column('updated_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
            sa.PrimaryKeyConstraint('id')
        )
        op.create_index('ix_code_bindings_item_type_id', 'code_bindings', ['item_type', 'item_id'])

    if not _table_exists('code_binding_verifications'):
        op.create_table('code_binding_verifications',
            sa.Column('id', sa.Integer(), nullable=False, autoincrement=True),
            sa.Column('binding_id', sa.Integer(), nullable=False),
            sa.Column('verification_status', sa.Text(), nullable=False),
            sa.Column('files_matched', sa.Integer(), nullable=True),
            sa.Column('verified_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
            sa.Column('notes', sa.Text(), nullable=True),
            sa.ForeignKeyConstraint(['binding_id'], ['code_bindings.id'], ondelete='CASCADE'),
            sa.PrimaryKeyConstraint('id')
        )
        op.create_index('ix_cbv_binding_id', 'code_binding_verifications', ['binding_id'])


def downgrade() -> None:
    op.drop_table('code_binding_verifications')
    op.drop_table('code_bindings')
    op.drop_table('scope_amendments')
    op.drop_table('governance_rules')
    op.drop_table('context_scopes')
