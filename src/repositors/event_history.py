from src.config.database.connection import DBConnectionHandler
from src.entities.entities import EventHistory


class EventHistoryReporsitory:
    
    def create(self, subscription_id:int, type:str, created_at) -> None:
        with DBConnectionHandler() as db:
            event  = EventHistory(subscription_id=subscription_id, type=type, created_at=created_at)
            db.session.add(event)
            db.session.commit()
            
    def getAll(self) -> list:
        with DBConnectionHandler() as db:
            events = db.session.query(EventHistory).all()
            return events
    
    def getBySubscriptionId(self, subscription_id:int):
        with DBConnectionHandler() as db:
            event = db.session.query(EventHistory).filter(EventHistory.subscription_id==subscription_id).first()
            return event
        
    def delete(self, envent_id):
        pass
        