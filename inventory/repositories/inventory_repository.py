from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models.inventory import Inventory
from typing import List, Optional

class InventoryRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def get_all(self, skip: int = 0, limit: int = 100) -> List[Inventory]:
        """Get all inventories with pagination"""
        return self.db.query(Inventory).offset(skip).limit(limit).all()
    
    def get_by_id(self, id: Long) -> Optional[Inventory]:
        """Get a inventory by ID"""
        return self.db.query(Inventory).filter(Inventory.id == id).first()
    
    def create(self, productName: String, qty: Integer, photo: str) -> Optional[Inventory]:
        """Create a new inventory"""
        inventory = Inventory(
            productName=productName,
            qty=qty,
            photo=photo
        )
        
        try:
            self.db.add(inventory)
            self.db.commit()
            self.db.refresh(inventory)
            return inventory
        except IntegrityError:
            self.db.rollback()
            return None
    
    def update(self, id: Long, **kwargs) -> Optional[Inventory]:
        """Update a inventory's details"""
        inventory = self.get_by_id(id)
        if not inventory:
            return None
            
        for key, value in kwargs.items():
            if hasattr(inventory, key) and value is not None:
                setattr(inventory, key, value)
        
        self.db.commit()
        self.db.refresh(inventory)
        return inventory
    
    def delete(self, id: Long) -> bool:
        """Delete a inventory by ID"""
        inventory = self.get_by_id(id)
        if not inventory:
            return False
            
        self.db.delete(inventory)
        self.db.commit()
        return True 