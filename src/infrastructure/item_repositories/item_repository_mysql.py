'''
from domain.services.controllers.database_controller import DatabaseController
from domain.models import Item, Inventory

class ItemRepository:
    def register_item(self, character_id: int, item: Item, database_controller: DatabaseController):
        raise NotImplementedError
    
    
    def get_all_items_by_character_id(self, character_id: int, database_controller: DatabaseController): # -> list[Item]
        raise NotImplementedError
    
    
    def get_item_by_name(self, character_id: int, name: str, database_controller: DatabaseController) -> Item:
        raise NotImplementedError
    
    
    def delete_item(self, character_id: int, name: str, database_controller: DatabaseController):
        raise NotImplementedError
    
    
    def edit_item(self, character_id: int, name: str, target: str, substitute: str|int, database_controller: DatabaseController):
        raise NotImplementedError
'''

from domain.services.controllers.database_controller import DatabaseController
from domain.services.repositories.item_repository import ItemRepository
from domain.models import Item


class ItemRepositoryMySQL(ItemRepository):
    def register_item(self, character_id: int, item: Item, database_controller: DatabaseController):
        database_controller.execute()
        database_controller.commit()


    def get_all_items_by_character_id(self, id: int, database_controller: DatabaseController) -> Inventory:
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