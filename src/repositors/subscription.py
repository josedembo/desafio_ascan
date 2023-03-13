from src.config.database.connection import DBConnectionHandler
from src.entities.subscription import Subscription
from src.entities.user import User
from src.entities.event_history import EventHistory
from src.entities.status import Status


class SubscriptionRepositor:
    
    def create(self, user_id, status_id, ):
        with DBConnectionHandler() as db:
            new_subscription = Subscription(user_id=user_id, status_id=status_id)
            db.session.add(new_subscription)
            db.session.commit()
    
    def getAll(self):
        with DBConnectionHandler() as db:
            all_subscriptions = db.session.query(Subscription).all()
            return all_subscriptions
    
    def getById(self, subscription_id):
        with DBConnectionHandler() as db:
            subscription = db.session.query(Subscription).filter(Subscription.id==subscription_id).first()
            return subscription
        
    def getByUserId(self, user_id:int):
        with DBConnectionHandler() as db:
            subscription = db.session.query(Subscription).filter(Subscription.user_id==user_id).first()
            return subscription
    
    def updated(self,subsc_id:int, status_id:int):
        with DBConnectionHandler() as db:
            db.session.query(Subscription).filter(Subscription.id == subsc_id).update({
                "status_id": status_id
            })
            db.session.commit()
    
    def select(self):
        with DBConnectionHandler() as db:
            subs_data = db.session.query(Subscription, EventHistory, Status )\
                .join(target=EventHistory,onclause=Subscription.id==EventHistory.subscription_id)\
                .join(target=Status, onclause=Subscription.status_id==Status.id)\
                .with_entities(
                    Subscription.id,
                    Subscription.created_at,
                    Subscription.updated_at,
                    EventHistory.type,
                    EventHistory.created_at,
                    Status.status_name
                ).all()
                
            return subs_data
                