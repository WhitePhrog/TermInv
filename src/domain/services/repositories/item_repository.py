from domain.services.controllers.database_controller import DatabaseController
from domain.models import Item, Inventory

class ItemRepository:
    def create_item(self, item: Item, database_controller: DatabaseController):
        raise NotImplementedError
    
    
    def get_all_items_by_character_id(self, inventory: Inventory, database_controller: DatabaseController): # -> list[Item]
        raise NotImplementedError
    
    
    def get_item_by_name(self, name: str, database_controller: DatabaseController) -> Item:
        raise NotImplementedError
    