from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os 

load_dotenv()

dialect = "mysql"
driver = "pymysql"
username = os.environ.get("DB_USERNAME")
password = os.environ.get("DB_PASSWORD")
port = os.environ.get("DB_PORT")
host = "localhost"
database = "desafio_ascan"

class DBConnectionHandler:
    
    def __init__(self) -> None:
        self.__conection_string = f"{dialect}+{driver}://{username}:{password}@{host}:{port}/{database}"
        self.__engine = self.__create_engine()
        self.session = None
        
    
    def __create_engine(self):
        engine = create_engine(self.__conection_string)
        return engine
    
    def get_engine(self):
        return self.__engine
    
    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self
    
    def __exit__(self, exc_type, exp_val, exc_tb):
        self.session.close()