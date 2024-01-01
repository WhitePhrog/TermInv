from domain.services.controllers.database_controller import DatabaseController
from domain.services.repositories.inventory_repository import InventoryRepository
from domain.models import Inventory


class InventoryRepositoryMySQL(InventoryRepository):
    def register_inventory(self, inventory: Inventory, database_controller: DatabaseController):
        database_controller.execute("INSERT INTO characters (name, capacity) VALUES (%s, %s)", (inventory.name, inventory.capacity))
        database_controller.commit()


    def get_inventory_by_id(self, id: int, database_controller: DatabaseController) -> Inventory:
        inventory = database_controller.execute(f"SELECT name, capacity FROM characters WHERE id={id}")
        return Inventory(**inventory)
    
    
    def get_all_inventories(self, database_controller: DatabaseController):
        inventories = database_controller.execute("SELECT * FROM characters")
        return [Inventory(**inventory_data) for inventory_data in inventories]
    
    
    def delete_inventory(self, id: int, database_controller: DatabaseController):
        database_controller.execute(f"DELETE FROM characters WHERE id={id}")
        database_controller.commit()
        
        
    def edit_inventory(self, id: int, target: str, substitute: str | int, database_controller: DatabaseController):
        database_controller.execute(f"UPDATE characters SET {target}={substitute} WHERE id={id}")
        database_controller.commit()