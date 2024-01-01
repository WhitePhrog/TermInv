from domain.services.controllers.database_controller import DatabaseController
from domain.services.repositories.inventory_repository import InventoryRepository
from domain.models import Inventory


class InventoryRepositoryMySQL(InventoryRepository):
    def register_inventory(self, inventory: Inventory, database_controller: DatabaseController):
        database_controller.execute("INSERT INTO characters (name, capacity) VALUES (%s, %s)", (inventory.name, inventory.capacity))
        database_controller.commit()
        print("\n----------------------------------------------\n"
              "Inventory registered. It can now be\n"
              "accessed through the main menu.")


    def get_inventory_by_id(self, id: int, database_controller: DatabaseController) -> Inventory:
        selected_inventory = database_controller.execute(f"SELECT name, capacity FROM characters WHERE id = %s", (id))
        return Inventory(**selected_inventory)
    
    
    def get_all_inventories(self, database_controller: DatabaseController):
        inventories = database_controller.execute("SELECT * FROM characters")
        return [Inventory(**inventory_data) for inventory_data in inventories]
    
    
    def delete_inventory(self, inventory: Inventory, database_controller: DatabaseController):
        database_controller.execute("DELETE FROM characters WHERE id = %s", (inventory.id))
        database_controller.execute("DELETE FROM items WHERE character_id = %s", (inventory.id))
        database_controller.commit()
        
        
    def edit_inventory(self, inventory: Inventory, target: str, substitute: str | int, database_controller: DatabaseController):
        database_controller.execute("UPDATE characters SET %s = %s WHERE id = %s", (target, substitute, inventory.id))
        database_controller.commit()