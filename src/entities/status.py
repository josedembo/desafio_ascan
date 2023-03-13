from src.config.database.base import Base
from sqlalchemy import String, Column, Integer, ForeignKey,DateTime
from datetime import datetime

class Status(Base):
    __tablename__="status"
    __table_args__ = {'extend_existing': True}
    
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    status_name = Column(String(50), nullable=False, unique=True)
    
    def __repr__(self) -> str:
        return f"<<id: {self.id}, status_name: {self.status_name}>>"