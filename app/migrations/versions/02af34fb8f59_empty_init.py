"""Empty init

Revision ID: 02af34fb8f59
Revises: 
Create Date: 2023-08-30 18:52:59.183837

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "02af34fb8f59"
down_revision = None
branch_labels = None
depends_on = None


# includes the code that would be needed to perform changes to the database based on this migration
def upgrade() -> None:
    pass


# includes any code that would be needed to undo this migration and return to the previous state.
def downgrade() -> None:
    pass
