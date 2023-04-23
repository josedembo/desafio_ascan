"""create user table

Revision ID: 042e291741eb
Revises: 
Create Date: 2023-04-21 01:40:29.820177

"""
from alembic import op
import sqlalchemy as sa
from src.config.database.connection import DBConnectionHandler

# revision identifiers, used by Alembic.
revision = '042e291741eb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    dbconnection = DBConnectionHandler()
    engine = dbconnection.get_engine()
    conn = engine.connect()
    conn.execute(sa.text("""CREATE TABLE users (
        id INTEGER NOT NULL AUTO_INCREMENT, 
        full_name VARCHAR(250) NOT NULL, 
        username VARCHAR(20) NOT NULL, 
        password TEXT NOT NULL, 
        email VARCHAR(50) NOT NULL, 
        created_at DATETIME, 
        updated_at DATETIME, 
        PRIMARY KEY (id), 
        UNIQUE (username), 
        UNIQUE (email), 
        UNIQUE (username), 
        UNIQUE (email)
        );"""))
    conn.commit()
    conn.close()


def downgrade() -> None:
    dbconnection = DBConnectionHandler()
    engine = dbconnection.get_engine()
    conn = engine.connect()
    conn.execute(sa.text("DROP TABLE users;"))
    conn.commit()
    conn.close()
