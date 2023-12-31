from domain.services.controllers.database_controller import DatabaseController
from domain.models import Inventory

class InventoryRepository:
    def create_inventory(self, inventory: Inventory, database_controller: DatabaseController):
        raise NotImplementedError
    
    
    def get_inventory_by_id(self, inventory: Inventory, database_controller: DatabaseController) -> Inventory:
        raise NotImplementedError