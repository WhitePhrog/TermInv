from domain.services.controllers.database_controller import DatabaseController
from domain.models import Inventory

class InventoryRepository:
    def register_inventory(self, inventory: Inventory, database_controller: DatabaseController):
        raise NotImplementedError
    
    
    def get_inventory_by_id(self, inventory: Inventory, database_controller: DatabaseController) -> Inventory:
        raise NotImplementedError
    
    
    def get_all_inventories(self, database_controller: DatabaseController): # -> list[Inventory]
        raise NotImplementedError
        
    
    def delete_inventory(self, inventory: Inventory, database_controller: DatabaseController):
        raise NotImplementedError
    
    
    def edit_inventory(self, inventory: Inventory, target: str, substitute: str|int,database_controller: DatabaseController):
        raise NotImplementedError
    