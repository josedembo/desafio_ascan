"""create table status

Revision ID: f32f967af3e1
Revises: 77dc2e8bedcf
Create Date: 2023-04-21 02:19:38.179035

"""
from alembic import op
import sqlalchemy as sa
from src.config.database.connection import DBConnectionHandler

# revision identifiers, used by Alembic.
revision = 'f32f967af3e1'
down_revision = '77dc2e8bedcf'
branch_labels = None
depends_on = None


def upgrade() -> None:
    dbconnection = DBConnectionHandler()
    engine = dbconnection.get_engine()
    conn = engine.connect()
    conn.execute(sa.text("""CREATE TABLE status (
        id INTEGER NOT NULL AUTO_INCREMENT, 
        status_name VARCHAR(50) NOT NULL, 
        PRIMARY KEY (id), 
        UNIQUE (status_name), 
        UNIQUE (status_name)
        );"""))
    conn.commit()
    conn.close()


def downgrade() -> None:
    dbconnection = DBConnectionHandler()
    engine = dbconnection.get_engine()
    conn = engine.connect()
    conn.execute(sa.text("DROP TABLE status;"))
    conn.commit()
    conn.close()
