"""create table event_history

Revision ID: 77dc2e8bedcf
Revises: e1ded167ed52
Create Date: 2023-04-21 02:19:11.454856

"""
from alembic import op
import sqlalchemy as sa
from src.config.database.connection import DBConnectionHandler

# revision identifiers, used by Alembic.
revision = '77dc2e8bedcf'
down_revision = 'e1ded167ed52'
branch_labels = None
depends_on = None


def upgrade() -> None:
    dbconnection = DBConnectionHandler()
    engine = dbconnection.get_engine()
    conn = engine.connect()
    conn.execute(sa.text("""CREATE TABLE event_histories (
        id INTEGER NOT NULL AUTO_INCREMENT, 
        subscription_id INTEGER NOT NULL, 
        type VARCHAR(120) NOT NULL, 
        created_at DATETIME NOT NULL, 
        PRIMARY KEY (id), 
        FOREIGN KEY(subscription_id) REFERENCES subscriptions (id) ON DELETE CASCADE
        );"""))
    conn.commit()
    conn.close()


def downgrade() -> None:
    dbconnection = DBConnectionHandler()
    engine = dbconnection.get_engine()
    conn = engine.connect()
    conn.execute(sa.text("DROP TABLE event_histories;"))
    conn.commit()
    conn.close()
