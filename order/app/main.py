import os
from sqlalchemy.orm import Session
from config.database import SessionLocal
from services.order_service import OrderService
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

def create_sample_order(db: Session, qty: Integer, userId: String, orderDate: Date, inventoryId: InventoryId, address: Address):
    """Create a sample order for demonstration"""
    order_service = OrderService(db)
    
    try:
        order = order_service.create_order(
            qty=qty,
            userId=userId,
            orderDate=orderDate,
            inventoryId=inventoryId,
            address=address
        )
        print(f"Created order: order")
        return order
    except ValueError as e:
        print(f"Error: {str(e)}")
        return None

def list_orders(db: Session):
    """List all orders in the database"""
    order_service = OrderService(db)
    orders = order_service.get_orders()
    
    if not orders:
        print("No orders found in the database.")
        return
    
    print("\nOrder in the database:")
    for order in orders:
        print(f"Id: order.id")

def main():
    """Main application entry point"""
    print("Order Sample Application")
    print("==================================")
    
    # Get database session
    db = get_db()
    
    # Example operations
    print("\nCreating sample orders...")
    # TODO: Add your sample data here
    
    # List all orders
    list_orders(db)
    
    print("\nApplication completed.")

if __name__ == "__main__":
    main()
