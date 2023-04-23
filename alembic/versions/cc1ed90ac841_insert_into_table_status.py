"""insert into table status

Revision ID: cc1ed90ac841
Revises: f32f967af3e1
Create Date: 2023-04-21 02:47:55.505759

"""
from alembic import op
import sqlalchemy as sa
from src.config.database.connection import DBConnectionHandler

# revision identifiers, used by Alembic.
revision = 'cc1ed90ac841'
down_revision = 'f32f967af3e1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    dbconnection = DBConnectionHandler()
    engine = dbconnection.get_engine()
    conn = engine.connect()
    conn.execute(sa.text("""INSERT  INTO desafio_ascan.status (id, status_name) VALUES (1, "Activa"),(2, "Cancelada");"""))
    conn.commit()
    conn.close()


def downgrade() -> None:
    dbconnection = DBConnectionHandler()
    engine = dbconnection.get_engine()
    conn = engine.connect()
    conn.execute(sa.text("DELETE FROM status;"))
    conn.commit()
    conn.close()
