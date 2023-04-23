"""create table subscription

Revision ID: e1ded167ed52
Revises: 042e291741eb
Create Date: 2023-04-21 02:18:47.199482

"""
from alembic import op
import sqlalchemy as sa
from src.config.database.connection import DBConnectionHandler

# revision identifiers, used by Alembic.
revision = 'e1ded167ed52'
down_revision = '042e291741eb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    dbconnection = DBConnectionHandler()
    engine = dbconnection.get_engine()
    conn = engine.connect()
    conn.execute(sa.text("""CREATE TABLE subscriptions (
        id INTEGER NOT NULL AUTO_INCREMENT, 
        status_id INTEGER NOT NULL, 
        user_id INTEGER NOT NULL, 
        created_at DATETIME, 
        updated_at DATETIME, 
        PRIMARY KEY (id), 
        FOREIGN KEY(user_id) REFERENCES users (id) ON DELETE CASCADE
        );"""))
    conn.commit()
    conn.close()


def downgrade() -> None:
    dbconnection = DBConnectionHandler()
    engine = dbconnection.get_engine()
    conn = engine.connect()
    conn.execute(sa.text("DROP TABLE subscriptions;"))
    conn.commit()
    conn.close()
