import unittest
from unittest.mock import MagicMock, patch
from sqlalchemy.orm import Session
from models.order import Order
from services.order_service import OrderService
from repositories.order_repository import OrderRepository

class TestOrderService(unittest.TestCase):
    def setUp(self):
        # Mock database session
        self.db = MagicMock(spec=Session)
        
        # Create a mock order repository
        self.order_repository = MagicMock(spec=OrderRepository)
        
        # Create the order service with mocked repository
        with patch('services.order_service.OrderRepository', return_value=self.order_repository):
            self.order_service = OrderService(self.db)
    
    def test_get_orders(self):
        # Mock data
        mock_orders = [
            Order(id=1, qty=1, userId="test1", orderDate=None, inventoryId=None, address=None),
            Order(id=2, qty=2, userId="test2", orderDate=None, inventoryId=None, address=None)
        ]
        
        # Configure mock
        self.order_repository.get_all.return_value = mock_orders
        
        # Call the method
        result = self.order_service.get_orders()
        
        # Assertions
        self.order_repository.get_all.assert_called_once_with(0, 100)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].id, 1)
        self.assertEqual(result[1].id, 2)
    
    def test_get_order_by_id(self):
        # Mock data
        mock_order = Order(id=1, qty=1, userId="test1", orderDate=None, inventoryId=None, address=None)
        
        # Configure mock
        self.order_repository.get_by_id.return_value = mock_order
        
        # Call the method
        result = self.order_service.get_order(1)
        
        # Assertions
        self.order_repository.get_by_id.assert_called_once_with(1)
        self.assertEqual(result.id, 1)
    
    def test_create_order_success(self):
        # Mock data
        mock_order = Order(id=1, qty=1, userId="test1", orderDate=None, inventoryId=None, address=None)
        
        # Configure mocks
        self.order_repository.create.return_value = mock_order
        
            # Call the method
            result = self.order_service.create_order(
                qty=1,
                userId="test1",
                orderDate=None,
                inventoryId=None,
                address=None
            )
        
        # Assertions
        self.order_repository.create.assert_called_once_with(
            qty=1,
            userId="test1",
            orderDate=None,
            inventoryId=None,
            address=None
        )
        self.assertEqual(result.id, 1)
    

if __name__ == '__main__':
    unittest.main()
