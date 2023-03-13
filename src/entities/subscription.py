from src.config.database.base import Base
from sqlalchemy import String, Column, Integer, ForeignKey,DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from src.config.database.connection import DBConnectionHandler

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

if __name__ == "__main__":
    
    with DBConnectionHandler() as db:
        Base.metadata.create_all(db.get_engine())