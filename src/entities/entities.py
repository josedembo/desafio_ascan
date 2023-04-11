from src.config.database.base import Base
from sqlalchemy import Column, String, Integer, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from src.config.database.connection import DBConnectionHandler


class User(Base):
    __tablename__="users"
    __table_args__ = {'extend_existing': True}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(250), nullable=False)
    username = Column(String(20), nullable=False, unique=True)
    password = Column(Text(), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, onupdate=datetime.now())
    subscription = relationship("Subscription", backref="subscription.id", passive_deletes=True)
    
    def __repr__(self) -> str:
        return f"<<User id: {self.id}, name:{self.full_name}, created_at: {self.created_at}, updated_at: {self.updated_at} >>"
 
    
class Subscription(Base):
    __tablename__= "subscriptions"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    status_id = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, onupdate=datetime.now(), nullable=True)
    event_history = relationship("EventHistory", backref="event_histories.id", passive_deletes=True)
    
    def __repr__(self) -> str:
        return f"<<id: {self.id}, status_id: {self.status_id}, user_id: {self.user_id}, created_at: {self.created_at}, updated_at:{self.updated_at}>>"


class Status(Base):
    __tablename__="status"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    status_name = Column(String(50), nullable=False, unique=True)
    
    def __repr__(self) -> str:
        return f"<<id: {self.id}, status_name: {self.status_name}>>"


class EventHistory(Base):
    __tablename__ = "event_histories"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    subscription_id = Column(Integer, ForeignKey("subscriptions.id", ondelete="CASCADE"), nullable=False)
    type = Column(String(120), nullable=False)
    created_at = Column(DateTime, nullable=False)
    
    def __repr__(self) -> str:
        return f"<<id: {self.id}, subscription_id: {self.subscription_id},type: {self.type}, created_at: {self.created_at}>>"
    
    
if __name__ == "__main__":
    
    with DBConnectionHandler() as db:
        Base.metadata.create_all(db.get_engine())
