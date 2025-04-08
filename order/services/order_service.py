from sqlalchemy.orm import Session
from repositories.order_repository import OrderRepository
from models.order import Order
from typing import List, Optional, Dict
import hashlib
import os

class OrderService:
    def __init__(self, db: Session):
        self.order_repository = OrderRepository(db)
    
    def get_orders(self, skip: int = 0, limit: int = 100) -> List[Order]:
        """Get all orders with pagination"""
        return self.order_repository.get_all(skip, limit)
    
    def get_order(self, id: Long) -> Optional[Order]:
        """Get a order by ID"""
        return self.order_repository.get_by_id(id)
    
    def create_order(self, qty: Integer, userId: String, orderDate: Date, inventoryId: str, address: str) -> Optional[Order]:
        """Create a new order"""
        # Create the order
        return self.order_repository.create(
            qty=qty,
            userId=userId,
            orderDate=orderDate,
            inventoryId=inventoryId,
            address=address
        )
    
    def update_order(self, id: Long, data: Dict) -> Optional[Order]:
        """Update a order's details"""
            
        return self.order_repository.update(id, **data)
    
    
    def delete_order(self, id: Long) -> bool:
        """Delete a order by ID"""
        return self.order_repository.delete(id)
