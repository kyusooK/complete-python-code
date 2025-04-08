import unittest
from unittest.mock import MagicMock, patch
from sqlalchemy.orm import Session
from models.inventory import Inventory
from services.inventory_service import InventoryService
from repositories.inventory_repository import InventoryRepository

class TestInventoryService(unittest.TestCase):
    def setUp(self):
        # Mock database session
        self.db = MagicMock(spec=Session)
        
        # Create a mock inventory repository
        self.inventory_repository = MagicMock(spec=InventoryRepository)
        
        # Create the inventory service with mocked repository
        with patch('services.inventory_service.InventoryRepository', return_value=self.inventory_repository):
            self.inventory_service = InventoryService(self.db)
    
    def test_get_inventories(self):
        # Mock data
        mock_inventories = [
            Inventory(id=1, productName="test1", qty=1, photo=None),
            Inventory(id=2, productName="test2", qty=2, photo=None)
        ]
        
        # Configure mock
        self.inventory_repository.get_all.return_value = mock_inventories
        
        # Call the method
        result = self.inventory_service.get_inventories()
        
        # Assertions
        self.inventory_repository.get_all.assert_called_once_with(0, 100)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].id, 1)
        self.assertEqual(result[1].id, 2)
    
    def test_get_inventory_by_id(self):
        # Mock data
        mock_inventory = Inventory(id=1, productName="test1", qty=1, photo=None)
        
        # Configure mock
        self.inventory_repository.get_by_id.return_value = mock_inventory
        
        # Call the method
        result = self.inventory_service.get_inventory(1)
        
        # Assertions
        self.inventory_repository.get_by_id.assert_called_once_with(1)
        self.assertEqual(result.id, 1)
    
    def test_create_inventory_success(self):
        # Mock data
        mock_inventory = Inventory(id=1, productName="test1", qty=1, photo=None)
        
        # Configure mocks
        self.inventory_repository.create.return_value = mock_inventory
        
            # Call the method
            result = self.inventory_service.create_inventory(
                productName="test1",
                qty=1,
                photo=None
            )
        
        # Assertions
        self.inventory_repository.create.assert_called_once_with(
            productName="test1",
            qty=1,
            photo=None
        )
        self.assertEqual(result.id, 1)
    

if __name__ == '__main__':
    unittest.main()
