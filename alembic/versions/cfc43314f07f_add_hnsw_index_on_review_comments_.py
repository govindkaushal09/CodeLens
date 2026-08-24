"""add hnsw index on review_comments embedding

Revision ID: cfc43314f07f
Revises: 26af9476109e
Create Date: 2026-08-25 01:36:28.857841

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cfc43314f07f'
down_revision: Union[str, Sequence[str], None] = '26af9476109e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.execute("""
        CREATE INDEX IF NOT EXISTS review_comments_embedding_hnsw_idx
        ON review_comments
        USING hnsw (embedding vector_cosine_ops)
        WITH (m = 16, ef_construction = 64)
    """)


def downgrade():
    op.execute("DROP INDEX IF EXISTS review_comments_embedding_hnsw_idx")
