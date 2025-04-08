from sqlalchemy.orm import Session
from repositories.inventory_repository import InventoryRepository
from models.inventory import Inventory
from typing import List, Optional, Dict
import hashlib
import os

class InventoryService:
    def __init__(self, db: Session):
        self.inventory_repository = InventoryRepository(db)
    
    def get_inventories(self, skip: int = 0, limit: int = 100) -> List[Inventory]:
        """Get all inventories with pagination"""
        return self.inventory_repository.get_all(skip, limit)
    
    def get_inventory(self, id: Long) -> Optional[Inventory]:
        """Get a inventory by ID"""
        return self.inventory_repository.get_by_id(id)
    
    def create_inventory(self, productName: String, qty: Integer, photo: str) -> Optional[Inventory]:
        """Create a new inventory"""
        # Create the inventory
        return self.inventory_repository.create(
            productName=productName,
            qty=qty,
            photo=photo
        )
    
    def update_inventory(self, id: Long, data: Dict) -> Optional[Inventory]:
        """Update a inventory's details"""
            
        return self.inventory_repository.update(id, **data)
    
    
    def delete_inventory(self, id: Long) -> bool:
        """Delete a inventory by ID"""
        return self.inventory_repository.delete(id)
