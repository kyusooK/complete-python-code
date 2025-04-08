import os
from sqlalchemy.orm import Session
from config.database import SessionLocal
from services.inventory_service import InventoryService
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_db():
    """Creates a new database session for each request"""
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()

def create_sample_inventory(db: Session, productName: String, qty: Integer, photo: Photo):
    """Create a sample inventory for demonstration"""
    inventory_service = InventoryService(db)
    
    try:
        inventory = inventory_service.create_inventory(
            productName=productName,
            qty=qty,
            photo=photo
        )
        print(f"Created inventory: inventory")
        return inventory
    except ValueError as e:
        print(f"Error: {str(e)}")
        return None

def list_inventories(db: Session):
    """List all inventories in the database"""
    inventory_service = InventoryService(db)
    inventories = inventory_service.get_inventories()
    
    if not inventories:
        print("No inventories found in the database.")
        return
    
    print("\nInventory in the database:")
    for inventory in inventories:
        print(f"Id: inventory.id")

def main():
    """Main application entry point"""
    print("Inventory Sample Application")
    print("==================================")
    
    # Get database session
    db = get_db()
    
    # Example operations
    print("\nCreating sample inventories...")
    # TODO: Add your sample data here
    
    # List all inventories
    list_inventories(db)
    
    print("\nApplication completed.")

if __name__ == "__main__":
    main()
