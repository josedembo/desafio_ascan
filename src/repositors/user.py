from src.config.database.connection import DBConnectionHandler
from src.entities.entities import User


class UserRepositor:
    def create(self, email, password, username, full_name):
        with DBConnectionHandler() as db:
            user = User(email=email, password=password, 
                        username=username, full_name=full_name)
            db.session.add(user)
            db.session.commit()
            
    def getall(self):
        with DBConnectionHandler() as db:
            data = db.session.query(User).all()
            return data

    def getById(self, id:int):
        with DBConnectionHandler() as db:
            user = db.session.query(User).filter(User.id==id).first()
            return user
        
    def getByEmail(self, email):
        with DBConnectionHandler() as db:
            user = db.session.query(User).filter(User.email==email).first()
            return user
        
    def getByUsername(self, username):
        with DBConnectionHandler() as db:
            user = db.session.query(User).filter(User.username==username).first()
            return user
    
    def update(self, id:int, full_name):
        with DBConnectionHandler() as db:
            db.session.query(User).filter(User.id==id).update({
                "full_name":full_name 
            })
            db.session.commit()
    def delete(self, id:int):
        with DBConnectionHandler() as db:
            db.session.query(User).filter(User.id==id).delete()
            db.session.commit()