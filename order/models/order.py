from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func
from .base import Base

class Order(Base):
    __tablename__ = "orders"
    
    id = Column(Long, primary_key=True, index=True)
    qty = Column(Integer, nullable=True)
    userId = Column(String, nullable=True)
    orderDate = Column(Date, nullable=True)
    inventoryId = Column(InventoryId(100), nullable=True)
    address = Column(Address(100), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    def __repr__(self):
        return f"<Order(id={self.id})>"
