from src.config.database.base import Base
from sqlalchemy import String, Column, Integer, ForeignKey,DateTime
from datetime import datetime


class EventHistory(Base):
    __tablename__ = "event_histories"
    __table_args__ = {'extend_existing': True}
    
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    subscription_id = Column(Integer, ForeignKey("subscriptions.id", ondelete="Cascade"), nullable=False)
    type = Column(String(120), nullable=False)
    created_at = Column(DateTime, nullable=False)
    
    def __repr__(self) -> str:
        return f"<<id: {self.id}, subscription_id: {self.subscription_id},type: {self.type}, created_at: {self.created_at}>>"