from src.config.database.connection import DBConnectionHandler
from src.entities.entities import Subscription, Status, EventHistory
from sqlalchemy.orm.exc import NoResultFound


class SubscriptionRepositor:
    
    def create(self, user_id, status_id, ):
        with DBConnectionHandler() as db:
            try:
                new_subscription = Subscription(user_id=user_id, status_id=status_id)
                db.session.add(new_subscription)
                db.session.commit()
            except Exception as ex:
                db.session.rollback()
                raise ex
            
    def select_by_userId(self, user_id):
        with DBConnectionHandler() as db:
            try:
                subscription = db.session.query(Subscription).filter(Subscription.user_id==user_id).first()
                return subscription
            except NoResultFound:
                return None
            except Exception as ex:
                db.session.rollback()
                raise ex
    
    def select_by_id_user(self, subscription_id, user_id):
        with DBConnectionHandler() as db:
            try:
                subscription = db.session.query(Subscription).filter(Subscription.id == subscription_id, Subscription.user_id == user_id).first()
                return subscription
            except Exception as ex:
                db.session.rollback()
                raise ex
    
    def getById(self, subscription_id):
        with DBConnectionHandler() as db:
            try:
                subscription = db.session.query(Subscription, EventHistory)\
                .join(target=EventHistory, onclause=Subscription.id==EventHistory.subscription_id)\
                .filter(Subscription.id==subscription_id).all()
                return subscription
            except Exception as ex:
                db.session.rollback()
                raise ex
        
    def select_by_Id(self, id):
        with DBConnectionHandler() as db:
            try:
                subscription = db.session.query(Subscription).filter(Subscription.id==id).first()
                return subscription
            except NoResultFound:
                return None
            except Exception as ex:
                db.session.rollback()
                raise ex
    
    def update(self,subscription_id:int, status_id:int):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Subscription).filter(Subscription.id == subscription_id).update({
                    "status_id": status_id
                })
                db.session.commit()
            except Exception as ex:
                db.session.rollback()
                raise ex
    
    def select(self):
        with DBConnectionHandler() as db:
            try: 
                subs_data = db.session.query(Subscription, Status )\
                    .join(target=Status, onclause=Subscription.status_id==Status.id)\
                    .all()
                return subs_data
            except Exception as ex:
                db.session.rollback()
                raise ex
    def select_by_status(self, status):
        with DBConnectionHandler() as db:
            try: 
                subs_data = db.session.query(Subscription, Status )\
                    .join(target=Status, onclause=Subscription.status_id==Status.id)\
                    .filter(Subscription.status_id == status)\
                    .all()
                return subs_data
            except Exception as ex:
                db.session.rollback()
                raise ex
        
    def delete(self, id, user_id): 
        with DBConnectionHandler() as db:
            try:
                db.session.query(Subscription).filter(Subscription.id==id, Subscription.user_id==user_id).delete()
                db.session.commit()
            except Exception as ex:
                db.session.rollback()
                raise ex
                