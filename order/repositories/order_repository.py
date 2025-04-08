from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models.order import Order
from typing import List, Optional

class OrderRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def get_all(self, skip: int = 0, limit: int = 100) -> List[Order]:
        """Get all orders with pagination"""
        return self.db.query(Order).offset(skip).limit(limit).all()
    
    def get_by_id(self, id: Long) -> Optional[Order]:
        """Get a order by ID"""
        return self.db.query(Order).filter(Order.id == id).first()
    
    def create(self, qty: Integer, userId: String, orderDate: Date, inventoryId: str, address: str) -> Optional[Order]:
        """Create a new order"""
        order = Order(
            qty=qty,
            userId=userId,
            orderDate=orderDate,
            inventoryId=inventoryId,
            address=address
        )
        
        try:
            self.db.add(order)
            self.db.commit()
            self.db.refresh(order)
            return order
        except IntegrityError:
            self.db.rollback()
            return None
    
    def update(self, id: Long, **kwargs) -> Optional[Order]:
        """Update a order's details"""
        order = self.get_by_id(id)
        if not order:
            return None
            
        for key, value in kwargs.items():
            if hasattr(order, key) and value is not None:
                setattr(order, key, value)
        
        self.db.commit()
        self.db.refresh(order)
        return order
    
    def delete(self, id: Long) -> bool:
        """Delete a order by ID"""
        order = self.get_by_id(id)
        if not order:
            return False
            
        self.db.delete(order)
        self.db.commit()
        return True 