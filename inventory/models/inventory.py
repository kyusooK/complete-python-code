from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func
from .base import Base

class Inventory(Base):
    __tablename__ = "inventories"
    
    id = Column(Long, primary_key=True, index=True)
    productName = Column(String, nullable=True)
    qty = Column(Integer, nullable=True)
    photo = Column(Photo(100), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    def __repr__(self):
        return f"<Inventory(id={self.id})>"
