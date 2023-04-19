from sqlalchemy import create_engine, text
import os 
from dotenv import load_dotenv
from src.entities.entities import Status
from src.config.database.connection  import DBConnectionHandler

load_dotenv()

dialect = "mysql"
driver = "pymysql"
username = os.environ.get("DB_USERNAME")
password = str(os.environ.get("DB_PASSWORD"))
port = os.environ.get("DB_PORT")
host = "mysqldb"
database = "desafio_ascan"


with DBConnectionHandler() as db:
    status1 = Status(id = 1, status_name ="Activada")
    status2 = Status(id = 2, status_name = "Cancelada")
    db.session.add(status1)
    db.session.add(status2)
    
    db.session.commit()
