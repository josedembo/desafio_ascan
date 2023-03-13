from src.config.database.connection import DBConnectionHandler
from src.entities.status import Status



class StatusRepositor:
    
    def create(self, name:str):
        with DBConnectionHandler() as db:
            status = Status(status_name = name)
            db.session.add(status)
            db.session.commit()
    
    def getAll(self) -> list:
        with DBConnectionHandler() as db:
            status_data = db.session.query(Status).all()
            return status_data
    
    def updated(self):
        pass
    
    def delete(self):
        pass